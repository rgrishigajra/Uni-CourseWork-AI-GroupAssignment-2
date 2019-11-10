#!/usr/local/bin/python3

"""
This is where you should write your AI code!

Authors: PLEASE ENTER YOUR NAMES AND USER ID'S HERE

Based on skeleton code by Abhilash Kuhikar, October 2019
"""

from logic_IJK import Game_IJK
import random,copy

# Suggests next move to be played by the current player given the current game
#
# inputs:
#     game : Current state of the game
#
# This function should analyze the current state of the game and determine the
# best move for the current player. It should then call "yield" on that move.

def next_move(game: Game_IJK)-> None:

    '''board: list of list of strings -> current state of the game
       current_player: int -> player who will make the next move either ('+') or -'-')
       deterministic: bool -> either True or False, indicating whether the game is deterministic or not
    '''

    board = game.getGame()
    player = game.getCurrentPlayer()
    deterministic = game.getDeterministic()

    # You'll want to put in your fancy AI code here. For right now this just
    # returns a random move.
    #move=alpha_beta_decision(game)
    #yield move
    #if player=='+':
    #    yield move
    #else:
    yield random.choice(['U','D','L','R'])

# Check if given array is Monotonic
def is_monotonic(row):
    return (all(row[i].upper() >= row[i + 1].upper() for i in range(len(row) - 1)))

def monotonicity(game: Game_IJK):
    score=0
    score+=sum([1 for row in game.getGame() if is_monotonic(row)])
    score+=sum([1 for row in game._Game_IJK__transpose(game.getGame()) if is_monotonic(row)])
    return score

def get_difference(row):
    return (sum(abs(ord(row[i].upper())-ord(row[i+1].upper())) for i in range(len(row)-1) if row[i]!=' '))

def smoothness(game:Game_IJK):
    smoothness=0
    smoothness-=sum([get_difference(row) for row in game.getGame()])
    smoothness-=sum([get_difference(row) for row in game._Game_IJK__transpose(game.getGame())])
    return 0.1*smoothness

#Generate successors for a given game state
def successor(game: Game_IJK):
    return [copy.deepcopy(game).makeMove(move) for move in ['U','L','D','R']]

#Take an decision
def alpha_beta_decision(game: Game_IJK):
    boards=successor(game)
    min_values=[min_value(copy.deepcopy(board),float('-inf'),float('inf'),1)[2] for board in boards]
    return ['U','L','D','R'][min_values.index(max(min_values))]

def max_value(game: Game_IJK,alpha,beta,depth):
    if game.state() != 0 or depth==4:
        #Evaluation function
        return (game,monotonicity(game)+smoothness(game),beta)
    depth+=1
    for board in successor(game):
        alpha=max(alpha,min_value(copy.deepcopy(board),alpha,beta,depth)[2])
        if alpha>=beta:
            return (board,alpha,beta)
    return (game,alpha,beta)

def min_value(game: Game_IJK,alpha,beta,depth):
    if game.state() != 0 or depth==4:
        #Evaluation function
        return (game,alpha,monotonicity(game)+smoothness(game))
    depth+=1
    for board in successor(game):
        beta=min(beta,max_value(copy.deepcopy(board),alpha,beta,depth)[1])
        if beta<=alpha:
            return (board,alpha,beta)
    return (game,alpha,beta)