# Algorithms-for-Distributed-Processing-Systems-GROUP-6

# Distributed System Algorithms  
### JOMO KENYATTA UNIVERSITY OF AGRICULTURE AND TECHNOLOGY  
### COLLEGE OF ENGINEERING AND TECHNOLOGY  
### SCHOOL OF ELECTRICAL, ELECTRONIC AND INFORMATION ENGINEERING  
### DEPARTMENT OF TELECOMMUNICATIONS AND INFORMATION ENGINEERING  
### ICS 2403: DISTRIBUTED COMPUTING AND APPLICATIONS  

---

## GROUP 6  
| NAME | REG. NO. |
|------|----------|
| Rukiah Mwari | ENE221-0223/2021 |
| Milkah Chelangat | ENE221-0179/2021 |
| Angela Mugwe | ENE221-0220/2021 |
| Dalphine Momanyi | ENE221-0108/2021 |
| Victoria Chege | ENE221-0147/2021 |
| Owens Omwanda | ENE221-0167/2021 |

---

# Distributed System Algorithms

Distributed systems are the backbone of modern computing, but what keeps them running smoothly? It's all about the algorithms. These algorithms are like the secret sauce, making sure everything works together seamlessly. Below are classes of algorithms in Distributed Processing Systems. 

---

## 1. Coordination and Synchronization Algorithms

Synchronization Algorithms interact closely to synchronize parallel executions across dispatched nodes. This synchronization enables multiple processes or threads to run concurrently, preventing race conditions, deadlocks, and inconsistencies. The processes must be allowed to execute concurrently, except when they need to synchronize to exchange information, i.e., communicate about shared data. The synchronization mechanisms can also be viewed as resource management and concurrency management mechanisms to streamline the behavior of the processes that would otherwise act independently. Here are some examples of problems requiring synchronization:
• Physical clock synchronization 

Physical clocks usually diverge in their values due to hardware limitations. Keeping them synchronized is a fundamental challenge to maintain a common time.

Practical applications  
Distributed lock managers in databases, leader election, distributed job scheduling, and coordinated access to shared resources (e.g., billing counters). Used in distributed cron systems, job queues, and the coordination of stateful services. 

Relevance to large-scale cloud environments  
• Cloud orchestration (e.g., leader election in etcd/Kubernetes), distributed transaction coordination, and microservice coordination need reliable synchronization: logical clocks for event ordering and locks/semaphores for resource allocation. These primitives underpin many control-plane services.  
• Distributed Locks: Distributed locks are mechanisms used to coordinate access to shared resources across multiple nodes in a distributed system.  
• Semaphores: Semaphores are another synchronization primitive used to control access to shared resources, particularly in concurrent programming. They can be used to limit the number of concurrent accesses to a resource or to signal events between processes.  
• Distributed Clocks: Distributed clocks are used to maintain synchronized timestamps across multiple nodes in a distributed system.

Relevance  
Synchronization is essential for the distributed processes to overcome the limited observation of the system state from the viewpoint of any one process. Overcoming this limited observation is necessary for taking any actions that would impact other processes. For this purpose, distributed locks, semaphores, and distributed clocks play a significant part. The combination of these guarantees safe synchronization of the system without compromising its performance. 

---

## 2. Consensus Algorithms

Consensus algorithms allow the different nodes distributed throughout them to agree on a single shared value or outcome in spite of individual node failures and disagreements among them (meaning despite the situations when one of the nodes failed or there were discrepancies among them).  
• They provide a fundamental basis for distributed applications like distributed DBMS, blockchain, blockchain networks, and BFT protocols such as Paxos, Raft, and BFT.  
• These guidelines guarantee consistency and fault tolerance in the presence of various types of pathways. 

Relevance to modern telecommunication systems  
• Control-plane consistency (SDN controllers, NFV orchestration), subscriber state replication, and coordinated policy updates require consensus to avoid split-brain and ensure correct routing and session handling. Telecom control components frequently need deterministic leader behavior to maintain session continuity. 

Relevance to large-scale cloud environments  
• Consensus is core to cluster management (Kubernetes’ etcd), configuration propagation, and consistent metadata. Raft is popular due to understandable semantics and engineering usability. For large cloud services, consensus is used for the control plane, not the high-throughput data plane.

---

## 3. Scheduling in Distributed Systems

The techniques that are used for scheduling the processes in distributed systems are as follows:

