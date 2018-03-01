# 8-tile Puzzle
Intelligent Systems First Project, using A* search algorithm. Python implementation

Constanza Liévanos A01361506
Cesar Guadarrama cantu A01364853
Allan Julian A01361651
28/02/18

Problem description in [http://www.d.umn.edu/~jrichar4/8puz.html](http://www.d.umn.edu/~jrichar4/8puz.html)

## Description
### A* Algorithm
  1. Create the search graph G = {S0}. Also put S0 in an ordered list called OPEN.
  2. Create a list called CLOSED an set it to NIL.
  3. if OPEN = NIL then exit indicating failure
  4. Let Si = Remove(Head(OPEN)), add Si to CLOSED.
  5. If Si is the goal node, exit with the solution being the patch backward along
  the arc of G from Si to S0.
  6. Expand Si generating M successors that are not already ancestors of Si in G.
  Add successors M to G creating arcs from Si to each member of M.
  7. Establish a pointer to Si from each of those members of M that were not
  already in G (i.e., not already on either OPEN or CLOSED). Add these
  members of M to OPEN. For each member, m, of M that was already on OPEN
  or CLOSED, redirect its pointer to Si if the best path to m found so far is
  through Si. For each member of M already on CLOSED, redirect the pointers
  of each of its descendants in G so that they point backward along the best
  paths found so far to these descendants.
  8. Reorder the list OPEN in order of increasing values of (ties are resolved in
  favor of the deepest node in the search tree).
  9. Goto step 3.

  f(n)=g(n)+h(n)

### Manhattan distance
For the project we used the Manhattan priority function: The sum of the Manhattan distances (sum of the vertical and horizontal distance) from the blocks to their goal positions, plus the number of moves made so far to get to the search node.

For example, if x=(a,b)x=(a,b) and y=(c,d)y=(c,d), the Manhattan distance between xx and yy is:
  |a−c|+|b−d|

## Results 
After implementing the algorithm we saw that if we tried really hard to mix the numbers the program took a lot of time to find the answer. In some cases, we even stopped the programm because it took too long, specially if we tried to print each iteration.

## Conclusions
The time complexity depends on the heuristic function and is found to be exponential O(bd)O(bd) where b is the branching factor and d is the distance from source to destination.
## Division of labour

The way we divided the project was basically into two. Allan's task was to do the function of the Manhattan distance as well as the possible combinatios the puzzle had to do for each iteration.
The other part was Cesar and Constanza, the task was to implement the A* algorithm itself and put Allan's part together.
