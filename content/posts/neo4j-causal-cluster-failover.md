Title: Neo4j Causal Cluster Failover  
Slug: neo4j-causal-cluster-failover  
Date: 2018-06-20 03:08:50  
Authors: fkz  
Category: Note  
Tags: Neo4j  
Summary: Failover for Neo4j Causal Cluster might be easier than what you think.  
Modified: 2020-10-26 00:22:50  
  
  
## TL;DR  
  
Use `bolt+routing` protocol for your neo4j client driver to connect to Neo4j causal cluster.  
(If the Neo4j driver you are using supports Bolt Routing Protocol)  
  
---  
  
## Preface  
  
I've been using Neo4j about two months. I established a [Neo4j causal cluster](https://neo4j.com/docs/operations-manual/current/clustering/introduction/) via [Helm chart of Neo4j](https://github.com/kubernetes/charts/tree/master/stable/neo4j) and used it in production with 3 core nodes (1 Leader, 2 Followers) and 3 read replicas.  
  
---  
  
## Problem  
  
Recently, I got an error like this: `Not A Leader Error: Can't write to FOLLOWER node`. It always occured after the leader node became follower node. That's the time I realized there might be a problem of the failover process.  
  
---  
  
## Thoughts  
  
At first, I was trying hard to find a way to make the Kubernetes service of my Neo4j causal cluster to always redirect conneciton to leader node. Because I know that [Neo4j causal cluster comes up with default service discovery mechanism](https://neo4j.com/docs/operations-manual/current/clustering/setup-new-cluster/#causal-clustering-discovery), I was thinking maybe adding a sidecar container to watch the result of cypher shell `dbms.cluster.overview();` and make it change the pod label for the pod, so I can add a selector into Kubernetes service to do what I want.  
  
After I read some posts and codes about how to write a sidecar container in a pod, I still don't know how to do. Just about the time I almost gave up, I found the salvation: <https://graphaware.com/neo4j/2018/01/03/casual-cluster-quickstart.html>.  
  
`bolt+routing://<host>:<port>` caught my eyes.  
  
---  
  
## Solution  
  
It's really simple, but it looks like not many people who use Neo4j causal cluster know about it. I've spent so much time on finding the answer.  
Official documentation of Neo4j also mentioned about it: <https://neo4j.com/docs/developer-manual/current/drivers/client-applications/#_routing_drivers_bolt_routing>. (I should've read official doc more carefully, so I don't have to waste so much time on the wrong path.)  
It turns out if you're using `bolt` protocol (`7687` port) for your Neo4j client to connect to Neo4j cluster and the Neo4j client you're using support the [Bolt Routing Protocol](https://neo4j.com/docs/developer-manual/current/terminology/#term-bolt-routing-protocol), you can just simply change the url of Neo4j:  
  
from `bolt://<host>:<port>`  
to `bolt+routing://<host>:<port>`  
(The `<host>` here for me is the Kubernetes service name of my Neo4j causal cluster)  
  
[I am using `py2neo` as my Neo4j driver and it happens to support Bolt Routing Protocol](http://py2neo.org/v4/database.html?highlight=routing#the-graph). HOW LUCKY.  
  
That's it.  
