# Databases — Research Notes

## Foundations
A database system provides durable storage plus mechanisms for querying, concurrency, recovery, security, and integrity.

## Relational model
Relations contain tuples and attributes. SQL provides declarative querying over relational data.

Core concepts:
- primary/foreign keys
- candidate keys
- constraints
- normalization
- transactions
- indexes

## Normalization
1NF removes repeating groups; higher normal forms reduce problematic dependencies and redundancy. Denormalization can be justified for performance when consistency and update costs are controlled.

## Transactions and ACID
- Atomicity: all-or-nothing transaction behavior.
- Consistency: preserves declared/system integrity constraints.
- Isolation: concurrent transactions behave according to selected isolation semantics.
- Durability: committed changes survive specified failures.

## Concurrency
Isolation levels trade consistency guarantees against concurrency. Common phenomena include dirty reads, non-repeatable reads, and phantom reads.

## Indexing
B-tree/B+ tree indexes support ordered access and range queries. Hash indexes can be useful for equality lookups. Indexes accelerate reads but consume storage and make writes more expensive.

## Query optimization
A database optimizer chooses an execution plan using statistics, cost estimates, indexes, join strategies, and cardinality estimates. Inspect execution plans when investigating performance.

## Distributed databases
Important concepts include replication, partitioning/sharding, consistency models, quorum techniques, consensus, and failure handling.

## Books
- *Database System Concepts* — Silberschatz, Korth, Sudarshan: https://www.db-book.com/
- *Database Internals* — Alex Petrov: https://www.oreilly.com/library/view/database-internals/9781492040330/
- *Designing Data-Intensive Applications* — Martin Kleppmann: https://dataintensive.net/

## Research papers
- Codd, “A Relational Model of Data for Large Shared Data Banks”: https://doi.org/10.1145/362384.362685
- Gray, “The Transaction Concept: Virtues and Limitations”: https://doi.org/10.1145/358396.358400
- DeCandia et al., “Dynamo: Amazon’s Highly Available Key-value Store”: https://www.allthingsdistributed.com/files/amazon-dynamo-sosp2007.pdf
- Corbett et al., “Spanner: Google’s Globally-Distributed Database”: https://research.google/pubs/pub39966/

## Research checklist
For database experiments record workload, schema, indexes, isolation level, hardware, dataset size, query plans, latency percentiles, throughput, and failure assumptions.