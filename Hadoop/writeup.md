##  After Run jps command 

![capture](https://cloud.githubusercontent.com/assets/7775681/4295323/bd8d45e0-3de8-11e4-961c-a0bd5c350098.PNG)



####  1 )  How do you add nodes to your Hadoop cluster  ? 


* First, add the new node's DNS name to the conf/slaves file on the master node.

* Then log in to the new slave node and execute:


$ cd path/to/hadoop
$ bin/hadoop-daemon.sh start datanode
$ bin/hadoop-daemon.sh start tasktracker

If you are using the dfs.include/mapred.include functionality, you will need to additionally add the node to the
 dfs.include/mapred.include file, then issue hadoop dfsadmin -refreshNodes and hadoop mradmin -refreshNodes so
 that the NameNode and JobTracker know of the additional node that has been added.



#### 2 )   Can everyone in class add the remaining members of the class to thier cluster?

    Yes we can add. 
    
####  Can everyone simultaneously run thier own Hadoop cluster, AND be a slave (worker) in another Hadoop cluster?

  Yes  and  I agree with your statment (i.e  This would obviously never be ideal in the real world.)
  
####  can this work as a model in our BigData course? 
 
   I read this article http://bradhedlund.com/2011/09/10/understanding-hadoop-clusters-and-the-network/  
  and what i understood was 
  
  * Hadoop Cluster has Client machines , Master machines , Slave Machines. 
   They perform their duties parallelly inorder  to do things very fast at large scale. 
  * I think if we dedicate some machines   as masters and some machines  as slaves in a hadoop cluster will will get
  better results and better performance .

  
  
  
#### 3 ) Our digital ocean servers only have 512MB of Ram. Can you speculate WHY Hadoop cannot run on a server with such 
minimal resources?

Hadoop jobs written in Java can consume between 1 and 2 GB of RAM per core. 
If you use HadoopStreaming to write your jobs in a scripting language such as Python, more memory may be advisable.
 Due to the I/O-bound nature of Hadoop, adding higher-clocked CPUs may not be the most efficient use of resources, 
 unless the intent is to run HadoopStreaming. Big data clusters, of course, can use as many large and 
 fast hard drives as are available. However, too many disks in a single machine will result in many disks not
 being used in parallel. It is better to have three machines with 4 hard disks each than one machine with 12 drives.
 The former configuration will be able to write to more drives in parallel and will provide greater throughput. 
 Finally, gigabit Ethernet connections between machines will greatly improve performance over a cluster connected via a
 slower network interface.

