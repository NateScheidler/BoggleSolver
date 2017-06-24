#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon May 22 19:34:09 2017

@author: nathanielscheidler
"""
import dictrie
import collections

    
class solver():
    def __init__(self, e_l):
        self.found_words = set()
        self.e_l = e_l
        self.t = dictrie.Dictrie()
        with open('dictionary.txt') as dictionary: # this takes like 5 seconds
            for word in dictionary:
                self.t.add(word.lower().strip())
    
    def solve_(self, board, path):
        neighbors = []
        #print path
        cur = next(reversed(path))

        for i in range(cur[0]-1, cur[0]+2):
            for j in range(cur[1]-1, cur[1]+2):
                if 0 <= i <= self.e_l-1 and 0 <= j <= self.e_l-1 and not path.has_key((i,j)):
                    neighbors.append((i,j))
        
        cur_word = ""
        for pos in path:
            cur_word += path[pos]
            
        for p in neighbors:
            try_letter = board[p[0]][p[1]]
            try_word = cur_word + try_letter
            try_path = collections.OrderedDict.copy(path)
            try_path[p] = try_letter
            if self.t.contains_path(try_word):
                if self.t.contains(try_word):
                    self.found_words.add(try_word)
                self.solve_(board, try_path)
    
    def solve(self, board):
        self.found_words = set()
        for i in range(0,self.e_l):
            for j in range(0,self.e_l):
                path = collections.OrderedDict()
                path[(i,j)] = board[i][j]
                self.solve_(board, path)
        return self.found_words
