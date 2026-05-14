"""
CS 460 – Algorithms: Final Programming Assignment
The Torchbearer

Student Name: Cassie Scott
Student ID:   134075705

INSTRUCTIONS
------------
- Implement every function marked TODO.
- Do not change any function signature.
- Do not remove or rename required functions.
- You may add helper functions.
- Variable names in your code must match what you define in README Part 5a.
- The pruning safety comment inside _explore() is graded. Do not skip it.

Submit this file as: torchbearer.py
"""

import heapq


# =============================================================================
# PART 1
# =============================================================================

def explain_problem():
    
    return """A single shorest path run from S is not enough because a set of\n
    chambers, M, must be visited before visiting final node T. A shortest\n
    path is not guarantee to visit every required location.\n\n
    After all inter locations costs are known we must choose the next chamber\n
    to visit.\n\n
    The immediate next best chamber to visit may not be the overall best\n
    choice for minimum fuel cost"""


# =============================================================================
# PART 2
# =============================================================================

def select_sources(spawn, relics, exit_node):

    sources = [spawn]
    for relic in relics:
        sources.append(relic)
    sources.append(exit_node)

    return sources


def run_dijkstra(graph, source):

    dist = {node: float('inf') for node in graph}
    dist[source] = 0

    nodeQueue = []
    heapq.heappush(nodeQueue, (0, source))

    while nodeQueue:
        currentDist, currentNode = heapq.heappop(nodeQueue)

        if currentDist > dist[currentNode]:
            continue

        # explore all adjacent nodes, updating when a shorter path is found
        for adjacent, edgeDist in graph[currentNode]:
            if currentDist + edgeDist < dist[adjacent]:
                dist[adjacent] = currentDist + edgeDist
                heapq.heappush(nodeQueue, (dist[adjacent], adjacent))

    return dist


def precompute_distances(graph, spawn, relics, exit_node):

    sources = select_sources(spawn, relics, exit_node)
    dist_table = {}

    # Run Dijkstras for each source node and add to dist_table for lookup
    for source in sources:
        dist_table[source] = run_dijkstra(graph, source)

    return dist_table


# =============================================================================
# PART 3
# =============================================================================

def dijkstra_invariant_check():
    """
    Returns
    -------
    str
        Your Part 3 README answers, written as a string.
        Must match what you wrote in README Part 3.

    TODO
    """
    return "TODO"


# =============================================================================
# PART 4
# =============================================================================

def explain_search():
    """
    Returns
    -------
    str
        Your Part 4 README answers, written as a string.
        Must match what you wrote in README Part 4.

    TODO
    """
    return "TODO"


# =============================================================================
# PARTS 5 + 6
# =============================================================================

def find_optimal_route(dist_table, spawn, relics, exit_node):

    current_loc = spawn
    relics_remaining = set(relics)
    relics_visited_order = []
    cost_so_far = dist_table[current_loc][current_loc]
    best = [float('inf'), []]

    # explore all permutations
    _explore(dist_table, current_loc, relics_remaining, relics_visited_order, cost_so_far, exit_node, best)

    # return best path found
    return best


def _explore(dist_table, current_loc, relics_remaining, relics_visited_order,
             cost_so_far, exit_node, best):

    # prune if current branch worse than current best
    if cost_so_far >= best[0]:
        return

    # base case: all relics explored
    if not relics_remaining:

        # end if impossible to reach exit
        if dist_table[current_loc][exit_node] == float('inf'):
            return

        total_cost = cost_so_far + dist_table[current_loc][exit_node]

        # if new best cost found, update best
        if total_cost < best[0]:
            best[0] = total_cost
            best[1] = relics_visited_order.copy()

        return

    # recur for next relic chosen
    for relic in relics_remaining:

        # end if impossible to reach relic
        if dist_table[current_loc][relic] == float('inf'):
            continue

        # visit
        relics_visited_order.append(relic)
        new_relics_remaining = relics_remaining - {relic}
        new_cost_so_far = cost_so_far + dist_table[current_loc][relic]

        # recur to next node
        _explore(dist_table, relic, new_relics_remaining, relics_visited_order,
                 new_cost_so_far, exit_node, best)

        # backtrack
        relics_visited_order.pop()


# =============================================================================
# PIPELINE
# =============================================================================

def solve(graph, spawn, relics, exit_node):
    """
    Parameters
    ----------
    graph : dict[node, list[tuple[node, int]]]
    spawn : node
    relics : list[node]
    exit_node : node

    Returns
    -------
    tuple[float, list[node]]
        (minimum_fuel_cost, ordered_relic_list)
        Returns (float('inf'), []) if no valid route exists.

    TODO
    """
    pass


# =============================================================================
# PROVIDED TESTS (do not modify)
# Graders will run additional tests beyond these.
# =============================================================================

def _run_tests():
    print("Running provided tests...")

    # Test 1: Spec illustration. Optimal cost = 4.
    graph_1 = {
        'S': [('B', 1), ('C', 2), ('D', 2)],
        'B': [('D', 1), ('T', 1)],
        'C': [('B', 1), ('T', 1)],
        'D': [('B', 1), ('C', 1)],
        'T': []
    }
    cost, order = solve(graph_1, 'S', ['B', 'C', 'D'], 'T')
    assert cost == 4, f"Test 1 FAILED: expected 4, got {cost}"
    print(f"  Test 1 passed  cost={cost}  order={order}")

    # Test 2: Single relic. Optimal cost = 5.
    graph_2 = {
        'S': [('R', 3)],
        'R': [('T', 2)],
        'T': []
    }
    cost, order = solve(graph_2, 'S', ['R'], 'T')
    assert cost == 5, f"Test 2 FAILED: expected 5, got {cost}"
    print(f"  Test 2 passed  cost={cost}  order={order}")

    # Test 3: No valid path to exit. Must return (inf, []).
    graph_3 = {
        'S': [('R', 1)],
        'R': [],
        'T': []
    }
    cost, order = solve(graph_3, 'S', ['R'], 'T')
    assert cost == float('inf'), f"Test 3 FAILED: expected inf, got {cost}"
    print(f"  Test 3 passed  cost={cost}")

    # Test 4: Relics reachable only through intermediate rooms.
    # Optimal cost = 6.
    graph_4 = {
        'S': [('X', 1)],
        'X': [('R1', 2), ('R2', 5)],
        'R1': [('Y', 1)],
        'Y': [('R2', 1)],
        'R2': [('T', 1)],
        'T': []
    }
    cost, order = solve(graph_4, 'S', ['R1', 'R2'], 'T')
    assert cost == 6, f"Test 4 FAILED: expected 6, got {cost}"
    print(f"  Test 4 passed  cost={cost}  order={order}")

    # Test 5: Explanation functions must return non-placeholder strings.
    for fn in [explain_problem, dijkstra_invariant_check, explain_search]:
        result = fn()
        assert isinstance(result, str) and result != "TODO" and len(result) > 20, \
            f"Test 5 FAILED: {fn.__name__} returned placeholder or empty string"
    print("  Test 5 passed  explanation functions are non-empty")

    print("\nAll provided tests passed.")


if __name__ == "__main__":
    _run_tests()
