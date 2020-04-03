The program has been coded in python 3.6.1.


The code has some global variables to store the information about the board.

Following functions are inplemented to obtained the desired result:

1) informationModule(action, finalTime): this gives all the desired information as output on the terminal screen.

2) dls(root,depth): Used to call limited_search funtion and return its resursive result.

3) iterative_deepening(root): rcursively calls dls funtion with incremental depth.

4) limited_search(root,depth_limit,action): performs limited depth first search for root node passed as parameter.

5) goalTest(x): tells if a node x is root or not.

6) checker(x): check if the input, passed as parameter, is solvable or not.

7) actions(n): Used to perform up,down,left and right operations on node n.

8) main(): this is the driver function of the program.

Note: Input is taken at run time. 
Only one configuration of 15 puzzle problem can be passed as input at a time.
If running in 2.7 version convert "input" function used in main function to "raw_input"