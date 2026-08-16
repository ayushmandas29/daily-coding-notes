# Computer Networking — Research-Oriented Notes

## 1. Networking Model
Computer networking enables hosts and applications to exchange information using layered protocols.

The Internet architecture is commonly discussed through TCP/IP layers: link, internet, transport, and application. The OSI model is a useful conceptual reference, but Internet protocols do not map perfectly one-to-one onto OSI layers.

## 2. Application Layer
Important protocols:
- **HTTP/HTTPS:** web communication.
- **DNS:** maps domain names to resource records/IP-related information.
- **DHCP:** dynamically configures hosts with network parameters.
- **SSH:** secure remote administration.
- **SMTP/IMAP/POP:** email transport/access protocols.

## 3. Transport Layer
### TCP
Connection-oriented, reliable byte-stream transport. It provides sequencing, acknowledgements, retransmission, flow control, and congestion control.

### UDP
Connectionless datagram transport with lower protocol overhead but no built-in guarantee of delivery, ordering, or duplicate suppression.

Application requirements determine which is appropriate.

## 4. Internet Layer
IP provides addressing and packet forwarding across interconnected networks.

IPv4 uses 32-bit addresses; IPv6 uses 128-bit addresses.

Important concepts:
- subnetting/CIDR
- routing tables
- default gateways
- ARP for IPv4 local-link address resolution
- ICMP for network-layer control/error reporting

## 5. Ethernet and Local Networks
Ethernet defines common wired LAN mechanisms. Switches forward frames using learned MAC-address information. VLANs logically segment Layer-2 networks.

## 6. Routing
Routers forward packets between networks using routing information. Dynamic routing protocols include OSPF and BGP, which solve different routing problems.

- **OSPF:** interior gateway routing protocol.
- **BGP:** inter-domain routing protocol used between autonomous systems.

## 7. DNS
DNS is a distributed hierarchical naming system. Important record types include A, AAAA, CNAME, MX, NS, TXT, and SOA.

Caching reduces latency and query load but means changes can take time to propagate according to TTL behavior.

## 8. HTTP
HTTP is an application protocol for distributed hypermedia systems.

Important methods:
- GET
- POST
- PUT
- PATCH
- DELETE
- HEAD
- OPTIONS

Important status groups:
- 2xx success
- 3xx redirection
- 4xx client-side conditions
- 5xx server-side conditions

HTTPS uses HTTP over TLS, providing confidentiality and integrity protections when correctly configured.

## 9. TLS
TLS provides secure communication using cryptographic mechanisms for authentication, confidentiality, and integrity. Modern deployments should use current protocol versions and secure cipher/configuration choices.

## 10. Networking for Embedded Systems
Networking matters in embedded engineering because controllers increasingly communicate with sensors, gateways, industrial systems, cloud services, mobile applications, and other controllers.

Study:
- Ethernet
- TCP/IP
- UDP
- MQTT
- HTTP/HTTPS
- CAN/CAN-FD
- Modbus
- TLS
- device addressing
- time synchronization
- OTA updates

## 11. Networking + ML
An embedded ML system may use networking to:
`device → gateway/API → cloud/edge service → model/data pipeline → response`

Networking choices influence latency, reliability, bandwidth, security, and whether inference should happen locally or remotely.

## 12. Network Security
Important controls include:
- segmentation
- firewalls
- authentication
- encryption
- certificate management
- secure protocols
- intrusion detection
- logging
- patching

Avoid treating encryption as a complete security architecture; identity, authorization, key management, endpoint security, and monitoring are also required.

## 13. Performance
Measure:
- latency
- throughput
- packet loss
- jitter
- retransmissions
- connection setup time
- bandwidth utilization

For real-time embedded systems, deterministic behavior and bounded latency may matter more than maximum throughput.

## Trusted Sources
- IETF RFC 8200 — IPv6 — https://www.rfc-editor.org/rfc/rfc8200
- IETF RFC 9293 — TCP — https://www.rfc-editor.org/rfc/rfc9293
- IETF RFC 768 — UDP — https://www.rfc-editor.org/rfc/rfc768
- IETF RFC 9110 — HTTP Semantics — https://www.rfc-editor.org/rfc/rfc9110
- IETF RFC 1034 — DNS Concepts and Facilities — https://www.rfc-editor.org/rfc/rfc1034
- IETF RFC 8446 — TLS 1.3 — https://www.rfc-editor.org/rfc/rfc8446
- IETF RFC 4271 — BGP-4 — https://www.rfc-editor.org/rfc/rfc4271
- IEEE 802.3 Ethernet overview — https://www.ieee802.org/3/
- RFC Editor — https://www.rfc-editor.org/

**Research rule:** when documenting a protocol, record its purpose, packet/message model, state machine where relevant, failure behavior, security considerations, and the authoritative RFC/standard instead of relying on informal summaries.
