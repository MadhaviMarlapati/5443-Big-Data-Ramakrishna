Topic: Dynamic Query Optimizers for   Big Data 

Querying massive datasets is time consuming and expensive without the right hardware and infrastructure. Enterprises are adapting large-scale data processing platforms, such as Hadoop, to gain actionable insights from their “big data”. Query optimization is still an open challenge in this environment due to the volume and heterogeneity of data. Query on big data can be optimized in different ways.  Twitter and Facebook uses its own tools to query and analyze large volumes of data dynamically.


A  Paradigm for learning queries on Big Data

Formal query languages are not sufficient to analyze big data. Big data may have instances of databases. This paper proposes a novel paradigm for interactive learning of queries on big data, without assuming knowledge of database schema. An important part of paradigm is a function that identifies in the input database instance a set of small, easy to visualize fragments, from which we ask the user to choose the interested elements. Another important function of paradigm is measuring the potential information. Two instantiations of paradigm were discussed, those are learning relational join queries and learning graph queries. 





Fast Data in the Era of Big Data: Twitter’s
Real-Time Related Query Suggestion Architecture

This paper discusses how twitter is querying the big data. Initially twitter tried to use Hadoop. But Hadoop does not given better results. Then twitter started implementing its own methodology to query big data. It is custom in-memory processing engine specifically designed for the task.  This paper provides a case study illustrating the challenges of real-time data processing in the era of big data. Three aspects of data velocity, volume and variety has to be considered. Twitter want to develop a search assistance, that needs to be provided in real time and must dynamically adapt to the rapidly evolving global conversation. Twitter has to provide dynamic search assistance and has to return the results dynamically. Twitter’s Hadoop based analytics stack built primarily around Pig .


MISO: Souping Up Big Data Query Processing with a
Multistore System

Multistore systems utilize multiple distinct data stores such as Hadoop’s HDFS and an RDBMS for query processing by allowing a query to access data and computation in both stores. Tuning the physical design of a multistore, i.e., deciding what data resides in which store, can reduce the amount of data movement during query processing, which is crucial for good multistore performance. Author discusses method called MISO for MultISstore Online tuning, is adaptive, lightweight, and works in an online fashion utilizing only the by-products of query processing. 

In a multistore scenario there are two data stores, the big data store and the RDBMS. In our system, the big data store is Hive (HV) and the RDBMS is a commercial parallel data warehouse (DW). Tuning the physical design of a multistore system is important to obtaining good query performance. In a multistore system, the query optimizer can choose many different split points at which to migrate computation from one store to the other during query evaluation. The overall execution time of a query is dependent on the existing physical design of each store, and varies depending on which portion of the query is evaluated in which store.


Designing Query Optimizers for Big Data Problems of The
Future

The Vertica SQL Query Optimizer was written from the ground up for the Vertica Analytic Database. Its design, and the tradeoffs they encountered during implementation, support the case that the full power of novel database systems can be realized only with a custom Query Optimizer. The Vertica Analytic Database (Vertica) is a modern, commercially successful RDBMS. It contains a SQL query optimizer, written from scratch, especially for the Vertica Storage System and Execution Engine. Vertica developed three versions of query optimizers. They are StarOpt , StarifiedOpt and V2Opt. V2Opt as fully extensible for ongoing improvements and future Big Data requirements.

Dynamically Optimizing Queries over
Large Scale Data Platforms

Query optimization is still an open challenge in big data, due to the volume and heterogeneity of data, comprising both structured and un/semi-structured datasets. It has become common practice to push business logic close to the data via user defined functions (UDFs), Author introduces “pilot runs” for querying big data. Which execute part of the query over a sample of the data to estimate selectivities, and employ a cost-based optimizer that uses these selectivities to choose an initial query plan. Then, follows a dynamic optimization approach, in which plans evolve as parts of the queries get executed. Author address the query optimization problem for large scale data platforms, by continuously collecting statistics during query execution, and feeding these statistics to a cost-based query optimizer to decide the next query sub-expression to execute. Author implemented techniques in the context of Jaql. Author discusses the pilot runs algorithm 
 


References: 
[1]	Bonifati, A., Clucanu, R., Lemay, A., Staworko, S., A paradigm for learning queries on big data. Proceedings of DATA4U '14 (September 2014, Hangzhou, Chaina), 7-12.
[2]	Karanasos, K., Balmin, A., Kutsch, M., Ozcan, F., Ercegovac, V., Xia, C., Jackson, J.,             Dynamically Optimizing Queries over Large Scale Data Platforms. Proceedings of SIGMOD '14  (June 2014, UT, USA), 943-954.
[3]	LeFerve, J., Snakaranarayanan, J., Hacigumus, H., Tatemura, J., Polyzotis, N., Carey, M., MISO: souping up big data query processing with a multistore system. Proceedings of SIGMOD '14 (June 2014, UT, USA), 1591-1602.
[4]	Mishne, G., Dalton, J., Li, Z., Sharma, A., Lin, J., Fast data in the era of big data: Twitter's real-time related query suggestion architecture.  Proceedings of SIGMOD '13 (June 2013, NY, USA), 1147-1158.
[5]	Tran, N., Bodagala, S., Dave, J., Designing query optimizers for big data problems of the future. Proceedings of the VLDB Endowment (August 2013, Trento, Italy), 1168-1169.

