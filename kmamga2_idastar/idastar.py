import random
import math
import time
import psutil
import os

 
class IDAStar:
    def __init__(self, h, neighbours):
        #Constructoe to initialize IDAStar variable
 
        self.h = h
        self.neighbours = neighbours
        self.FOUND = object()
 
 
    def solve(self, root, is_goal, max_cost=None): #function returns the shortest path between Current and goal node
    
 
        self.is_goal = is_goal
        self.path = [root]
        self.is_in_path = {root}
        self.path_descrs = []
        self.nodes_evaluated = 0
 
        bound = self.h(root)
 
        while True:
            t = self._search(0, bound)
            if t is self.FOUND: return self.path, self.path_descrs, bound, self.nodes_evaluated
            if t is None: return None
            bound = t
 
    def _search(self, g, bound): #function to search for goal
        self.nodes_evaluated += 1
 
        node = self.path[-1]
        f = g + self.h(node)
        if f > bound: return f
        if self.is_goal(node): return self.FOUND
 
        m = None # Lower bound on cost.
        for cost, n, descr in self.neighbours(node):
            self.nodes_evaluated += 1
            if n in self.is_in_path: continue
 
            self.path.append(n)
            self.is_in_path.add(n)
            self.path_descrs.append(descr)
            t = self._search(g + cost, bound)
 
            if t == self.FOUND: return self.FOUND
            if m is None or (t is not None and t < m): m = t
 
            self.path.pop()
            self.path_descrs.pop()
            self.is_in_path.remove(n)
 
        return m
 
 
def slide_solved_state(n):
    return tuple(i % (n*n) for i in range(1, n*n+1))
 
def slide_randomize(p, neighbours):
    for _ in range(len(p) ** 2):
        self.nodes_evaluated += 1
        _, p, _ = random.choice(list(neighbours(p)))
    return p
 
def slide_neighbours(n): #function to calculate Childern
    movelist = []
    for gap in range(n*n):
        x, y = gap % n, gap // n
        moves = []
        if x > 0: moves.append(-1)    # Move the blank tile left.
        if x < n-1: moves.append(+1)  # Move the blank tile right.
        if y > 0: moves.append(-n)    # Move the blank tile up.
        if y < n-1: moves.append(+n)  # Move the blank tile down.
        movelist.append(moves)
 
    def neighbours(p): #Function to calculate childern
        gap = p.index(0)
        l = list(p)
 
        for m in movelist[gap]:
            l[gap] = l[gap + m]
            l[gap + m] = 0
            yield (1, tuple(l), (l[gap], m))
            l[gap + m] = l[gap]
            l[gap] = 0
 
    return neighbours
 
def encode_cfg(cfg, n): #To encode the input
    r = 0
    b = n.bit_length()
    for i in range(len(cfg)):
        r |= cfg[i] << (b*i)
    return r
 
 
def gen_wd_table(n):# function to calculate manhattan distance
    goal = [[0] * i + [n] + [0] * (n - 1 - i) for i in range(n)]
    goal[-1][-1] = n - 1
    goal = tuple(sum(goal, []))
 
    table = {}
    to_visit = [(goal, 0, n-1)]
    while to_visit:
        cfg, cost, e = to_visit.pop(0)
        enccfg = encode_cfg(cfg, n)
        if enccfg in table: continue
        table[enccfg] = cost
 
        for d in [-1, 1]:
            if 0 <= e + d < n:
                for c in range(n):
                    if cfg[n*(e+d) + c] > 0:
                        ncfg = list(cfg)
                        ncfg[n*(e+d) + c] -= 1
                        ncfg[n*e + c] += 1
                        to_visit.append((tuple(ncfg), cost + 1, e+d))
 
    return table
 
def slide_wd(n, goal):
    wd = gen_wd_table(n)
    goals = {i : goal.index(i) for i in goal}
    b = n.bit_length()
    def h(p):
        ht = 0 # Walking distance between rows.
        vt = 0 # Walking distance between columns.
        d = 0
        for i, c in enumerate(p):
            if c == 0: continue
            g = goals[c]
            xi, yi = i % n, i // n
            xg, yg = g % n, g // n
            ht += 1 << (b*(n*yi+yg))
            vt += 1 << (b*(n*xi+xg))
 
            if yg == yi:
                for k in range(i + 1, i - i%n + n): # Until end of row.
                    if p[k] and goals[p[k]] // n == yi and goals[p[k]] < g:
                        d += 2
 
            if xg == xi:
                for k in range(i + n, n * n, n): # Until end of column.
                    if p[k] and goals[p[k]] % n == xi and goals[p[k]] < g:
                        d += 2
 
        d += wd[ht] + wd[vt]
 
        return d
    return h
 
 
 
 
if __name__ == "__main__": #main function or driver fuction
    solved_state = slide_solved_state(4)
    neighbours = slide_neighbours(4)
    process = psutil.Process(os.getpid())
    initial_memory = process.memory_info().rss / 1024.0
    initial_time = time.time()
    is_goal = lambda p: p == solved_state
    #Enter the test cases to as input
    tests = [
        (5,2,4,8,10,3,11,14,6,0,9,12,13,1,15,7),
        (5,2,4,8,10,0,3,14,13,6,11,12,1,15,9,7)
    ]
 
    slide_solver = IDAStar(slide_wd(4, solved_state), neighbours)
 
    for p in tests:
        path, moves, cost, num_eval = slide_solver.solve(p, is_goal, 80)
        #slide_print(p)
        print(", ".join({-1: "L", 1: "R", -4: "U", 4: "D"}[move[1]] for move in moves))
        print("Nodes Expanded "+ str(num_eval))
    final_memory = process.memory_info().rss / 1024.0
    final_time = time.time()
    print("Memory Used "+str(final_memory-initial_memory)+" KB")
    print("time taken: "+str(final_time-initial_time))
