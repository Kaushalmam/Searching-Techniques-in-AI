import random
import math
import time
import psutil
import os
from collections import deque


class Board:
    def __init__(self, tiles):                              #Constructor that initialize the values to a Board type variable

        self.size = int(math.sqrt(len(tiles)))
        self.tiles = tiles


    def execute_action(self, action):                       #Function that executes actions on the board and returns the resultiong configuration of the board
        new_tiles = self.tiles[:]
        empty_index = new_tiles.index('0')
        if action == 'l':
            if empty_index % self.size > 0:                 #performs Left action
                new_tiles[empty_index -
                          1], new_tiles[empty_index] = new_tiles[empty_index], new_tiles[empty_index-1]
        if action == 'r':
            if empty_index % self.size < (self.size-1):     #performs Right action
                new_tiles[empty_index +
                          1], new_tiles[empty_index] = new_tiles[empty_index], new_tiles[empty_index+1]
        if action == 'u':
            if empty_index-self.size >= 0:                  #performs Up action
                new_tiles[empty_index-self.size], new_tiles[empty_index] = new_tiles[empty_index], new_tiles[empty_index-self.size]
        if action == 'd':
            if empty_index+self.size < self.size*self.size: #performs Down action
                new_tiles[empty_index+self.size], new_tiles[empty_index] = new_tiles[empty_index], new_tiles[empty_index+self.size]
        return Board(new_tiles)

class Node:
    def __init__(self, state, parent, action):              #Constructor that initialize the values to a Node type variable
        self.state = state
        self.parent = parent
        self.action = action
    def __eq__(self, other):                                #Compares if two Node type variables are equal and return True or False
        return self.state.tiles == other.state.tiles

def get_children(parent_node):                              #Function the expands a node
    children = []
    actions = ['l', 'r', 'u', 'd']
    for action in actions:
        child_state = parent_node.state.execute_action(action)
        child_node = Node(child_state, parent_node, action)
        children.append(child_node)
    return children

def find_path(node):                                        #Funtion that finds a path to the goal state
    path = []
    while(node.parent is not None):
        path.append(node.action)
        node = node.parent
    path.reverse()
    return path


def manhattanDist(tiles):
                                                            #Manhattan distance is the sum of the distance of misplaced tiles from their correct position.
    distance = 0
    for i in range(4):
        for j in range(4):
            value = int(tiles[(i*4)+j])
            if value == 0:                                  #we dont consider the blank space while computing Manhattan distance
                continue  
            distance += abs(i - (value - 1) / 4) + abs(j - (value - 1) % 4) #Adds the value to distance equal to the value by which a current tile is off from its desired loctaion
    return distance


def tiles_misplaced(tiles):                                 #counts the number of misplaced tiles in the code
    misplaced_tiles = 0
    compare=['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','0']
    for i in range(0,16):
        if(tiles[i]!=compare[i]):
            misplaced_tiles+=1                              #increments misplaced is there exists a tile that is not at its desired location

    return misplaced_tiles


def run_astar(root_node):                                   #This functin performs the A* search
    start_time = time.time()
    
    m_dist = manhattanDist(root_node.state.tiles)         #To use the misplaced tile heuristic use tiles_misplaced(root_node.state.tiles) here
    frontier = [[m_dist, root_node]]                        #Frontier stores the value of heuristic funtion and the current and previous states of input
    explored = []                                           #Stores the nodes that are already explored.
    count = 0                                               #Counts the number of nodes explanded
    while frontier:
        i = 0

        cur_time = time.time()                              #Stores the time used by the code
        if (cur_time - start_time) > 30:                    #If it takes too long to calculate the solution 
            return "solution not found"

        for j in range(1, len(frontier)):                   #Looks for an entry in frontier that has minimun heuristic value
            if frontier[i][0] > frontier[j][0]:
                i = j

        curr_path_heur = frontier[i][0]                     #stores the heuristic value for the current node
        cur_node = frontier[i][-1]                          #stores the configuration of the current node
        curr_state_path = frontier[i][1:]                   #stores the intermidiate configuration to the current node
        frontier = frontier[:i] + frontier[i+1:]            #removes the current node from frontier


        if goal_test(cur_node.state.tiles):                 #executes if our current node is the goal
            print('Solution:')
            path = find_path(cur_node)
            end_time = time.time()
            return path, count, (end_time-start_time)

        if cur_node in explored:
            continue

        for child in get_children(cur_node):
            if child in explored:
                continue
            else:
                x = manhattanDist(child.state.tiles)         #To use the misplaced tile heuristic use tiles_misplaced(child.state.tiles) here
                y = manhattanDist(cur_node.state.tiles)      #To use the misplaced tile heuristic use tiles_misplaced(cur_node.state.tiles) here
                newpath = [curr_path_heur + x - y] + curr_state_path + [child]
                frontier.append(newpath)
                explored.append(cur_node)
        count += 1
    print("frontier empty")
    return False

def main():                                                     #This is the main or the driver function.
    process = psutil.Process(os.getpid())
    initial_memory = process.memory_info().rss / 1024.0         #This calculates the inititial memnory consumption
    initial = input("Enter input sequence: ")                   #This statement asks for n input from the user
    board = initial.split()                                     #This splits the input into a list of characters on the basis of space
    root = Node(Board(board), None, None)
    print(run_astar(root))
    final_memory = process.memory_info().rss / 1024.0           #This calculates the memory used by our code
    print(str(final_memory-initial_memory)+" KB")


def goal_test(cur_tiles):                                       #This function performs the goal test.
    return cur_tiles == ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '0']


if __name__ == '__main__':
    main()
