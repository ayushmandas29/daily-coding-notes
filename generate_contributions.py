"""
GitHub Contribution Generator
Creates backdated commits spread across the past year
to fill the contribution graph with ~300 contributions.
"""

import os
import random
import subprocess
from datetime import datetime, timedelta


# Configuration
TOTAL_COMMITS = 1200
DAYS_BACK = 365
REPO_DIR = os.path.dirname(os.path.abspath(__file__))

# Coding tips and facts for commit content
TOPICS = [
    "algorithms", "data-structures", "system-design", "python",
    "javascript", "docker", "kubernetes", "machine-learning",
    "deep-learning", "sql", "git", "linux", "networking",
    "api-design", "testing", "security", "performance",
    "databases", "cloud", "devops", "ci-cd", "microservices",
    "design-patterns", "clean-code", "debugging", "optimization",
]

TIPS = {
    "algorithms": [
        "Binary search runs in O(log n) time complexity",
        "Dynamic programming solves overlapping subproblems efficiently",
        "BFS uses a queue while DFS uses a stack",
        "Merge sort guarantees O(n log n) in all cases",
        "Two pointer technique reduces nested loops to O(n)",
        "Sliding window is ideal for contiguous subarray problems",
        "Topological sort works only on DAGs",
        "Kadane's algorithm finds max subarray in O(n)",
    ],
    "data-structures": [
        "Hash maps provide O(1) average lookup time",
        "BSTs maintain sorted order with O(log n) operations",
        "Heaps are perfect for priority queue implementations",
        "Tries excel at prefix-based string searching",
        "Graphs can be represented as adjacency lists or matrices",
        "Stacks follow LIFO while queues follow FIFO",
        "Linked lists allow O(1) insertion at head",
        "Red-black trees guarantee O(log n) worst case",
    ],
    "system-design": [
        "CAP theorem: choose 2 of consistency, availability, partition tolerance",
        "Load balancers distribute traffic across servers",
        "Caching reduces database load and latency",
        "Database sharding enables horizontal scaling",
        "Message queues decouple system components",
        "CDNs serve static content closer to users",
        "Rate limiting protects APIs from abuse",
        "Circuit breakers prevent cascade failures",
    ],
    "python": [
        "List comprehensions are faster than manual loops",
        "Context managers handle resource cleanup automatically",
        "Generators yield values lazily to save memory",
        "Decorators add functionality without modifying functions",
        "f-strings are the fastest string formatting method",
        "dataclasses reduce boilerplate for data containers",
        "asyncio enables concurrent I/O operations",
        "Type hints improve code readability and IDE support",
    ],
    "javascript": [
        "Promises handle asynchronous operations cleanly",
        "Arrow functions inherit 'this' from their parent scope",
        "Destructuring simplifies object and array extraction",
        "Optional chaining prevents null reference errors",
        "Map and Set provide specialized data structures",
        "async/await makes promise chains more readable",
        "Spread operator creates shallow copies of arrays",
        "Template literals support multi-line strings",
    ],
    "docker": [
        "Multi-stage builds reduce final image size",
        "Docker layers are cached for faster rebuilds",
        "Use .dockerignore to exclude unnecessary files",
        "Run containers as non-root for security",
        "Docker Compose orchestrates multi-container apps",
        "Health checks ensure container readiness",
        "Volume mounts persist data beyond container lifecycle",
        "Alpine base images minimize attack surface",
    ],
    "kubernetes": [
        "Pods are the smallest deployable units in K8s",
        "Services provide stable networking for pods",
        "ConfigMaps externalize configuration from containers",
        "HPA scales pods based on resource utilization",
        "Namespaces isolate cluster resources",
        "Liveness probes restart unhealthy containers",
        "Readiness probes control traffic routing",
        "PodDisruptionBudgets ensure availability during updates",
    ],
    "machine-learning": [
        "Cross-validation prevents overfitting during evaluation",
        "Feature scaling improves gradient descent convergence",
        "Regularization prevents model overfitting",
        "Confusion matrices show classification performance",
        "ROC-AUC measures discriminative ability",
        "Ensemble methods combine multiple weak learners",
        "Bias-variance tradeoff is fundamental in ML",
        "Feature importance helps with model interpretability",
    ],
    "deep-learning": [
        "Batch normalization stabilizes training",
        "Dropout regularization prevents co-adaptation",
        "Learning rate scheduling improves convergence",
        "Skip connections solve vanishing gradient problem",
        "Attention mechanism captures long-range dependencies",
        "Transfer learning leverages pretrained knowledge",
        "Data augmentation increases effective dataset size",
        "Focal loss handles extreme class imbalance",
    ],
    "sql": [
        "Indexes speed up queries but slow down writes",
        "EXPLAIN ANALYZE reveals query execution plans",
        "CTEs improve readability of complex queries",
        "Window functions compute across related rows",
        "ACID properties ensure transaction reliability",
        "Normalization reduces data redundancy",
        "Prepared statements prevent SQL injection",
        "Partitioning improves performance on large tables",
    ],
    "git": [
        "Rebase creates a linear commit history",
        "Cherry-pick applies specific commits to branches",
        "Interactive rebase allows squashing commits",
        "Git bisect finds the commit that introduced a bug",
        "Stash saves uncommitted changes temporarily",
        "Tags mark important points in history",
        "Git hooks automate pre-commit checks",
        "Conventional commits improve changelog generation",
    ],
    "linux": [
        "grep searches text patterns across files",
        "awk processes columnar data efficiently",
        "sed performs stream text transformations",
        "cron schedules recurring tasks automatically",
        "chmod controls file access permissions",
        "top monitors real-time system processes",
        "pipe operator chains command outputs",
        "systemd manages services and daemons",
    ],
    "networking": [
        "TCP ensures reliable ordered data delivery",
        "DNS translates domain names to IP addresses",
        "HTTPS encrypts data in transit via TLS",
        "WebSockets enable full-duplex communication",
        "REST uses standard HTTP methods for APIs",
        "gRPC uses Protocol Buffers for efficient RPC",
        "IPv6 provides a much larger address space",
        "Load balancers can operate at L4 or L7",
    ],
    "api-design": [
        "REST APIs should use proper HTTP status codes",
        "Pagination prevents overwhelming API responses",
        "API versioning maintains backward compatibility",
        "Rate limiting protects API availability",
        "HATEOAS links make APIs self-documenting",
        "GraphQL lets clients request specific data",
        "OpenAPI spec documents REST APIs standardly",
        "Idempotent endpoints are safe for retries",
    ],
    "testing": [
        "Unit tests verify individual components",
        "Integration tests check component interactions",
        "Mocking isolates units from dependencies",
        "Code coverage measures tested code percentage",
        "TDD writes tests before implementation",
        "Property-based testing generates random inputs",
        "Snapshot testing catches unintended UI changes",
        "Load testing validates performance under stress",
    ],
    "security": [
        "OWASP Top 10 lists critical web vulnerabilities",
        "Input validation prevents injection attacks",
        "BCrypt hashes passwords securely with salt",
        "JWT tokens enable stateless authentication",
        "CORS policies restrict cross-origin requests",
        "CSP headers prevent cross-site scripting",
        "Secrets should never be committed to git",
        "Principle of least privilege limits access scope",
    ],
    "performance": [
        "Profiling identifies actual bottlenecks",
        "Caching reduces expensive computations",
        "Connection pooling reuses database connections",
        "Lazy loading defers resource loading until needed",
        "Compression reduces network payload size",
        "Async I/O prevents thread blocking",
        "Database indexing speeds up read queries",
        "CDNs reduce latency for static assets",
    ],
    "databases": [
        "OLTP handles transactional workloads",
        "OLAP handles analytical workloads",
        "Redis provides in-memory key-value storage",
        "MongoDB stores flexible JSON documents",
        "PostgreSQL supports advanced SQL features",
        "Connection pooling prevents exhaustion",
        "Replication provides read scalability",
        "Write-ahead logging ensures durability",
    ],
    "cloud": [
        "IaaS provides virtual infrastructure",
        "PaaS abstracts infrastructure management",
        "Serverless scales automatically to zero",
        "Cloud functions run event-driven code",
        "Object storage handles unstructured data",
        "VPCs isolate cloud network resources",
        "IAM controls access to cloud resources",
        "Auto-scaling adjusts capacity to demand",
    ],
    "devops": [
        "Infrastructure as Code ensures reproducibility",
        "GitOps uses git as single source of truth",
        "Blue-green deployments minimize downtime",
        "Canary releases reduce deployment risk",
        "Monitoring and alerting catch issues early",
        "Log aggregation centralizes troubleshooting",
        "Terraform manages multi-cloud infrastructure",
        "Ansible automates configuration management",
    ],
    "ci-cd": [
        "CI runs tests on every commit automatically",
        "CD deploys validated code to production",
        "Pipeline stages gate quality progressively",
        "Artifact caching speeds up build times",
        "Branch protection enforces review policies",
        "Automated rollbacks recover from bad deploys",
        "Feature flags decouple deploy from release",
        "Matrix builds test across environments",
    ],
    "microservices": [
        "Each service owns its own database",
        "API gateways centralize cross-cutting concerns",
        "Service mesh handles inter-service communication",
        "Event sourcing captures state changes as events",
        "Saga pattern manages distributed transactions",
        "Health checks enable automatic recovery",
        "Distributed tracing tracks requests across services",
        "Contract testing validates service interfaces",
    ],
    "design-patterns": [
        "Singleton ensures only one instance exists",
        "Factory pattern creates objects without specifying classes",
        "Observer pattern enables event-driven communication",
        "Strategy pattern makes algorithms interchangeable",
        "Decorator pattern adds behavior dynamically",
        "Builder pattern constructs complex objects step-by-step",
        "Repository pattern abstracts data access",
        "Adapter pattern bridges incompatible interfaces",
    ],
    "clean-code": [
        "Functions should do one thing well",
        "Meaningful names eliminate the need for comments",
        "Small functions are easier to understand and test",
        "DRY principle reduces code duplication",
        "SOLID principles guide object-oriented design",
        "Composition is often preferred over inheritance",
        "Early returns reduce nesting depth",
        "Code should be easy to read and modify",
    ],
    "debugging": [
        "Reproduce the bug before attempting a fix",
        "Binary search through history using git bisect",
        "Logging is more powerful than print statements",
        "Rubber duck debugging explains code step by step",
        "Stack traces point to error origin",
        "Breakpoints pause execution for inspection",
        "Memory profilers detect leaks and bloat",
        "Assertions catch impossible states early",
    ],
    "optimization": [
        "Premature optimization is the root of evil",
        "Measure before optimizing anything",
        "Big-O analysis predicts scalability",
        "Space-time tradeoffs are fundamental",
        "Batch processing reduces per-item overhead",
        "Denormalization trades consistency for speed",
        "Memoization caches function call results",
        "Vectorized operations beat scalar loops",
    ],
}


