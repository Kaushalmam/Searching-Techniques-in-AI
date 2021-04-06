from state import State
import search
import time
import os
import psutil       

def path(last_pos):     #This function will return the moves to be done to reach the goal state
    pos = last_pos.prev
    next_pos = last_pos
    p=" "
    
    while pos != None:
        if pos.node.up() == next_pos.node:
            p="U"+p    
        elif pos.node.down() == next_pos.node:
            p="D"+p            
        elif pos.node.left() == next_pos.node:
            p="L"+p            
        elif pos.node.right() == next_pos.node:
            p="R"+p
        pos = pos.prev
        next_pos = next_pos.prev
    return p
def main():
    problem = raw_input ()       #This asks for am input from the users and accepts it as string
    problem_as_list= problem.split()    #This splits the string received on the basis of blankspace
    operable_problem =[int(k) for k in problem_as_list] #Converts that string list into an interger list
    start_time = time.time()
    if (0  in operable_problem):
        c=search.check(operable_problem)      # c is a boolean variable that stores if the input has a solution or not.
        if(c == True):
            print ("Solution exists")
            game = State(operable_problem)           #This ststement will convert our input into a customized data-structure State     
            result = search.find(game)   #This will run bfs function in search.py file.
            final_pos = result.position
            nodes_expanded = result.nodes_expanded
            print "Time taken", time.time() - start_time
            p = psutil.Process(os.getpid())                             
            print "Memory consumed", str(p.memory_info()[0]/float(2**20))+"KB"
            print "Number of times node was expanded" , nodes_expanded
            print "Path or moves to take in order to reach goal state",path(final_pos)
        else:
            print ("There is no solution to this puzzle")

    else:
        print ("Can't find a solution")
    
if __name__== "__main__":
    main()
