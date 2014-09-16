Placing Image to this file 


![capture](https://cloud.githubusercontent.com/assets/7775681/4295323/bd8d45e0-3de8-11e4-961c-a0bd5c350098.PNG)



#### How do you add nodes to your Hadoop cluster  ? 


First, add the new node's DNS name to the conf/slaves file on the master node.

Then log in to the new slave node and execute:


$ cd path/to/hadoop
$ bin/hadoop-daemon.sh start datanode
$ bin/hadoop-daemon.sh start tasktracker

If you are using the dfs.include/mapred.include functionality, you will need to additionally add the node to the dfs.include/mapred.include file, then issue hadoop dfsadmin -refreshNodes and hadoop mradmin -refreshNodes so that the NameNode and JobTracker know of the additional node that has been added.