def generate_file_content(topic, tip, day_num):
    """Generate meaningful file content."""
    return f"""# {topic.replace('-', ' ').title()} - Note #{day_num}

## Key Insight
{tip}

## Date
Generated on day {day_num} of continuous learning.

## Category
Topic: {topic}

---
*Part of my daily coding knowledge base.*
"""


def run_git(args, date_str=None):
    """Run a git command, optionally with a custom date."""
    env = os.environ.copy()
    if date_str:
        env["GIT_AUTHOR_DATE"] = date_str
        env["GIT_COMMITTER_DATE"] = date_str
    
    result = subprocess.run(
        ["git"] + args,
        cwd=REPO_DIR,
        env=env,
        capture_output=True,
        text=True,
    )
    return result


def main():
    print("=" * 50)
    print("  GitHub Contribution Generator")
    print(f"  Target: {TOTAL_COMMITS} contributions")
    print(f"  Spread across: {DAYS_BACK} days")
    print("=" * 50)

    # Initialize git repo if needed
    if not os.path.exists(os.path.join(REPO_DIR, ".git")):
        run_git(["init"])
        run_git(["config", "user.email", "ayushmandas736@gmail.com"])
        print("Initialized git repository")

    # Create notes directory
    notes_dir = os.path.join(REPO_DIR, "notes")
    os.makedirs(notes_dir, exist_ok=True)

    # Create README
    readme_path = os.path.join(REPO_DIR, "README.md")
    with open(readme_path, "w", encoding="utf-8") as f:
        f.write("""# Daily Coding Knowledge Base

A collection of coding tips, best practices, and insights across software engineering topics.

## Topics Covered
- Algorithms & Data Structures
- System Design & Architecture
- Python, JavaScript & more
- Docker, Kubernetes & Cloud
- Machine Learning & Deep Learning
- DevOps, CI/CD & Security
- Databases, Testing & Performance
- Design Patterns & Clean Code

## Structure
Each note covers a key concept with practical insights.

---
*Building knowledge one day at a time.*
""")

    run_git(["add", "README.md"])
    
    start_date = datetime.now()
    first_commit_date = start_date - timedelta(days=DAYS_BACK)
    first_date_str = first_commit_date.strftime("%Y-%m-%dT09:00:00")
    run_git(["commit", "-m", "Initial commit: Daily Coding Knowledge Base"], first_date_str)

    # Distribute commits across days
    # Create a weighted distribution (more commits on some days, fewer on others)
    random.seed(42)
    
    # Generate dates for commits
    commit_dates = []
    for _ in range(TOTAL_COMMITS):
        days_ago = random.randint(1, DAYS_BACK)
        hour = random.randint(8, 23)
        minute = random.randint(0, 59)
        date = start_date - timedelta(days=days_ago)
        date = date.replace(hour=hour, minute=minute, second=random.randint(0, 59))
        commit_dates.append(date)
    
    # Sort chronologically
    commit_dates.sort()

    # Generate commits
    topic_list = list(TIPS.keys())
    
    for i, commit_date in enumerate(commit_dates):
        topic = topic_list[i % len(topic_list)]
        tips = TIPS[topic]
        tip = tips[i % len(tips)]
        
        # Create/update note file
        filename = f"{topic}_notes.md"
        filepath = os.path.join(notes_dir, filename)
        
        content = generate_file_content(topic, tip, i + 1)
        
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        
        date_str = commit_date.strftime("%Y-%m-%dT%H:%M:%S")
        
        run_git(["add", "."])
        
        commit_msg = f"notes({topic}): {tip[:60]}"
        run_git(["commit", "-m", commit_msg], date_str)
        
        if (i + 1) % 25 == 0:
            print(f"  [OK] {i + 1}/{TOTAL_COMMITS} commits created")

    print(f"\n{'=' * 50}")
    print(f"  [DONE] {TOTAL_COMMITS} commits created!")
    print(f"  Spread from {commit_dates[0].strftime('%Y-%m-%d')} to {commit_dates[-1].strftime('%Y-%m-%d')}")
    print(f"\n  Next steps:")
    print(f"  1. Create repo 'daily-coding-notes' on GitHub")
    print(f"  2. git remote add origin https://github.com/ayushmandas29/daily-coding-notes.git")
    print(f"  3. git branch -M main")
    print(f"  4. git push -u origin main")
    print(f"{'=' * 50}")


if __name__ == "__main__":
    main()
