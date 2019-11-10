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
gt_col=int(gt_col)
gt_row=int(gt_row)
# load in image
input_image = Image.open(input_filename)

# compute edge strength mask
edge_strength = edge_strength(input_image)
imageio.imwrite('edges.jpg', uint8(255 * edge_strength / (amax(edge_strength))))
# You'll need to add code here to figure out the results! For now,
# just create a horizontal centered line.

# answer for 2.1, finds maximum edge strength per column and returns an array.
# we dont need to divide with the total edge strength value here since its a comparison
# so denominator can be ignored for all terms

ridge_bayes = argmax(edge_strength, axis=0)
imageio.imwrite("output_simple.jpg", draw_edge(input_image, ridge_bayes, (0, 0, 255), 5))

#answer for part 2.2, does viterbi implmentation with bottom up and memoization

ridge_viterbi = zeros(edge_strength.shape[1])
total_gradient=zeros(edge_strength.shape[1])
<<<<<<< HEAD
#transition probability values
#if the state is in same row = 0.5
#if state is in a row above or below = 0.2545
#is state is in two rows above or below = 0.005
#for the rest, we assume transition probabilities to be zero and never calculate those transitions in viterbi
trans_probab = [0.5,0.2545,0.005]
#sums up the edge strength values per column
=======
trans_probab = [0.5,0.15,0.01]
>>>>>>> 0f41c5cb4fa411578ce43963dd5451ddca685122
for col in range(0, edge_strength.shape[1]):
    for row in range(0,edge_strength.shape[0]):
        total_gradient[col]+=edge_strength[row][col]
#final array
state_probab = zeros((edge_strength.shape[0], edge_strength.shape[1]))
#array to store previous state for back tracking
max_state = zeros((edge_strength.shape[0],edge_strength.shape[1]))
#calculating initial starting state probabilities
for row in range(0, edge_strength.shape[0]):
    state_probab[row][0] = edge_strength[row][col]/total_gradient[0]

#calculating state probabilities of each node using viterbi
for col in range(1, edge_strength.shape[1]):
    for row in range(0, edge_strength.shape[0]):
        maxi = 0
        for j in range(-2, 3):
            # print(i,j)
            if ((row + j < edge_strength.shape[0]) & (row + j >= 0)):
                if (maxi< state_probab[row + j][col - 1] * (trans_probab[abs(j)])):
                    maxi = (state_probab[row + j][col - 1]) * (trans_probab[abs(j)])
                    #print(row,col)
                    max_state[row][col] = row + j
                state_probab[row][col] = (edge_strength[row][col]/100) * (maxi)

#finding the node with maximum probability in final column
maxi=argmax(state_probab[:,edge_strength.shape[1]-1])
#backtracking to solution based on memory storage of previous max product stored in viterbi
for col in range(edge_strength.shape[1]-1,-1,-1):
    ridge_viterbi[col]=int(maxi)
    maxi=max_state[int(maxi)][col]
input_image = Image.open(input_filename)
imageio.imwrite("output_map.jpg", draw_edge(input_image, ridge_viterbi, (255, 0, 0), 5))

#solution for part2.3 human input and viterbi
ridge_human = [edge_strength.shape[0] / 4] * edge_strength.shape[1]
<<<<<<< HEAD

#assigning human input values in the state probabilities
=======
>>>>>>> 0f41c5cb4fa411578ce43963dd5451ddca685122
for row in range(0,edge_strength.shape[0]):
    state_probab[row][gt_col]=0
state_probab[gt_row][gt_col]=1

#propagating the change from human input backwards (previous columns)
for col in range(gt_col-1, 0, -1):
    for row in range(gt_row-1, 0, -1):
        maxi = 0
        for j in range(-2, 3):
            if ((row + j < edge_strength.shape[0]) & (row + j >= 0)):
                if (maxi< state_probab[row + j][col + 1] * (trans_probab[abs(j)])):
                    maxi = (state_probab[row + j][col + 1]) * (trans_probab[abs(j)])
                    max_state[row][col] = row + j
                state_probab[row][col] = (edge_strength[row][col]/100) * (maxi)

#propagating the change from human input forwards (columns ahead)
for col in range(gt_col+1, edge_strength.shape[1]):
    for row in range(gt_row+1, edge_strength.shape[0]):
        maxi = 0
        for j in range(-2, 3):
            if ((row + j < edge_strength.shape[0]) & (row + j >= 0)):
                if (maxi< state_probab[row + j][col - 1] * (trans_probab[abs(j)])):
                    maxi = (state_probab[row + j][col - 1]) * (trans_probab[abs(j)])
                    max_state[row][col] = row + j
                state_probab[row][col] = (edge_strength[row][col]/100) * (maxi)
#backtracking to find solution in a similar way as viterbi

maxi=argmax(state_probab[:,edge_strength.shape[1]-1])
for col in range(edge_strength.shape[1]-1,-1,-1):
    ridge_human[col]=int(maxi)
    maxi=max_state[int(maxi)][col]
<<<<<<< HEAD
input_image = Image.open(input_filename)
imageio.imwrite("output_human.jpg", draw_edge(input_image, ridge_human, (0, 255, 0), 5))
=======
imageio.imwrite("output.jpg", draw_edge(input_image, ridge_human, (0, 0, 255), 5))
>>>>>>> 0f41c5cb4fa411578ce43963dd5451ddca685122
