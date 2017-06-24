#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 11 18:05:44 2017

@author: nathanielscheidler
"""

#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Mar  4 16:37:15 2017

@author: nathanielscheidler
"""

"""
Next steps:
    Come up with a way to store and retrieve trie in file
    Turn this into a boggle solver
    Turn that into a letterpress solver
    optional: make a letterpress OCR thingamajigger
    finally: achieve high score on letterpress
"""

class Dictrie:
    def __init__(self, letter=None):
        self.letter_map = {}
        self.letter = letter
        self.ends_word = False
        
    def add(self, word):
        if len(word) == 0:
            self.ends_word = True
        else:
            if not self.letter_map.has_key(word[0]):
                new_node = Dictrie(word[0])
                self.letter_map[word[0]] = new_node
            self.letter_map.get(word[0]).add(word[1:])

    
    def contains_path(self, word):
        if len(word) == 0:
            return True
        if not self.letter_map.has_key(word[0]):
            return False
        else:
            return self.letter_map.get(word[0]).contains_path(word[1:])
                
    def contains(self, word):
        if len(word) == 0:
                if self.ends_word:
                    return True
                else:
                    return False
        if not self.letter_map.has_key(word[0]):
            return False
        else:
            return self.letter_map.get(word[0]).contains(word[1:])



    