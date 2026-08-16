# Cloud Computing — Research-Oriented Notes

## 1. Foundations
Cloud computing provides on-demand access to shared computing resources such as compute, storage, networking, and managed services. NIST defines essential characteristics including on-demand self-service, broad network access, resource pooling, rapid elasticity, and measured service.

### Service models
- **IaaS:** virtualized compute, storage, networking; customer manages OS and applications.
- **PaaS:** provider manages more of the runtime/platform; customer focuses on applications.
- **SaaS:** complete application delivered as a service.
- **Serverless:** developer deploys functions/services while the platform manages server capacity and scaling.

### Deployment models
Public, private, hybrid, and community models address different governance and infrastructure requirements.

## 2. Core Architecture
A production cloud system normally combines:
`clients → DNS/CDN → load balancer/API gateway → application services → cache/database/object storage → observability`

Important concerns are availability, scalability, fault isolation, security, cost, latency, and recovery.

## 3. Compute
Virtual machines provide isolation and configurable operating systems. Containers package applications with dependencies and are lighter-weight than full VMs. Serverless functions are useful for event-driven workloads but introduce execution/runtime constraints.

## 4. Storage
- **Object storage:** durable blobs/files, backups, data lakes.
- **Block storage:** persistent virtual disks.
- **File storage:** shared filesystem semantics.

Storage design should consider durability, availability, consistency, latency, lifecycle, encryption, and cost.

## 5. Networking
Study VPC/VNet concepts, subnets, routing, security groups/firewalls, load balancing, NAT, DNS, private endpoints, and CDN architectures.

## 6. Databases
Managed cloud databases may be relational, key-value, document, graph, time-series, or analytical systems. Select based on access patterns rather than popularity.

## 7. Reliability
Use redundancy, health checks, automated recovery, backups, replication, graceful degradation, and tested disaster-recovery procedures.

Important terms:
- **RTO:** acceptable recovery time.
- **RPO:** acceptable data-loss window.

## 8. Security
Apply least privilege, strong identity controls, encryption in transit/at rest, secrets management, network segmentation, logging, vulnerability management, and continuous monitoring.

## 9. Cloud + ML
Typical ML architecture:
`data sources → object storage/data warehouse → preprocessing → training → model registry → serving → monitoring`

Cloud is useful for elastic training and managed deployment, but it does not remove the need for data governance, reproducibility, model evaluation, or cost control.

## Trusted Sources
- NIST SP 800-145 — https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-145.pdf
- NIST Cloud Computing Program — https://www.nist.gov/programs-projects/nist-cloud-computing-program
- AWS Well-Architected Framework — https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html
- Microsoft Azure Architecture Center — https://learn.microsoft.com/azure/architecture/
- Google Cloud Architecture Framework — https://cloud.google.com/architecture/framework

**Research rule:** document architecture decisions, assumptions, failure modes, security controls, cost model, and recovery strategy rather than treating cloud services as interchangeable building blocks.
