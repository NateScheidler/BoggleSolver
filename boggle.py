#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 14 23:55:35 2017

@author: nathanielscheidler
"""
import random
import collections
import solver

# This is the letter set from Scrabble, used here to make decent boards
abc = 'aaaaaaaaabbccddddeeeeeeeeeeee' + \
      'ffggghhiiiiiiiiijkllllmmnnnnn' + \
      'nooooooooppqrrrrrrssssttttttuuuuvvwwxyyz' 

# Generates an n by n square board
def gen_board(n):
    board = []
    for i in range(n):
        row = []
        for j in range(n):
            c = abc[random.randint(0,len(abc)-1)]
            row.append(c)
        board.append(row)
    return board

def pretty_print(board):
    for i in range(len(board)):
        print board[i]


edge = 4

lst_board = 'D C L P  E I A E  R N T R  S E G S'.lower().split()


board = []
for i in range(0,16,4):
    board.append(lst_board[i:i+4])
pretty_print(board)
s = solver.solver(edge)
words =  sorted(s.solve(board))
print words

score = 0
for word in words:
    if len(word) == 3 or len(word) == 4:
        score += 1
    if len(word) == 5:
        score += 2
    if len(word) == 6:
        score += 3
    if len(word) > 6:
        score += 5
print score
    
'''

path = collections.OrderedDict()

path[(0,0)] = 'a'
path[(0,1)] = 'r'
path[(0,2)] = 't'
cur = (0,3)

e_l = 4

cur_word = ""
for pos in path:
    cur_word += path[pos]
for i in range(cur[0]-1, cur[0]+2):
    for j in range(cur[1]-1, cur[1]+2):
        print i,j, 0 <= i <= e_l, 0 <= j <= e_l, not path.has_key((i,j)) 
        '''

