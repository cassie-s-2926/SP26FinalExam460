# The Torchbearer

**Student Name:** Cassie
**Student ID:** Scott
**Course:** CS 460 – Algorithms | Spring 2026

> This README is your project documentation. Write it the way a developer would document
> their design decisions , bullet points, brief justifications, and concrete examples where
> required. You are not writing an essay. You are explaining what you built and why you built
> it that way. Delete all blockquotes like this one before submitting.

---

## Part 1: Problem Analysis

> Document why this problem is not just a shortest-path problem. Three bullet points, one
> per question. Each bullet should be 1-2 sentences max.

- **Why a single shortest-path run from S is not enough:**
  _A single shorest path run from S is not enough because a set of chambers, M, must be
  visited before visiting final node T. A shortest path is not guarantee to visit every
  required location._

- **What decision remains after all inter-location costs are known:**
  _After all inter locations costs are known we must choose the next chamber to visit._

- **Why this requires a search over orders (one sentence):**
  _The immediate next best chamber to visit may not be the overall best choice for
  minimum fuel cost._

---

## Part 2: Precomputation Design

### Part 2a: Source Selection

| Source Node Type | Why it is a source |
|---|---|
| _spawn_| The path will always visit the start node |
| _relics_ | Nodes with relics must be visited |
| _exist_node_ | The path will always end at the exit node |

### Part 2b: Distance Storage

> Fill in the table. No prose required.

| Property | Your answer |
|---|---|
| Data structure name | Dictionary |
| What the keys represent | Nodes in graph |
| What the values represent | Shortest path from source node to  |
| Lookup time complexity | O(1) |
| Why O(1) lookup is possible | A dictionary looks up by key by hash table |

### Part 2c: Precomputation Complexity

> State the total complexity and show the arithmetic. Two to three lines max.

- **Number of Dijkstra runs:** _Number of source nodes_
- **Cost per run:** _O(ElogV)_
- **Total complexity:** _O(E^2logV)_
- **Justification (one line):** _Dijkstra runs once for each source node up to E,
-   it runs for time O(ElogV) for V vertices and E nodes each time it runs._

---

## Part 3: Algorithm Correctness

> Document your understanding of why Dijkstra produces correct distances.
> Bullet points and short sentences throughout. No paragraphs.

### Part 3a: What the Invariant Means

> Two bullets: one for finalized nodes, one for non-finalized nodes.
> Do not copy the invariant text from the spec.

- **For nodes already finalized (in S):**
  _Finalized node have shortest path from some source node to all other nodes in graph._

- **For nodes not yet finalized (not in S):**
  _Nodes not yet finalized have some shortest path which is within finalized set._

### Part 3b: Why Each Phase Holds

> One to two bullets per phase. Maintenance must mention nonnegative edge weights.

- **Initialization : why the invariant holds before iteration 1:**
  _The set S for some source node is empty, except to itself which is 0, so all nodes in S, None, fail the invariant._

- **Maintenance : why finalizing the min-dist node is always correct:**
  _if current dist is not best, it is ignored and no better distance is set, if not, if current dist and some edge distance to the node is a better option, it is the best option of the known set each step._

- **Termination : what the invariant guarantees when the algorithm ends:**
  _The invariant guarantees, each node explored gets a better option for a node if available until all nodes are set, meaning all nodes are set for shortest path._

### Part 3c: Why This Matters for the Route Planner

> One sentence connecting correct distances to correct routing decisions.

_The route needs the best cost for visiting every node in the set, therefore the correct best path for any connection between important nodes means a best route for visiting the nodes in set._

---

## Part 4: Search Design

### Why Greedy Fails

> State the failure mode. Then give a concrete counter-example using specific node names
> or costs (you may use the illustration example from the spec). Three to five bullets.

- **The failure mode:** _Best path fails all required visits._
- **Counter-example setup:** _start = A [A, B, C, D] exit = D relics = B, C._
- **What greedy picks:** _[A, B, D]._
- **What optimal picks:** _[A, B, C, D]._
- **Why greedy loses:** _C with some relic._

### What the Algorithm Must Explore

> One bullet. Must use the word "order."

- _The algorithm must explore each possible path in order of best distance._

---

## Part 5: State and Search Space

### Part 5a: State Representation

> Document the three components of your search state as a table.
> Variable names here must match exactly what you use in torchbearer.py.

| Component | Variable name in code | Data type | Description |
|---|---|---|---|
| Current location | Current_loc | node | Holds currnt location being explored |
| Relics already collected | relics_visited_order | list | ordered set of relics visited |
| Fuel cost so far | cost_so_far | int | current cost computed for path|

### Part 5b: Data Structure for Visited Relics

> Fill in the table.

| Property | Your answer |
|---|---|
| Data structure chosen | list |
| Operation: check if relic already collected | Time complexity: O(1) |
| Operation: mark a relic as collected | Time complexity: O(1)|
| Operation: unmark a relic (backtrack) | Time complexity: O(1) |
| Why this structure fits | Mutable, includes pop function |

### Part 5c: Worst-Case Search Space

> Two bullets.

- **Worst-case number of orders considered:** _Check every possible path is explored for some k number of nodes for total k^2._
- **Why:** _If no prunes occur, every node and possible neighbor nodes up to all other nodes in graph is k^2._

---

## Part 6: Pruning

### Part 6a: Best-So-Far Tracking

> Three bullets.

- **What is tracked:** _Cost so far in branch._
- **When it is used:** _Comparing to saved best cost path._
- **What it allows the algorithm to skip:** _If cost so far is already over, or equal to, any further paths in branch cant be less than current._

### Part 6b: Lower Bound Estimation

> Three bullets.

- **What information is available at the current state:** _The best path over all branches explored._
- **What the lower bound accounts for:** _Lower bound accounts for branches leading to always worse overall solutions._
- **Why it never overestimates:** _If current path is already at or more than the best, any choice will always result in a worst solution. Any branch with possible better solution is considered for all branches, leading to best overall._

### Part 6c: Pruning Correctness

> One to two bullets. Explain why pruning is safe.

- _Any path in branch pruned cant be a solution better than current best._

---

## References

> Bullet list. If none beyond lecture notes, write that.

- _ N/A _