1. **Task Assignment Approach:** In the Task Assignment Approach, the user-submitted process is composed of multiple related tasks that are scheduled to appropriate nodes in a system to improve the performance of the system as a whole.  
2. **Load Balancing Approach:** The workload is balanced among the nodes of the system.  
3. **Load Sharing Approach:** Ensures no node is idle while processes are waiting for their processing.

Practical applications  
• Kubernetes scheduling, batch job schedulers, NFV placement engines, and distributed batch processing systems. Load-sharing strategies are used for worker pools, task queues, and autoscaling triggers. 

Relevance to modern telecommunication systems  
• Scheduling of media processing tasks (e.g., transcoding), placement of VNFs to meet latency & capacity constraints, and dispatching signaling/processing tasks across core & edge. Dynamic load-sharing reduces dropped calls/overloads during spikes. 

Relevance to large-scale cloud environments  
• Cloud schedulers combine node capacity, pod priorities, affinity/anti-affinity, and locality to place workloads. Autoscalers rely on load metrics to provision more compute. Scheduling theory guides these policies. 

---

## 4. Load Balancing Algorithms

The load balancing algorithms split and distribute the computation task or network traffic equally among the nodes in order to avoid overloading and prevent the resources from being used or wasted.
• They do a smart job of scheduling resources based on workload variances, node capacity, and the metrics of performance.
• This is to ensure efficient resource usage and decrease the response time. Mechanisms like a round-trip schedule and weighted load balancing ensure efficient sharing of work in changing distributed systems.

Different Types of Load Balancing Algorithms are:  
1. Round Robin:
Requests are distributed evenly across servers in a circular manner. Each request is forwarded to the next server in line, ensuring that all servers receive approximately the same number of requests.
2. Least Connection  
Incoming requests are sent to the server with the fewest active connections at the time of the request. This helps to distribute the load based on the current capacity of each server.
3. IP Hash  
The IP address of the client is used to determine which server will handle the request. Requests from the same IP address are consistently routed to the same server, which can be beneficial for session persistence.
4. Weighted Round Robin  
Similar to Round Robin, but servers are assigned weights to reflect their capacity or performance. Servers with higher weights receive a proportionally higher number of requests, allowing for more granular control over load distribution.
5. Least Response Time  
Requests are forwarded to the server with the shortest response time or lowest latency. This algorithm aims to minimize response times for clients by directing them to the server that can respond most quickly.

Practical applications  
• API gateways, HTTP load balancers, session-affinity, edge load balancing, and DNS-based traffic distribution. 

Relevance to modern telecommunication systems  
• Balancing signaling & media across SBCs, distributing sessions among media servers, routing traffic at edge nodes.

Relevance to large-scale cloud environments  
• Service meshes, ingress controllers, health checks, and weighted/latency-based routing.

---

## 5. Reliable and Fault-Tolerant Distributed Systems
A reliable and fault-tolerant environment has multiple requirements and aspects, and these can be addressed using various strategies:
• Consensus algorithms 
All algorithms ultimately rely on message passing, and the recipients take actions based on the contents of the received messages. Consensus algorithms allow correctly functioning processes to reach agreement among themselves in spite of the existence of some malicious (adversarial) processes whose identities are not known to the correctly functioning processes. The goal of the malicious processes is to prevent the correctly functioning processes from reaching agreement. The malicious processes operate by sending messages with misleading information to confuse the correctly functioning processes.
• Replication and replica management Replication (as in having backup servers)  
It's a classical method of providing fault-tolerance. The triple modular redundancy (TMR) technique has long been used in software as well as hardware installations. More sophisticated and efficient mechanisms for replication are the subject of study here.
• Voting and quorum systems 
Providing redundancy in the active (e.g., processes) or passive (e.g., hardware resources) components in the system and then performing voting based on some quorum criterion is a classical way of dealing with fault-tolerance. Designing efficient algorithms for this purpose is the challenge.
• Distributed databases and distributed commit
For distributed databases, the traditional properties of the transaction (A.C.I.D. – atomicity, consistency, isolation, durability) need to be preserved in the distributed setting. The field of traditional “transaction commit” protocols is a fairly mature area. Transactional properties can also be viewed as having a counterpart for guarantees on message delivery in group communication in the presence of failures. Results developed in one field can be adapted to the other.


