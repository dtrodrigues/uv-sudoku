This solves Sudoku puzzles using `uv`'s dependency resolver. Inspired by https://www.splitgraph.com/blog/poetry-dependency-resolver-sudoku .

You must have [uv](https://github.com/astral-sh/uv) installed and in your PATH.

Usage:
1. `python3 generate-packages.py` # only needs to be run once
2. `python3 sudoku.py <input_data>` 

Example:
```
$ python3 sudoku.py 300400090000000064800090100000000000030002900500010700070050300020100607060040000
3 5 6 4 7 1 8 9 2
7 9 1 8 2 3 5 6 4
8 4 2 6 9 5 1 7 3
2 1 7 5 6 9 4 3 8
6 3 4 7 8 2 9 5 1
5 8 9 3 1 4 7 2 6
4 7 8 2 5 6 3 1 9
9 2 5 1 3 8 6 4 7
1 6 3 9 4 7 2 8 5
```
