def puzzle15_dls(seq, depth):
    #invoke the recursive depth limited search with initial set of moves as an empty list
    return puzzle15_recursive_dls(seq, depth, [])

def puzzle15_recursive_dls(current_node, limit, moves):
    global nodes_expanded
    global start_time
    time_elapsed = time.time() - start_time
    if time_elapsed > max_exec_time:
            #maximum execution time exhausted
            return "timeout"
    if is_soln(current_node):
        #initial state is solution. Print the solution and return.
        print_soln(moves, time.time())
        return "success"
    elif limit == 0:
        return "cutoff"
    else:
        nodes_expanded += 1
        cutoff_occurred = False
        action_state_pairs = get_actions(current_node)
        #iterate all actions and the resultant search states and check for solution state
        for action_state in action_state_pairs:
            new_state = action_state[1]
            temp_moves = moves.copy()
            temp_moves.append(action_state[0])
            #invoke the recursive call to perform dls on the child node
            status = puzzle15_recursive_dls(new_state, limit-1, temp_moves)
            if status == "cutoff":
                cutoff_occurred = True
            elif status != "failure":
                return status
        if cutoff_occurred == True:
            return status
        else:
            return "failure"

def puzzle15_iddfs(seq):
    depth = 0
    #invoke the depth limited search with incremental depths
    while True:
        status = puzzle15_dls(seq, depth)
        if status == "success":
            return
        elif status == "failure":
            print("No solution exists.")
            return
        elif status == "timeout":
            print("Solution cannot be found since the maximum execution time has been exceeded.")
            return
        depth += 1
    return
