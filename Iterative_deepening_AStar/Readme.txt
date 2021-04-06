The solution has been coded in python 3.6.1

The has the following components:

1) IDAStar: a userdefined data structure for string the details of the puzzle

2) solve: To iteratively calls the _search function.

3) _search: Searches for a goal node.

4) slide_solved_state(n): converts tiles into tuples

5) slide_neighbours(n): finda the neighbour for the node.

6) neighbours(p): works to find the childern of node p

7) encode_cfg(cfg, n): encodes the input into the desired format

8) gen_wd_table(n): Heuristic funtion for manhattan distance

9) slide_wd(n,goal): Heuristic funtion to calculate misplaced tiles

10) main(): the driver function the code.


Note:
The two test cases provided are passed in the test list in main function.
