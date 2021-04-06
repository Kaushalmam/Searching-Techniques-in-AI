from collections import namedtuple
import Queue
def find(start):
    
    SearchPos = namedtuple('SearchPos', 'node, prev')
    position = SearchPos(start, None)
    frontier = [position]       #this is used to store nodes that are to be explored
    explored = []               #this is used to store nodes that are already explored
    while len(frontier) > 0:

        #current position is the first position in the frontier
        position = frontier.pop(0)

        node = position.node

        #goal test will return True if the current node is goal_state
        if goal_test(node):
            Goal = namedtuple('Goal', 'position, nodes_expanded')
            success = Goal(position, len(explored))
            return success

        #expanded nodes are added to explored set
        explored.append(node)

        #All reachable positions from current postion is added to frontier
        for i in node.successors():
            new_position = SearchPos(i, position)
            frontier_check = i in [p.node for p in frontier]
            if i not in explored and not frontier_check:
                frontier.append(new_position)

#This function will check if we have reached the goal state  
def goal_test(state):
    
     goalList = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,0]
     return str(state) == str(goalList)


#Following code snippit checks if the input is solveable
def coun(x):
    
    count = 0;
    #i=0
    for i in range(0,16):
        j=i+1
        while j<16:
            if (x[j] and x[i] and x[i] > x[j]):
                count=count + 1;
            j += 1
      #  i+= 1
    return count;

def getzero(y):
    
    for i in range(0,16):
        if y[i] == 0:
            return 4-int(i/4)
    
def check(k):
    
    count = coun(k)
    row = getzero(k)
    if (row%2==0 and count%2!=0) or (row%2!=0 and count%2==0):
        return True
    return False
        
