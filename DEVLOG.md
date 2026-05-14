# Development Log – The Torchbearer

**Student Name:** Cassie Scott
**Student ID:** 134075705

> Instructions: Write at least four dated entries. Required entry types are marked below.
> Two to five sentences per entry is sufficient. Write entries as you go, not all in one
> sitting. Graders check that entries reflect genuine work across multiple sessions.
> Delete all blockquotes before submitting.

---

## Entry 1 – [5/13/26 03:20]: Initial Plan

_In part two it creates the set of important nodes we must visit once, from starting node 
	S to eventually ending node T. It defines dijkstra which computes the lowest cost path
	from a source node to all known node. Finally it computes a nested set of all 
	important nodes shortest paths to all other nodes using dijkstras on each source node. 
	This part will required understanding djikstra, should be fairly easy.
	In part 5 and 6. The best optimal path will set up a best cost and its path order of 
	chambers visited. Then, explore will run over the important nodes and shortest paths
	between them to find the best cost permutations, visiting each important node once and
	ending on the exit node. It will prune a subtree in a running path if current cost is over
	the stored best path cost, since it cannot be a better path, and update when a new best
	cost permutations is found.
	Soving the recurrsion function for explore function I expect will be the most difficult
	part. It will use a DFS, finding each permutation of paths, before backtracking. First,
	check base case, all important nodes explored. Update if path cost is less than stored
	best and backtrack. If not, if path cost is more than best stored stop exploring, prunning
	this subtree and backtrack. Else, it will find a next node to explore, add its cost, and
	explore this node, recurring. 
	The Pipeline then takes the directed graph, computes shortest distances between important
	nodes from part 2, then finds optimal path based on graph given from part 5 and 6, and
	finally returning the solution, best cost path to all chamber nodes from start node S to
	exit node T. If no solution is found return (float('inf') [])
	P.S: a copy of torchbearer.py will be used for testing before updating
	main file._

---

## Entry 2 – [5/13/26 07:16]: Part 1 and 2 implementation, part 2 minor bug, update to entry 1

> Required. At least one entry must describe a bug, wrong assumption, or design change
> you encountered. Describe what went wrong and how you resolved it.

_Implemented part 1 explaintion. Implemented Part 2 - select_sources run dijkstra and
	precompute distances functions. Initally the best path set returned from dijkstra was not
	returning in my tests. I checked the code finding that I was attempting to return the priority
	queue, which is empty. I then fixed it to return the distance set
	Also update to intal entry for testing._

---

## Entry 3 – [5/14/26 01:10]: [Part 5 and 6 implementation, part 6 bugs]

_Implemented part 5 and 6 find optimal route and explore functions. Worked on both simutniously
	since they rely on each other. After testing it first had a bug due to a change from best
	holding a single integer to list. This was fixed and was able to run. A second major bug,
	a test case was failing to compute and returned a infinity solution (no solution). After
	looking over, I was still unsure, so I used a chat bot to identify why the test was returning
	a failed solution. 1. the best was accidently made as a tuple, therfore immutable; 2. The
	prune comparasion was inverted; 3. Input current node instead of next node into recurrsion.
	These were then fixed, I also made some minor changes to how objects were created and updated
	during the recurrsion base. The test passed after these fixes. P.S. Pushed after entry by mistake._

---

## Entry 4 – [5/13/26 02:58]: Upload torchbearer.py fix

_Implementations from entry 3 was not updated into main torchbearer.py from torchebear_testing.py
	and pushed to github. Updated main file and push to github. Corresponding update to last entry._

---

## Entry 5 – [5/13/26 04:13]: Pipeline implementations, run tests ran

_Implementations of pipeline for full program implementations. tested using created data and provided
	case test. All test but 5 passed. Errors printed, so bug fixes might be required. Errors include
	empty strings, so those will be implemented last and if errors still persist, fix will be
	required. Minor change in explore function._

---

## Entry 6 – [Date]: Post-Implementation Reflection

> Required. Written after your implementation is complete. Describe what you would
> change or improve given more time.

_Your entry here._

---

## Final Entry – [Date]: Time Estimate

> Required. Estimate minutes spent per part. Honesty is expected; accuracy is not graded.

| Part | Estimated Hours |
|---|---|
| Part 1: Problem Analysis | |
| Part 2: Precomputation Design | |
| Part 3: Algorithm Correctness | |
| Part 4: Search Design | |
| Part 5: State and Search Space | |
| Part 6: Pruning | |
| Part 7: Implementation | |
| README and DEVLOG writing | |
| **Total** | |