## 6. Distributed Query Processing Algorithms/Distributed search and retrieval algorithm
Distributed query processing algorithms in distributed systems involve executing queries across multiple nodes to retrieve and process data distributed across the network. These algorithms aim to optimise query performance, minimise communication overhead, and ensure data consistency.
Some distributed query processing algorithms include:
• Parallel Query Execution: Queries are divided into subtasks that can be executed concurrently on multiple nodes. Results are then combined to form the final query result, reducing overall execution time.
• Data Partitioning: Data is partitioned across multiple nodes based on a predefined scheme, such as range partitioning or hash partitioning. Queries are then executed locally on each partition, minimising data transfer between nodes.
• Replica-Aware Query Routing: Queries are routed to nodes containing replicas of the required data, minimising network traffic and improving query performance by leveraging data locality.
• Join Algorithms: Join operations involving data from multiple nodes are optimised using distributed join algorithms such as hash join or merge join, which minimise data transfer and processing overhead.


## 7. Data Partitioning and Sharding
Partitioning in distributed systems refers to dividing a dataset or workload into distinct, manageable segments, known as partitions. This is crucial for enhancing the performance and scalability of distributed applications, as it allows different servers or nodes to handle separate portions of the data concurrently. There are several strategies for partitioning, including horizontal partitioning (dividing rows of a database table) and vertical partitioning (splitting columns).
• By distributing data across multiple nodes, partitioning reduces the load on individual servers and minimises data access times, thereby improving overall system efficiency.
• Additionally, partitioning enhances fault tolerance; if one partition becomes unavailable due to a failure, the rest of the system can still operate normally.

Horizontal Partitioning (Sharding): This strategy divides a table's rows into smaller, distinct groups, or shards. Each shard contains a subset of the data based on specific criteria, such as range or hash of a key attribute. For example, user records might be divided into different shards based on geographic regions or user IDs. This approach enables efficient load distribution and improved query performance, as queries can be directed to specific shards rather than scanning the entire dataset.

Partitioning Use Cases
Partitioning is a critical technique in distributed systems, enabling efficient data management and improving performance. Here are several use cases where partitioning is effectively applied:  

E-Commerce Applications: 
In e-commerce platforms, data related to products, users, and orders can grow rapidly.
• Horizontal Partitioning: User data can be partitioned by geographic location or user ID ranges.
• Vertical Partitioning: Product information can be split into separate tables for basic product details, pricing, and inventory.

Social Media Platforms: 
Social media applications generate massive amounts of user-generated content, including posts, comments, and likes.
• Hash Partitioning: User profiles and posts can be distributed across multiple nodes based on user IDs, ensuring an even load.
• Range Partitioning: Data can be partitioned by date ranges for activities like posts or comments.

Financial Services: 
Financial institutions manage large volumes of transactions, customer data, and historical records.
• Range Partitioning: Transactions can be partitioned by date, allowing efficient querying of recent transactions.
• List Partitioning: Customer data can be partitioned by account types or regions.

IoT (Internet of Things) Applications:
IoT applications collect data from numerous devices, generating vast amounts of time-series data.
• Horizontal Partitioning: Device data can be partitioned based on device ID or geographical location.
• Time-based Partitioning: Data can be partitioned by time intervals, such as hourly or daily.

Content Delivery Networks (CDNs):
CDNs serve large volumes of static content like images, videos, and web pages to users globally.
• Geographic Partitioning: Content can be partitioned based on user location to ensure that requests are directed to the nearest server.
• List Partitioning: Content can be categorized into different types (e.g., images, videos) and stored in separate partitions.
---

## 8. Large Scale Data Processing Algorithms
Introduction to the Problem:
• Large-scale data processing tasks, like indexing the web or analyzing logs, require distributed computing.
• Map and reduce operations allow easy parallelization at the same time that re-execution serves as the primary mechanism for fault-tolerance.

MapReduce model overview:  
<img width="590" height="640" alt="image" src="https://github.com/user-attachments/assets/b23bd08d-52d0-4509-ae4f-d2d561a1fa60" />

Map, written by the developers, takes an input pair and produces a set of intermediate key/value pairs. The MapReduce library groups together all intermediate values associated with the same intermediate Key I and passes them to the Reduce function.
The Reduce function, also written by the developers, accepts an intermediary key I and a set of values for that key. It merges these values to form a possibly smaller set of values. Typically, just zero or one output value is produced per Reduce invocation.  

Execution:  
• Input data is split into chunks and processed in parallel by a distributed set of “map” tasks.
• Intermediate results are shuffled and grouped by key.
• The grouped data is processed by a set of “reduce” tasks, producing the final output.  

Fault Tolerance:  
• MapReduce handles node failures by re-executing tasks on other machines.
• Intermediate data is replicated to ensure it’s available even if a node fails.  

