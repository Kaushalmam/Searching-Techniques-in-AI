from board import Node
class State:
    # this is the class that will store the details regarding state
    def __init__(self, initial_state=[]):#this is a custructor that will initialize current to current state.
        self.current = Node(initial_state)
    def __eq__(self, diff):    #this will test two State type variables for equality.
        return self.current == diff.current
    def __str__(self):          #this will print the current state.
        return str(self.current)
    def __hash__(self):         #this will return a key for the current state.
        return hash(str(self))

    def up(self):             # this function will run the up operation on current state and store it as another state.
        i = self.current.move_up()
        if i is None:
            return self
        else:
            return State(i)
        
    def down(self):           # this function will run the down operation on current state and store it as another state.
        i = self.current.move_down()
        if i is None:
            return self
        else:
            return State(i)

    def left(self):           # this function will run the left operation on current state and store it as another state.
        i = self.current.move_left()
        if i is None:
            return self
        else:
            return State(i)

    def right(self):          # this function will run the right operation on current state and store it as another state.
        i = self.current.move_right()
        if i is None:
            return self
        else:
           return State(i) 
        
#The following snippit is used to find the successors or of the current state
    def successors(self):
        suc = []
        up = self.current.move_up()
        if up != None:
            suc.append(State(up))
        down = self.current.move_down()
        
        if down != None:
            suc.append(State(down))
        left = self.current.move_left()

        if left != None:
            suc.append(State(left))
        right = self.current.move_right()

        if right != None:
            suc.append(State(right))

        return suc
