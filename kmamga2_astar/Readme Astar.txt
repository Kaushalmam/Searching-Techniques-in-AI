The program has been coded in python 3.6.1.

The program has two userdefined datatypes:

1) Board
	This stores all the information about the board configuraton and performs actions on the same.

2) Node:
	This dtores all the information about the node. For instance, Parent, state and action. It also compares if towo nodes are equal or not.

These are the funtions in the code:

1) get_children(parent_node): Finds the childern to the parent node.

2) find_path(node): Finds the path to traverse and reach the Goal.

3) manhattanDist(tiles): Calculates the Manhattan Distance for the Current configuration of the code.

4) tiles_misplaced(tiles): Returns the number of tiles misplaced in the current configuration.

5) run_astar(root_node): Performs the A star search starting from Root node.

6) goal_test(cur_tiles): Returns True if the Goal state is reached.

7) main(): This is the driver function of the code.

Note: There are two heuristics that can be used in the program, Manhattan distance and number of misplaced tiles. Initially the code runs on the Manhattan distance heuristic, but this can be changed by changing the function call from manhattanDist(tiles) to tiles_misplaced(tiles). There are comments where the changes are required to be done.