Optimizations:
• The system optimizes data locality, minimizing data transfer over the network.
• Combiners can be used to perform a local reduction before shuffling data, reducing the amount of data transferred.

Programming Model:
• Developers express computations as two functions: map and reduce.
• The system takes care of parallelization, distribution, fault tolerance, and load balancing.

Example Applications:
• The paper provides examples of various applications like distributed grep, distributed sort, and inverted index construction using the MapReduce model.
Implementation Details:
• The paper briefly describes the implementation details of Google’s MapReduce system, covering fault tolerance, data distribution, and the coordination of tasks.

Use Cases:  
• Web Indexing  
• Log Analysis  
• PageRank  
• Genomics  
• Social Networks  
• Fraud Detection  
• Weather  
• E-commerce  
• Ad Systems  
• NLP  

---

## 9. Membership and Failure Detection Algorithms
In distributed systems, maintaining an accurate and up-to-date list of active nodes (membership) and detecting failed nodes promptly (failure detection) are crucial for system reliability and availability. These algorithms enable distributed systems to adapt to dynamic changes in the network topology and node availability.
Includes:  
- Membership Protocols  
Track which nodes are currently active and participating in the distributed system
- Failure Detectors  
 Identify when nodes have become unresponsive or failed
- Gossip Protocols  
Disseminate membership information efficiently through periodic, randomized information exchange

Practical applications:
- Cluster membership in distributed databases (Cassandra, DynamoDB), service discovery in microservices architectures, and node health monitoring in container orchestration platforms like Kubernetes.

Relevance to modern telecommunication systems
- Tracking available network functions in NFV environments, detecting failed base stations or network elements, and maintaining subscriber session state across distributed gateways.

Relevance to large-scale cloud environments
- Auto-scaling groups in cloud platforms, instance health monitoring in AWS EC2/Azure VM, and pod lifecycle management in Kubernetes rely on robust membership and failure detection mechanisms.

 Types of Failure Detection Algorithms

1. Heartbeat-based Detection: Nodes periodically send heartbeat messages to indicate they are alive. Missing heartbeats trigger failure suspicions.

2. Ping-Ack Protocols: Monitoring nodes ping target nodes and wait for acknowledgments. Lack of response within timeout periods indicates potential failures.

3. Accrual Failure Detectors: Provide a suspicion level rather than binary decisions, allowing applications to make informed decisions based on confidence levels.

4. Gossip-based Membership Protocols: Nodes periodically exchange membership information with randomly selected peers, ensuring eventual consistency of the membership view.
  
---

