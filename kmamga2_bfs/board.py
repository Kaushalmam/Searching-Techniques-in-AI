class Node:
    # this is the class that will store the details regarding puzzle
    def __init__(self, initial_values=[]): #this is a custructor that will initialize value to puzzle.
        self.value = initial_values

    def __eq__(self, diff):                #this will test two Board type variables for equality.
        return self.value == diff.value

    def __str__(self):                      #this will print the puzzle.
        return str(self.value)
    
    def __hash__(self):                     #this will return a key for the current state of the board.
        return hash(str(self))

    
    def move_up(self):
        pos = self.value.index(0)
        if pos not in (0,1,2,3):        #if zero exists here then we cant movue it any further up.
            return None
        else:
            new_val = list(self.value)
            t=new_val[pos]
            new_val[pos]=new_val[pos-4]
            new_val[pos-4]=t
            return new_val

    def move_down(self):                 #if zero exists here then we cant movue it any further down.
        pos = self.value.index(0)
        if pos in (12,13,14,15):
            return None
        else:
            new_val = list(self.value)
            t=new_val[pos]
            new_val[pos]=new_val[pos+4]
            new_val[pos+4]=t
            return new_val

    def move_left(self):                 #if zero exists here then we cant movue it any further left.
        pos = self.value.index(0)
        if pos in (0,4,8,12):
            return None
        else:
            new_val = list(self.value)
            t=new_val[pos]
            new_val[pos]=new_val[pos-1]
            new_val[pos-1]=t
            return new_val
        
    def move_right(self):                #if zero exists here then we cant movue it any further right.
        pos = self.value.index(0)
        if pos in (3,7,11,15):
            return None
        else:
            new_val = list(self.value)
            t=new_val[pos]
            new_val[pos]=new_val[pos+1]
            new_val[pos+1]=t
            return new_val
