##  After Run jps command 

![capture](https://cloud.githubusercontent.com/assets/7775681/4295323/bd8d45e0-3de8-11e4-961c-a0bd5c350098.PNG)



#### How do you add nodes to your Hadoop cluster  ? 


First, add the new node's DNS name to the conf/slaves file on the master node.

Then log in to the new slave node and execute:


$ cd path/to/hadoop
$ bin/hadoop-daemon.sh start datanode
$ bin/hadoop-daemon.sh start tasktracker

If you are using the dfs.include/mapred.include functionality, you will need to additionally add the node to the dfs.include/mapred.include file, then issue hadoop dfsadmin -refreshNodes and hadoop mradmin -refreshNodes so that the NameNode and JobTracker know of the additional node that has been added.



####  Can everyone in class add the remaining members of the class to thier cluster?

    Yes 
    
####  Can everyone simultaneously run thier own Hadoop cluster, AND be a slave (worker) in another Hadoop cluster?

  Yes  and  I agree with your statment (i.e  This would obviously never be ideal in the real world.)
  
####  can this work as a model in our BigData course? 

  I read this article http://bradhedlund.com/2011/09/10/understanding-hadoop-clusters-and-the-network/  
  and what i understood was 
  
   Hadoop Cluster has Client machines , Master machines , Slave Machines. 
  They perform their duties parallelly inorder  to do things very fast at large scale. 
  I think some machines are dedicated as masters and some machines are dedicated as slaves in a hadoop cluster will give better results.