## 10. Clock Synchronisation Algorithms
Relevance to large-scale cloud environments
- Global distributed services requiring coordinated timestamps (Google Spanner's TrueTime), distributed tracing systems, and event sourcing architectures.

 Major Clock Synchronisation Algorithms

1. Network Time Protocol (NTP): Hierarchical time synchronisation protocol that strata clocks to provide microsecond-level accuracy across the internet.

2. Cristian's Algorithm: A Simple client-server approach where clients synchronise with a time server, accounting for network latency.

3. Berkeley Algorithm: An Averaging algorithm where a master node collects times from all nodes, computes the average, and instructs adjustments.

4. Precision Time Protocol (PTP): Provides nanosecond-level synchronisation for local networks, commonly used in financial and industrial systems.

5. Logical Clocks (Lamport Timestamps): Provides partial ordering of events without physical clock synchronisation using incrementing counters.

6. Vector Clocks: Extends Lamport timestamps to capture causal relationships between events in distributed systems.

---

## 11. Distributed Transaction Algorithms
Distributed transaction algorithms ensure atomicity, consistency, isolation, and durability (ACID properties) across multiple nodes in distributed systems. These algorithms coordinate the commit or abort decisions across participating nodes to maintain data consistency.

- Atomic Commitment Protocols: Ensure all nodes either commit or abort a transaction
- Concurrency Control: Manage simultaneous access to distributed data
- Recovery Protocols: Handle transaction recovery after failures

Practical applications
- Distributed databases (Google Spanner, Amazon Aurora), microservices with saga patterns, and financial systems requiring cross-service transactions.

Relevance to modern telecommunication systems
- Billing system transactions, subscriber profile updates across distributed databases, and network configuration changes requiring atomic updates across multiple network elements.

Relevance to large-scale cloud environments
- Cloud-native databases, distributed storage systems, and multi-region application deployments requiring cross-region consistency.


 Key Distributed Transaction Algorithms

1. Two-Phase Commit (2PC): 
   - Phase 1: Coordinator asks all participants to prepare for commit
   - Phase 2: Coordinator decides to commit or abort based on participant responses
   - Provides strong consistency but can block during coordinator failures

2. Three-Phase Commit (3PC):
   - Adds an additional pre-commit phase to reduce blocking scenarios
   - More fault-tolerant than 2PC but more complex

3. Paxos Commit:
   - Uses Paxos consensus algorithm for transaction commitment
   - Provides better fault tolerance than traditional 2PC

4. Saga Pattern:
   - Breaks transactions into a sequence of local transactions with compensating actions
   - Suitable for long-running business processes in microservices

5. Optimistic Concurrency Control:
   - Allows transactions to proceed without locking, validating conflicts at commit time
   - Suitable for low-conflict environments

## 12. Resource Allocation and Auction Algorithms

Resource allocation algorithms manage the distribution of limited resources (CPU, memory, storage, network bandwidth) among competing tasks or users in distributed systems. Auction-based approaches use market mechanisms for efficient and fair resource allocation.

- Centralized Schedulers: Make global allocation decisions based on system state
- Distributed Coordination: Nodes negotiate resource usage through peer-to-peer protocols
- Market-based Approaches: Use pricing and bidding mechanisms to allocate resources

Practical applications
- Cloud resource provisioning, grid computing, content delivery network resource allocation, and multi-tenant platform resource sharing.

Relevance to modern telecommunication systems
- Spectrum allocation in wireless networks, network slice resource allocation in 5G, and edge computing resource management for latency-sensitive applications.

Relevance to large-scale cloud environments
- Spot instances in cloud platforms (AWS EC2 Spot), auto-scaling policies, container resource limits in Kubernetes, and serverless computing resource allocation.



Resource Allocation Strategies

1. Commodity Market Model: Resources are priced based on supply and demand, users purchase what they need

2. Auction-based Allocation:
   - English Auction: Ascending price auction where highest bidder wins
   - Dutch Auction: Descending price auction until a bidder accepts
   - Vickrey Auction: Second-price sealed-bid auction

3. Proportional Share Scheduling: Resources allocated proportionally to weights or bids

4. Cooperative Game Theory: Nodes form coalitions to optimize resource usage

5. DRF (Dominant Resource Fairness): Allocates resources based on users' dominant resource demands

## 13. Self-Stabilizing Techniques in Distributed Processing Systems

Self-stabilizing algorithms enable distributed systems to recover from arbitrary transient faults and eventually reach a legitimate state without external intervention. These techniques provide built-in fault tolerance and resilience against temporary violations of system invariants.

- Automatic Recovery: Systems automatically converge to correct behavior after faults
- Fault Containment: Local faults don't propagate to cause global system failures
- Convergence Guarantees: Theoretical proofs of eventual correctness

Practical applications
- Routing protocols in computer networks, cluster membership management, distributed storage system recovery, and blockchain consensus mechanisms.

Relevance to modern telecommunication systems
- Self-healing networks, automatic recovery of network functions after software faults, and resilient routing in software-defined networks.

Relevance to large-scale cloud environments
- Automatic recovery of microservices, self-healing container orchestration, and resilient data replication in globally distributed databases.

 Self-Stabilization Techniques

1. Local Checking and Correction: Nodes periodically check local state consistency and make corrections

2. Token Circulation: A virtual token circulates through the system, enabling nodes to perform recovery actions

3. Spanning Tree Construction: Self-stabilizing algorithms for building and maintaining distributed spanning trees

4. Reset Mechanisms: Systems can detect illegitimate states and trigger reset procedures

5. Composition Techniques: Combining multiple self-stabilizing algorithms while maintaining overall stabilization properties

 Key Self-Stabilizing Algorithms

1. Dijkstra's Self-Stabilizing System: The seminal work introducing the concept of self-stabilization using a token ring

2. Self-Stabilizing Spanning Tree Protocols: Algorithms that maintain spanning tree structures despite transient faults

3. Self-Stabilizing Mutual Exclusion: Ensures mutual exclusion property is eventually restored after faults

4. Self-Stabilizing Clock Synchronization: Clocks automatically resynchronize after transient inconsistencies

5. Self-Stabilizing Resource Allocation: Resource allocation schemes that recover from arbitrary initial states

## Conclusion
In conclusion, distributed system algorithms form the backbone of modern distributed computing, enabling efficient coordination, communication, and fault tolerance among interconnected nodes. From consensus and replication algorithms to synchronization and security mechanisms, these algorithms play a critical role in ensuring the reliability, scalability, and security of distributed systems.
