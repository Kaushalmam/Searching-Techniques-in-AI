import time
import os
import psutil
goal = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,0]
expanded_nodes=0    #initializing some global variables to store the information of board
initial_time = 0
time_limit = 4200

def informationModule(action, finalTime):    #this function gives the desired information about the board
    global expanded_nodes
    movements = "->".join(actn for actn in action) #directions to reach Goal
    pro = psutil.Process(os.getpid())  
    overall_time = finalTime - initial_time #time taken
    print ("No. of nodes expanded by the agent-	", expanded_nodes)                         
    print ("Memory consumption-	    	        ", str(round(pro.memory_info()[0]/float(2**20)))+" KBs (approximate value)")
    print ("Computation time- 		        ", round(overall_time) ,"sec")
    print ("Moves to reach GOAL-			", movements)
    

def dls(root,depth):
    return limited_search(root,depth,[])

def iterative_deepening(root):
    #increases the depth and calls limited search funtion to perform limited dfs
    current_node= root
    depth=0
    while True:
        status = dls (root, depth)
        if status == "success":
            return
        elif status == "failed":
            print("no solution exists")
            return
        elif status == "delayed":
            print("computation didnt complete within time limit")
            return
        depth +=1
    return

def limited_search (root,depth_limit,action):
    #performs depth first search upto a certaian depth
    global initial_time
    global expanded_nodes
    curr_time=time.time()-initial_time #stores the computational time
    
    if curr_time>time_limit:
        print("cant find Solution")
        return "delayed"
    
    if goalTest(root):
        informationModule(action, time.time())
        return "success"
    elif depth_limit <= 0:
        return "limit reached"
    else:
        expanded_nodes +=1
        backTrack= False
        action_state_pairs=actions(root)
        for action_state in action_state_pairs:
            new_state = action_state[1]
            temp= action[:]
            temp.append(action_state[0])
            status = limited_search (new_state, depth_limit-1, temp)
            if status == "limit reached":
                backTrack= True
            elif status != "failed":
                return status
        if backTrack == True:
            return status
        else:
            return "failed"
            

def goalTest (x):   #This performs goal test
    return (str(x) == str(goal))
def checker(x):
    #this will check if the input is solvable
    count = 0; 
    for i in range (0,16):
        j=i+1
        while j<16:
            if (x[j] and x[i] and x[i] > x[j]):
                count=count + 1;
            j += 1
    for i in range(0,16):
        if x[i] == 0:
            blank= 4-int(i/4)
    if (blank%2==0 and count%2!=0) or (blank%2!=0 and count%2==0):
        return True
    return False
  
def actions(n):
    traversal = []  #stores the path to Goal state
    blankTile =  n.index(0) #stores the index of blank tile
    
    #move left operation    
    if  blankTile not in [0,4,8,12]:
         n[ blankTile],  n[ blankTile-1] =  n[ blankTile-1],  n[ blankTile]
         traversal += [['L',  n[:]]]
         n[ blankTile],  n[ blankTile-1] =  n[ blankTile-1],  n[ blankTile]

    #move up operation
    if blankTile not in [0,1,2,3]:
         n[blankTile],  n[blankTile-4] =  n[blankTile-4],  n[blankTile]
         traversal += [['U',  n[:]]]
         n[ blankTile],  n[ blankTile-4] =  n[ blankTile-4],  n[ blankTile]
         
    #move right operation    
    if blankTile not in [3,7,11,15]:
         n[ blankTile],  n[ blankTile+1] =  n[ blankTile+1],  n[ blankTile]
         traversal += [['R',  n[:]]]
         n[ blankTile],  n[ blankTile+1] =  n[ blankTile+1],  n[ blankTile]
         
    #move down operation    
    if 0 <=  blankTile not in [12,13,14,15]:
         n[ blankTile],  n[ blankTile+4] =  n[ blankTile+4],  n[ blankTile]
         traversal += [['D',  n[:]]]
         n[ blankTile],  n[ blankTile+4] =  n[ blankTile+4],  n[ blankTile]   
    return traversal

def main():
    #main or driver function
    board = []
    generate = []
    global initial_time
    initial_time = time.time()
    puzzle = input ("Enter a valid input:" )
    board= puzzle.split()
    generate =[int(i) for i in board]
    solvable = checker(generate)
    if (solvable == True):
        iterative_deepening(generate)
    else:
        print ("Unsolvable input")


if __name__ == '__main__':
    main()





    




        

