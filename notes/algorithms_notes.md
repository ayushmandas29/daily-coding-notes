# Algorithms — Research Notes

## Core ideas
An algorithm is a finite, well-defined procedure for transforming input into output. Research-level analysis asks about correctness, asymptotic complexity, space usage, stability, approximation quality, and practical constants.

## Complexity
- Big-O: asymptotic upper bound.
- Big-Theta: tight asymptotic bound.
- Big-Omega: asymptotic lower bound.

Analyze best, average, and worst cases when meaningful. Amortized analysis studies the average cost over a sequence of operations.

## Major paradigms
- Divide and conquer: merge sort, quicksort.
- Greedy: interval scheduling, minimum spanning tree algorithms.
- Dynamic programming: overlapping subproblems + optimal substructure.
- Graph algorithms: BFS, DFS, shortest paths, spanning trees.
- Randomized algorithms: random choices improve expected behavior or simplify algorithms.

## Correctness
Use invariants, induction, exchange arguments, contradiction, and loop invariants to prove algorithms correct.

## Trusted books
- *Introduction to Algorithms* — Cormen, Leiserson, Rivest, Stein: https://mitpress.mit.edu/9780262046305/introduction-to-algorithms/
- *The Algorithm Design Manual* — Skiena: https://www.algorist.com/
- *Algorithms* — Sedgewick & Wayne: https://algs4.cs.princeton.edu/home/

## Research papers
- Dijkstra, “A Note on Two Problems in Connexion with Graphs”: https://doi.org/10.1007/BF01386390
- Bellman, “On a Routing Problem”: https://doi.org/10.1007/BF01588925
- Floyd, “Algorithm 97: Shortest Path”: https://doi.org/10.1145/367766.368168
- Karger, Stein, “A New Approach to the Minimum Cut Problem”: https://doi.org/10.1145/263867.263872

## Practice rule
For every algorithm record: problem → intuition → pseudocode → proof idea → complexity → edge cases → implementation → benchmark → source.