#!/usr/local/bin/python3
#
# Authors: [PLEASE PUT YOUR NAMES AND USER IDS HERE]
#
# Mountain ridge finder
# Based on skeleton code by D. Crandall, Oct 2019
#

from PIL import Image
from numpy import *
from scipy.ndimage import filters
import sys
import imageio


# calculate "Edge strength map" of an image
#
def edge_strength(input_image):
    grayscale = array(input_image.convert('L'))
    filtered_y = zeros(grayscale.shape)
    filters.sobel(grayscale, 0, filtered_y)
    return sqrt(filtered_y ** 2)


# draw a "line" on an image (actually just plot the given y-coordinates
#  for each x-coordinate)
# - image is the image to draw on
# - y_coordinates is a list, containing the y-coordinates and length equal to the x dimension size
#   of the image
# - color is a (red, green, blue) color triple (e.g. (255, 0, 0) would be pure red
# - thickness is thickness of line in pixels
#
def draw_edge(image, y_coordinates, color, thickness):
    for (x, y) in enumerate(y_coordinates):
        for t in range(int(max(y - int(thickness / 2), 0)), int(min(y + int(thickness / 2), image.size[1] - 1))):
            image.putpixel((x, t), color)
    return image


# main program
#
(input_filename, gt_row, gt_col) = sys.argv[1:]

# load in image 
input_image = Image.open(input_filename)

# compute edge strength mask
edge_strength = edge_strength(input_image)
imageio.imwrite('edges.jpg', uint8(255 * edge_strength / (amax(edge_strength))))
# You'll need to add code here to figure out the results! For now,
# just create a horizontal centered line.


ridge_bayes = argmax(edge_strength, axis=0)
print(ridge_bayes)

imageio.imwrite("output.jpg", draw_edge(input_image, ridge_bayes, (255, 255, 0), 5))

ridge_viterbi = argmax(edge_strength, axis=0)
#print(type(ridge_viterbi))

trans_probab = [0.4, 0.2, 0.075, 0.025]
state_probab = zeros((141, 251))
max_state = zeros((141,251))
#print(max_state.shape)
for row in range(0, 141):
    state_probab[0][row] = edge_strength[0][row]

for col in range(1, 251):
    for row in range(0, 141):
        max = 0
        for j in range(-3, 4):
            # print(i,j)
            if ((row + j <= 140) & (row + j >= 0)):
                if (max < state_probab[row + j][col - 1] * trans_probab[abs(j)]):
                    max = state_probab[row + j][col - 1] * trans_probab[abs(j)]
                    #print(row,col)
                    max_state[row][col] = row + j
                state_probab[row][col] = edge_strength[row][col]/10 * max
    #print(argmax(state_probab), max_state)
#for row in range(0,140):
#print(argmax(state_probab[:,250]))
#print((state_probab[25,250]))
#print(state_probab[:,250])
max=argmax(state_probab[:,250])
for col in range(250,-1,-1):
    #print(max)
    ridge_viterbi[col]=int(max)
    max=max_state[int(max)][col]
print(ridge_viterbi)
# for col in range(250,-1,-1):
#     state_probab[][]
imageio.imwrite("output.jpg", draw_edge(input_image, ridge_viterbi, (0, 255, 0), 5))


ridge_human = [edge_strength.shape[0] / 4] * edge_strength.shape[1]
# imageio.imwrite("output.jpg", draw_edge(input_image, ridge_human, (0, 0, 255), 5))
