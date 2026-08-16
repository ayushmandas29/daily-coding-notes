# Data Structures — Research Notes

## Foundations
Data structures organize data to support operations such as search, insertion, deletion, update, traversal, and aggregation. The right structure depends on workload, memory model, ordering requirements, and complexity targets.

## Linear structures
- Array: O(1) indexed access; contiguous storage.
- Linked list: O(1) insertion/deletion after a known node, but poor random access.
- Stack: LIFO.
- Queue: FIFO.
- Deque: insertion/removal at both ends.

## Hash tables
Expected O(1) lookup under appropriate hashing/load assumptions. Collision strategies include chaining and open addressing. Worst-case behavior depends on implementation and adversarial inputs.

## Trees
- Binary search tree: ordered search structure.
- AVL / Red-Black trees: balanced search trees with logarithmic-height guarantees.
- Heap: supports priority-queue operations.
- B-tree/B+ tree: optimized for external storage and database/index workloads.

## Graphs
Represent graphs using adjacency lists or matrices. Choice depends on density and operation patterns.

## Advanced structures
- Trie: prefix queries.
- Union-Find/Disjoint Set Union: connectivity and Kruskal-style algorithms.
- Segment tree: range queries/updates.
- Fenwick tree: prefix/range aggregation with compact structure.

## Books
- *Introduction to Algorithms* — MIT Press: https://mitpress.mit.edu/9780262046305/introduction-to-algorithms/
- *Algorithms* — Princeton: https://algs4.cs.princeton.edu/home/
- *The Algorithm Design Manual*: https://www.algorist.com/

## Research papers
- Adelson-Velsky & Landis, “An Algorithm for the Organization of Information”: https://doi.org/10.1145/384044.384047
- Bayer & McCreight, “Organization and Maintenance of Large Ordered Indexes”: https://doi.org/10.1145/173466.173467
- Tarjan, “Efficiency of a Good But Not Linear Set Union Algorithm”: https://doi.org/10.1145/321879.321884

## Research checklist
For each structure document invariants, amortized/worst-case complexity, memory layout, cache behavior, concurrency implications, and workload suitability.