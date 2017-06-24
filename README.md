BoggleSolver
============

This boggle solver works by first assembling a trie for fast dictionary lookups, and then performing a depth-first-search on the board for words.

dictrie.py contains the trie implementation.

solver.py includes the dictionary build and solver. The dictionary takes a few seconds to build, so the Solver class builds the dictionary on initialization and uses it to solve a board with solver.solve(board).

boggle.py contains an example of the Solver class in use.
