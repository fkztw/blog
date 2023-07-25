Title: CPB200: BigQuery for Data Analysts  
Slug: cpb200-bigquery-for-data-analysts  
Date: 2016-12-15 09:45:43  
Authors: fkz  
Category: Conf/Meetup  
Tags: Google Cloud Platform  
Summary:  [CPB200](http://gcp.kktix.cc/events/05409197) 筆記  
Modified: 2016-12-16 17:07:43  
  
  
# 課程資訊  
  
+ <http://myclass.gcptrain.org/>  
    + azkyY21yCg==  
    + <https://sites.google.com/a/google.com/cloud-platform-training/cloud-platform-training/cpb200-bigquery-for-data-analysts>  
    + [slides](/files/cpb200-bigquery-for-data-analysts/CPB200.zip)  
+ Google 系列課程  
    + CP100: 介紹性質，廣而淺，新手課程。  
    + CP200: 開始針對單一技術做比較深的介紹。  
    + CP300: 五個全天的課程，上完之後一個月內通過線上考試可以拿到 CP300 證照。  
    + [GDE: Cloud Developer Expert](https://developers.google.com/experts/)  
  
---  
  
# Day 1: 2016/12/15  
  
---  
  
# Course Introduction  
  
---  
  
# Module 1: Introducing BigQuery  
  
+ SMACK  
    + Spark  
    + Mesos  
    + Akka  
    + Cassandra  
    + Kafka  
  
## Big Data Current State  
  
+ Real-Time Streaming Data  
+ Web analysis data  
+ IoT sensor data  
+ Fraud detection  
+ 一台 8-core, 32GB RAM 的 server 在普通情況下，大概撐不到 1000 個 concurrent connection  
  
## On Premises Versus Cloud  
  
Premises => Warehouse  
  
公司有機房的聽眾：「申請一台機器最快要一個禮拜才能用，一台機器要撐 3~5 年。」  
  
  
## Google's History of Innovation in Big Data  
  
+ Google Big Data Stack 1.0  
    + 2002: GFS  
    + 2004: MapReduce  
    + 2005: Bigtable  
+ Google Big Data Stack 2.0  
    + 2006: Dremel  
        + Apache Drill  
        + Query Engine  
    + 2010: Colossus  
    + 2011: Megastore  
    + 2012: Millwheel  
        + 處理 Streaming 的資料  
        + 和 Apache Beam 有關  
        + Google Cloud Dataflow is based on Millwheel  
        + Dataflow 會幫你預測資料大小，然後去做調整。  
  
## What is BigQuery  
  
+ Fully-managed, analytics data warehouse.  
    + Near real-time interactive analysis  
        + batch / streaming  
    + NoOps - No administration for performance and scale  
        + 但 OPs 還是得注意每天和每個月的 BigQuery 用量  
+ Reliable  
+ Economical  
+ Secure  
    + 可以透過 ACL 分享 dataset  
    + Data is encrypted in transport and at rest  
+ Auditable  
    + Immutable logs  
        + 除非是共用帳號，不然都找得到誰做了什麼事。  
+ Scalable  
    + Virtually unlimited data storeage and processing power.  
+ Flexible  
    + Streaming ingestion: 100K rows/sec per table for real-time data  
    + Data mashup: JOIN across diverse datasets/projects  
+ Easy to use  
    + Requires no indexes, keys, or partitions  
    + Familiar SQL interface and intuitive UI  
    + Nested and repeated field support for schema flexibility  
  
## BigQuery Is Not  
  
+ Transactional RDBMS  
    + BigQuery is not an OLTP system  
    + BigQuery 不像 RDBMS 要做正規化，反而是要做反正規化，讓資料愈扁平愈好  
    + RDBMS 要求 query 要在數毫秒，但 BigQuery 的 query  
+ Operational Data Store  
    + BigQuery is not geared towards capturing live data and applying updates/deletes as they happen in the system of record  
+ On-premises solution or appliance  
    + BigQuery is a self-contained, cloud-based solution  
  
## Comparisons  
  
+ OLTP (Online Transaciton Processing)  
+ OLAP (Online Analytical Processing)  
    + Similar in use cases they support  
    + BigQuery allows querying via SQL  
+ MapReduce  
    + Fundamentally a batch oriented technology  
    + Higher latency than BigQuery  
+ NoSQL  
    + Less scalable than BigQuery  
    + Awkward or impossible to query - No query language  
  
## BigQuery Use Cases  
  
+ Games and social media analytics  
+ Advertising campaign optimization  
+ Sensor data analysis  
+ POS-Retail Analytics  
+ Web logs, machine logs, infrastructure monitoring  
    + Google 利用 Machine Learning 分析 Machine logs 來去針對 server 做最佳的管理  
+ [Mobile Gaming Analytics](https://cloud.google.com/solutions/mobile/mobile-gaming-analysis-telemetry)  
+ [Zulily  |  Google Cloud Platform](https://cloud.google.com/customers/zulily/)  
  
## Lab 1  
  
[Sign Up for the Free Trial and Create a Project](https://codelabs.developers.google.com/codelabs/cpb200-free-trial/#0)  
  
  
---  
  
# Module 2: BigQuery Functional Overview  
  
## BigQuery Project Structure  
  
+ Project  
    + Top-level structure  
    + Contains users, APIs authentications, billing, data, access control lists (control access to datasets and jobs)  
+ Dataset  
    + Named parent of 1 or more tables  
    + 一堆 Table 的集合  
    + Support Partition Tables  
    + 如果資料存入以後沒有異動，3個月以後，費用會減半。  
+ Table  
    + Columnar structure that stores data  
+ Job  
    + Controls potentially long-running actions  
  
### Projects  
  
+ 可以決定要把哪些 Table 分享給哪些人  
+ 已經做完的 Job 不用 Clean 掉，因為沒有說執行過多少 Job 就不能執行  
  
### Datasets  
  
+ Reader  
+ Editor  
+ Owner  
    + 可以分享  
  
### Tables  
  
+ Collection of columns, rows  
+ Have a schema  
+ Views are supported  
+ Can be external (federated)  
    + Google Cloud Storage, Google Drive  
    + 可以從外部載入資料，例如只想存在自己的 Cloud Storage 的資料  
  
### Jobs  
  
+ 每一次執行 query 都會產生一個 Job  
+ Job 是 by user 紀錄的  
+ 以前不能 update, 現在可以 update 了  
    + 可以直接使用 Job ID 來 update insert 的內容  
  
## BigQuery Storage  
  
+ Traditional RDBMS Storage  
    + Row based  
    + Record-oriented storage  
    + 透過 index 和正規化讓資料查詢可以更快速  
+ BigQuery Storage  
    + Column based  
    + Columnar storage  
  
### BigQuery Managed Storage  
  
+ BigQuery data is stored on persistent disks in distributed storage  
+ No indexes, keys, or partitions are required  
+ Scales to dozens of petabytes  
  
### Storage Engine 2006-2015: ColumnIO  
  
Date => Decompress -> Filter (MapReduce) => Emit  
  
### Storage Engine 2016-Now: Capacitor  
  
Data => Emit => Dictionary => Filter => Lookup  
  
ref: <https://cloud.google.com/blog/big-data/2016/04/inside-capacitor-bigquerys-next-generation-columnar-storage-format>  
  
  
## BigQuery Processing  
  
+ Borg - Cluster management system  
+ Dremel query engine  
  
### Query Processing 2006-2015  
  
Mixer 0 <= Mixer 1 <= Leaf <= Juniper (Network) => Distributed Storage (Colossus)  
  
### Query Processing 2015-Present  
  
Master <= Shard <= Shard <= Shard <= Juniper (Network) => Distributed Storage (Colossus)  
  
  
## BigQuery Web User Interface  
  
+ 要不要用 Cache  
+ 要不要用 Legacy SQL  
+ 查詢前記得按一下右邊的 Validator，檢查語法順便看一下總共會 Query 多少資料，以免費用爆表。  
  
## BigQuery CLI  
  
+ 可以從 Cloud Shell 或 Cloud SDK 使用 bq  
    + `bq help`  
    + `bq ls`  
    + `bq mk`  
    + `bq load`  
  
## Lab 2  
  
[BigQuery Interfaces](https://codelabs.developers.google.com/codelabs/cpb200-bigquery-interfaces/#0)  
  
  
---  
  
# Module 3: BigQuery Fundamentals  
  
  
## BigQuery Schemas  
  
+ Consist of 1 or more fields (flat or nested)  
+ Define the field name, data type, and mode of columns in the table  
+ Fields are strongly typed (explicitly defined)  
+ Modes indicate whether field data is REQUIRED, NULLABLE or REPEATED  
    + REQUIRED fields must contain non-null data  
    + NULLABLE fields allow null values  
    + REPEATED fields contain an array of values  
  
### Schema Specification  
  
+ Specify schema on command line or in JSON file  
+ Schema file must contain single array object with entries that provide these properties:  
    + "name": Name of the column  
    + "type": Type of data  
    + "mode" (optional): REQUIRED, NULLABLE or REPEATED  
+ Example JSON schema:  
  
```  
[  
    {"name": "name", "type": "string", "mode": "required"},  
    {"name": "gender", "type": "string", "mode": "nullable"},  
    {"name": "count", "type": "integer", "mode": "required"}  
]  
```  
  
  
## Denormalized Data in BigQuery  
  
+ BigQuery uses a denormalized or "flat" schema  
    + Flatten normalized tables for super-fast querying  
    + No performance penalty for sparse columns or duplicate data  
    + Pre-join datasets into homogeneous tables  
    + Trade JOINS for column scans  
        + Storage is more performant and cheaper than compute resources  
    + Use nested repeated schema (using JSON or AVRO format) to simulate normalization benefits and limit duplication of data  
        + Without nesting, aggregation or JOINs are required  
  
### Denormalization Example  
  
+ A normalized one-to-many relationship between people and cities_lived is denormalized (“flattened”) into 1 table  
    + A person may have one to many rows in the table  
    + Name, age, and gender may be duplicated  
+ Using nested repeated schema avoids duplication of data  
+ Still allows for a flattened table, which retains high performance  
  
  
## BigQuery Jobs  
  
+ BigQuery defines and executes jobs for:  
    + Query execution  
    + Loading, copying, and exporting data  
+ Jobs are atomic  
+ Multiple jobs can run concurrently  
+ Completed jobs are listed in the jobs collection  
+ Jobs have 4 components:  
    + Reference – Job ID  
    + Configuration – Job task  
    + Status – Job state  
    + Statistics – Job statistics  
+ Job History 是 by user 的  
    + 要看到整個 project 的 BigQuery Job History 的話，要到 Cloud Logging 那邊選擇 BigQuery 查看  
  
  
## Destination Tables and Caching  
  
+ Query results are stored in a destination table  
+ Table is temporary or user-defined  
+ Temporary tables are:  
    + Defined by the service  
    + Used as query cache – You are not billed for storage  
+ User-defined tables:  
    + Remain persistent  
    + Are billed at normal storage rates  
    + Target location can be any accessible project/dataset  
  
### Query Caching  
  
+ Query results are cached to improve performance  
    + Subject to same quota policies as non-cached queries  
    + Cache results have a size limit of 128 MB compressed  
+ No charge for queries that use cached results  
+ Results are cached for approximately 24 hours  
    + Lifetime extended when a query returns a cached result  
+ Cache can be turned off  
  
在 Web UI 要怎麼知道是 Cached Query? => 仔細看算 query 時間結果後面的小括號，會標示 cached。  
  
  
#### Caveats  
  
+ Query caching only works for predictable queries  
    + When result set is identical to previous run(s) of a query  
+ Cache is per-user  
    + Not shareable across users  
+ Cache is invalidated if:  
    + Data in underlying table(s) changes  
    + Query uses dynamic functions, such as `CURRENT_TIMESTAMP()` or `NOW()`  
  
## Lab 3  
  
[BigQuery Components and Jobs](https://codelabs.developers.google.com/codelabs/cpb200-bigquery-components/#0)  
  
---  
  
# Module 4: Ingesting, Transforming and Storing Data  
  
## Ingesting Data  
  
+ Load data into BigQuery using CLI, web UI, or API  
+ Load data directly into BigQuery storage using streaming insert or a load job  
+ Load jobs support:  
    + Google Cloud Storage  
        + Standard, Durable Reduced Availability, or Nearline (reduced performance)  
    + Google Drive (JSON, CSV, AVRO, Sheets (first tab only))  
    + CSV, JSON, [AVRO](https://avro.apache.org/docs/current/) file uploads (slower)  
+ Can also use partner-provided tools/services  
+ Load jobs support four data sources:  
    + Objects in Google Cloud Storage  
    + Data sent with the job or streaming insert  
    + A Google Cloud Datastore backup  
    + Data in Google Drive  
+ Data can be:  
    + Loaded into a new table  
    + Appended to a table  
    + Used to overwrite a table  
+ BigQuery can ingest both compressed (GZIP) and uncompressed files  
    + Highly parallel load operations allow uncompressed files to load significantly faster than compressed files  
    + Uncompressed files are larger  
        + Possible bandwidth limitations  
        + More costly to store  
+ Weigh compression options based on use case  
+ File size limits  
    + CSV  
        + Compressed: 4GB  
        + Uncompressed  
            + With newlines: 4GB  
            + Without newlines: 5TB  
    + JSON (newline delimited)  
        + Compressed: 4 GB  
        + Uncompressed: 5 TB  
    + AVRO  
        + Compressed: Compressed files not supported; compressed data blocks are.  
        + Uncompressed: 5 TB (2 MB for the file header)  
  
> Datastore == BigTable + [MegaStore](http://research.google.com/pubs/pub36971.html)  
  
## Appending and Reloading Data  
  
+ Use CLI or API to append data to an existing table  
+ BigQuery does support deletes now (If unchecked the "use Legacy SQL")  
  
## Lab 4.1  
  
[Loading Data into BigQuery and Using Federated Queries](https://codelabs.developers.google.com/codelabs/cpb200-loading-data/#0)  
  
## Processing/Transforming Data  
  
### Schema Design Considerations  
  
+ Denormalized versus relational  
    + Denormalized yields better performance with some duplication  
    + JOINS on relational data are performant but can be slower than queries on denormalized data  
+ Flat versus nested and repeated  
+ Table partitioning  
    + Single table for all data  
    + Partition data by some range of values (date) - covered later  
    + Table decorators (partition, snapshot) - covered later  
        + `@`  
        + <https://cloud.google.com/bigquery/table-decorators>  
        + <http://blog.gdeltproject.org/using-bigquery-table-decorators-to-lower-query-cost/>  
  
### Data Format Considerations  
  
+ BigQuery supports three data formats: AVRO, JSON, CSV  
+ AVRO:  
    + Open source format that bundles serialized data and schema in same file  
    + Supports flat data and nested/repeated fields  
        + Nested/repeated data useful for expressing hierarchical data, reduces duplication when denormalizing data  
    + Loads faster in BigQuery if data contains embedded newlines  
    + Limited to 16 MB block size  
+ JSON (newline-delimited):  
    + Supports flat data and nested/repeated fields  
        + Nested/repeated data useful for expressing hierarchical data, reduces duplication when denormalizing data  
    + Loads faster in BigQuery if data contains embedded newlines  
    + One JSON object, including any nested/repeated fields, must appear on each line  
    + Supports UTF-8 encoding  
    + Limited to 2 MB row size  
    + Example  
```  
{"name": "abc", "gender": "M", "age": 38}  
{"name": "abc", "gender": "M", "age": 48}  
```  
+ CSV:  
    + Supports flat data only  
        + No nested/repeated data  
    + Supports UTF-8 encoding and ISO-8859-1 encoding  
        + If loading ISO-8859-1 encoded data, specify configuration.load.encoding property when creating load job  
    + Limited to 2 MB row and cell size  
  
  
## Storing Data  
  
### Long-Term Storage in BigQuery  
  
+ Automatic discount for data stored longer than 90 days  
    + If table data modified, 90-day counter resets  
+ No need to delete or archive old data  
    + Equivalent to cost of Cloud Storage Nearline  
    + 量大的時候似乎還是會比較貴，所以還是有人選擇 archive 到 GCS  
+ If preferred, store data in Cloud Storage and load into BigQuery when needed  
    + No charge for loading/exporting data  
    + Loading from Cloud Storage Nearline reduces performance  
    + Data in Cloud Storage available to other services  
  
---  
  
# Module 5: Pricing and Quotas  
  
要自己把費用算的很精確太難了，  
Google Cloud Platform 有各種不同的計費方式，  
這邊的重點當然還是放在怎麼省錢，  
順便瞭解一下計費方式。  
  
---  
  
# Module 6: Clauses and Functions  
  
## UDF Constraints  
  
+ Max output data size: 5 MB per input row  
+ Max number of UDFs that can run concurrently per user = 3  
+ *Native code JavaScript functions are not supported*  
+ The DOM objects Window, Document and Node, and functions that require them, are unsupported  
+ Bitwise operations in JavaScript handle only the most significant 32 bits  
  
## UDF Best Practices  
  
+ Use UDF test tool to debug to avoid incurring BigQuery charges  
+ Avoid persistent mutable state  
    + Do not store or access mutable state in UDF calls  
    + Each BQ node has local javascript processing environment that may produce local values  
+ Use memory efficiently to avoid memory exhaustion on local JavaScript environments  
+ Explicitly list SELECT columns instead of SELECT * (not supported)  
+ Pre-filter input to limit the size of data on which UDF will run  
  
  
## BigQuery Recipes  
  
投影片裡的範例不知道是不是故意排版的很醜讓人看不懂...  
其實只要照下面把 Query statement 排版一下  
再從最裡面的 Query 看到最外面就滿好懂了  
只是像一些 BigQuery 特有的 function: `EVERY()`, `SOME()`, `LAG()` 之類的  
只好到 <https://cloud.google.com/bigquery/docs/reference/legacy-sql> 察看文件了  
  
### Pivot  
  
Find 100 largest words in Shakespeare’s works and display the number of occurrences of those words in four of Shakespears more popular works.  
  
```bigquery  
SELECT  
    word,  
    SUM(IF(corpus = 'kinglear', corpus_total, 0)) AS kinglear,  
    SUM(IF(corpus = 'tempest', corpus_total, 0)) AS tempest,  
    SUM(IF(corpus = 'macbeth', corpus_total, 0)) AS macbeth,  
    SUM(IF(corpus = 'hamlet', corpus_total, 0)) AS hamlet,  
    SUM(corpus_total) AS [total]  
FROM (  
    SELECT  
        word,  
        LENGTH(word) AS word_len,  
        corpus,  
        SUM(word_count) AS corpus_total  
    FROM [publicdata:samples.shakespeare]  
    WHERE LENGTH(word) > 10  
    GROUP BY word, word_len, corpus  
)  
GROUP BY word, word_len  
ORDER BY word_len DESC  
LIMIT 100  
```  
  
### Cohort Analysis  
  
Counts of Wikipedia contributors who contribute only to pages on Manning brothers vs those who contributed to Manning brothers pages and other pages. Query highlights EVERY and SOME functions.  
  
```bigquery  
SELECT  
    peyton_all,  
    peyton_some,  
    eli_all,  
    eli_some,  
    COUNT(1) AS NUM,  
    AVG(edits) AS avg_edits  
FROM (  
    SELECT  
        contributor_id,  
        EVERY(peyton_edit) AS peyton_all,  
        SOME(peyton_edit) AS peyton_some,  
        EVERY(eli_edit) AS eli_all,  
        SOME(eli_edit) AS eli_some,  
        COUNT(1) AS edits  
    FROM (  
        SELECT  
            contributor_id,  
            (LOWER(title) CONTAINS 'peyton manning') AS peyton_edit,  
            (LOWER(title) CONTAINS 'eli manning') AS eli_edit  
        FROM [publicdata:samples.wikipedia]  
    )  
    GROUP BY contributor_id  
    HAVING peyton_all OR peyton_some OR eli_all OR eli_some  
)  
GROUP BY peyton_all, peyton_some, eli_all,eli_some  
ORDER BY peyton_all, peyton_some, eli_all,eli_some  
```  
  
### Trailing Averages  
  
Demonstrates windowing functions to calculate moving average on number Trailing avg of user activities in github.  
Outermost query combines trailing values into a weighted average paying attention to missing values.  
  
```bigquery  
SELECT  
    start_date,  
    ((num_0 + if(num_1 > -1, num_1, num_0) * 0.5 + if(num_2 > -1, num_2, num_0) * 0.25) / 1.75) AS smooth_num  
FROM (  
    SELECT  
        start_date, num_0,  
        LAG(num_0, 1, integer(-1)) OVER (ORDER BY start_date) AS num_1,  
        LAG(num_0, 2, INTEGER(-1)) OVER (ORDER BY start_date) AS num_2  
    FROM (  
        SELECT  
            DATE(created_at) as start_date,  
            INTEGER(COUNT(1)) num_0  
        FROM [publicdata:samples.github_timeline]  
        GROUP BY start_date  
    )  
)  
ORDER BY smooth_num DESC  
```  
  
---  
  
# Day 2: 2016/12/16  
  
---  
  
# Module 7: Nested, Repeated, and Nested Repeated Fields  
  
## Nested Field  
  
"type": "RECORD"  
  
+ BigQuery supports importing and exporting nested fields in JSON and AVRO files  
+ A nested record field adds a named substructure to a row of data  
+ Useful as a mechanism to organize related information  
  
### Example: JSON Nested Schema and Data  
  
Schema  
```  
[{"name": "name", "type": "string", "mode": "REQUIRED"},  
{"name": "book", "type": "RECORD", "fields":  
    [  
    {"name": "title", "type": "string"},  
    {"name": "ISBN", "type": "string"}  
    ]  
}]  
```  
  
Data (Newline-delimited JSON)  
```  
{"name": "randolph", "book": {"title": "The Beginning", "ISBN": "213423422" } }  
{"name": "charles", "book": {"title": "Fortunate Few", "ISBN": "993032933" } }  
{"name": "james", "book": {"title": "Homeward Bound", "ISBN": "884920039" } }  
```  
  
### Querying Nested Fields  
  
+ BigQuery automatically flattens nested fields when querying  
    + `SELECT * ... results in columns <record_name>_<nested_field_name>`  
+ To query a specific nested field:  
    + `SELECT name, book.title FROM [dataset.table]`  
  
## Lab 7.1  
  
CSV 無法表示 nest 結構，所以要上傳有 nested fields 的 data 的話，只能用 JSON 或 AVRO  
  
  
## Repeated Fields  
  
"mode": "REPEATED"  
  
+ BigQuery supports importing and exporting repeated fields in JSON and AVRO files  
+ A repeated field adds an *array* of data inside a single field or record  
+ Useful as a mechanism to denormalize a foreign table  
  
### Example: JSON Repeated Schema and Data  
  
Schema  
```  
[  
{"name": "name", "type": "string", "mode": "REQUIRED" },  
{"name": "city", "type": "string", "mode": "REPEATED" },  
{"name": "book", "type": "string", "mode": "REPEATED" }  
]  
```  
  
Data  
```  
{"name": "randy", "city": ["Tucson", "Houston", "Seattle"], "book": ["The Fudge"]}  
{"name": "charlie", "city": ["Tucson", "Seattle", "Redmond"], "book": []}  
{"name": "cynthia", "city": ["Houston", "Austin"], "book": ["The Fudge", "Outlaws"]}  
```  
  
### Querying Repeated Fields  
  
+ A query such as `SELECT * ...` produces an error:  
    + Cannot output multiple independently repeated fields at the same time  
    + 一定只能 flatten 其中一個 repeated field (下面 Querying Multiple Repeated Fields 的作法）  
+ Querying one repeated field, yields automatically flattened result  
    + Example: `SELECT name, book FROM [dataset.table]`  
  
### Querying Multiple Repeated Fields  
  
+ FLATTEN operator unrolls multiple repeated fields  
    + One record for each of the values  
+ Example: `SELECT * FROM (FLATTEN ([dataset.table], city))`  
  
### Lab 7.2  
  
BigQuery will automatically flatten a single repeated field (in this case, "city").  
Additional (independent) repeated fields in a query each require the use of the FLATTEN statement.  
A query on 5 independently repeating fields will require 4 FLATTEN statements.  
  
  
## Nested Repeated Fields  
  
"type": "RECORD"  
"mode": "REPEATED"  
  
+ BigQuery supports importing and exporting nested repeated fields in JSON and AVRO files  
+ Combine nested and repeated fields to denormalize a *one-to-many* relationship  
+ Useful as a mechanism to organize related information  
  
### Example: JSON Nested Repeated Schema  
  
```  
{"name": "author", "type": "string", "mode": "REQUIRED"},  
{"name": "book", "type": "RECORD", "mode": "REPEATED", "fields":  
    [  
        {"name": "title", "type": "string", "mode": "REQUIRED"},  
        {"name": "checked_out", "type": "timestamp", "mode": "REPEATED"}  
    ]  
},  
{"name": "citiesLived", "type": "RECORD", "mode": "REPEATED", "fields":  
    [  
        {"name": "place", "type": "string"},  
        {"name": "yearsLived", "type": "integer", "mode": "REPEATED"}  
    ]  
}  
```  
  
### Example: JSON Nested Repeated Data  
  
```  
{"author": "melville", "book": [{"title": "Moby Dick", "checked_out": ["2014-12-12 14:23", "2013-04-03 12:13"]}], "citiesLived": [{"place": "Denver, CO", "yearsLived" :["1986", "1987"]}]}  
{"author": "hardy", "book": [ {"title": "Return of the Native", "checked_out": ["1984-05-30 12:12", "1986-03-12 00:00", "1992-05-03 04:32"] }, {"title": "The Mayor of Casterbridge", "checked_out": ["1983-06-23 12:12", "1986-03-12 00:00", "1992-05-03 04:32"] } ], "citiesLived": [ {"place": "Austin, TX", "yearsLived" : ["1982", "1983", "1984"] }, {"place": "Dublin, CA", "yearsLived" : ["1992", "1999", "2000"]}]}  
{"author": "koontz", "book": [ {"title": "Velocity", "checked_out": ["1990-06-10 12:10", "2000-03-11 10:00", "1992-05-03 04:32"] }, {"title": "Intensity", "checked_out": ["2003-06-23 02:12", "2004-03-12 20:00", "1992-05-03 04:32"]}]}  
```  
  
### Querying Nested Repeated Fields  
  
+ A query such as `SELECT * ...` produces an error:  
    + Cannot output multiple independently repeated fields at the same time  
+ Example: `SELECT author, book.title, book.checked_out FROM [dataset.table]`  
  
  
### Using the WITHIN Keyword  
  
+ WITHIN keyword works with aggregate functions  
+ Example:  
    + `SELECT fullName, COUNT(children.name) WITHIN RECORD FROM [dataset.tableId]`  
+ `WITHIN RECORD`  
    + Aggregates data in the repeated values within the record  
+ `WITHIN <node>`  
    + Aggregates data in the repeated values within a node  
+ Example:  
    + `SELECT fullName, count(citiesLived.place) WITHIN RECORD, citiesLived.place, count(citiesLived.yearsLived) WITHIN citiesLived FROM [dataset.tableId]`  
  
要瞭解 Record 的結構層級，才能比較有效的使用 Within。  
  
### Lab 7.3  
  
使用 `REAPETED` and `NETSTED` Record 的時候，  
仍然要注意只能同時有一個 REAPETED field，  
否則就得使用 `FLATTEN`  
  
---  
  
# Module 8: Query Performance  
  
## JOIN and GROUP BY – How They Affect Performance  
  
### JOIN  
  
+ When possible, avoid CROSS JOIN  
+ Each row from first table is joined to every row in second table returning large amounts of data  
+ May result in “resources exceeded” errors  
+ Window functions often more efficient  
    + 例如：一個小時做一個 window  
+ The 8MB right-side table join limit no longer applies.  
  
### GROUP BY  
  
+ Use `GROUP BY` when the number of distinct groups is small (low cardinality)  
    + Aggregation of data performed in shards  
    + Low cardinality means shards do not shuffle data  
    + High performance  
+ Large `GROUP BY` is less optimal  
    + 建議不要做，但如果不得已的話還是可以做啦。  
    + High cardinality requires aggregation performed by multiple shards  
    + Shards produce hash key for each value and shuffle data  
  
### ROLLUP - Legacy SQL  
  
+ Use `ROLLUP` function in legacy SQL for large GROUP BY  
+ Adds extra rows to result that represent partial aggregations  
+ The fields in the GROUP BY must be in the SELECT (declares which columns to process).  
  
```bigquery  
SELECT  
    year,  
    is_male,  
    COUNT(1) AS COUNT  
FROM  
    publicdata:samples.natality  
WHERE  
    year >= 2000 AND year <=2002  
GROUP BY  
    ROLLUP(year, is_male)  
ORDER BY  
    year, is_male  
```  
  
```  
+------+---------+----------+  
| year | is_male | count    |  
+------+---------+----------+  
| NULL | NULL    | 12122730 |  
| 2000 | NULL    | 4063823  |  
| 2000 | false   | 1984255  |  
| 2000 | true    | 2079568  |  
| 2001 | NULL    | 4031531  |  
| 2001 | false   | 1970770  |  
| ...                       |  
| 2002 | true    | 2060857  |  
+------+---------+----------+  
```  
  
### Example: Large GROUP BY  
  
```  
SELECT  
    LogEdits,  
    COUNT(contributor_id) Contributors  
FROM (  
    SELECT  
        contributor_id,  
        INTEGER(LOG10(COUNT(*))) LogEdits  
    FROM  
        [publicdata:samples.wikipedia]  
    GROUP BY contributor_id  
)  
GROUP BY LogEdits  
ORDER BY LogEdits DESC  
```  
  
## Table Decorators  
  
### BigQuery Table Decorators  
  
只有要查有異動的資料的話，使用 Decorators 就好，可以節省資料量。  
不過 7 天之內要做，因為只會保留 7 天。  
  
+ Use to perform the most cost-effective query of a subset of your data  
+ Table decorators can be used whenever a table is read  
+ Copying a table, exporting a table, or listing data  
+ Can also be used to undelete a table within 2 days on a best-effort basis  
+ Currently supported in legacy SQL only  
  
### Table Decorator Types  
  
+ Snapshot decorators  
    + `@<time>`  
    + Time must be within last 7 days  
    + `@0` references oldest snapshot  
    + Relative time is negative  
    + Absolute time is positive  
+ Range decorators  
    + `@<time 1>-<time 2>`  
    + Time must be within last 7 days  
    + References data between `<time 1>` and `<time 2>`  
    + Time 2 is optional and defaults to ‘now’  
  
### Example: Snapshot Table Decorator  
  
+ <http://blog.gdeltproject.org/using-bigquery-table-decorators-to-lower-query-cost/>  
+ `@-14400000` - is a reference to a snapshot of the table at -14400000 milliseconds since the current time  
    + 14400000 milliseconds == 14400 seconds == 4 hours  
  
```  
SELECT count(*)  
FROM [publicdata:samples.shakespe are@-14400000]  
```  
  
  
## Wildcards  
  
### Wildcard Functions - Legacy SQL  
  
+ Cost-effective way to query data from a set of “sharded” tables  
    + Only the tables that match the wildcard are accessed  
    + Limits BigQuery data charges  
+ Equivalent to UNION of tables matched by wildcard  
+ Limits:  
    + *No query can reference more than 1,000 tables (even via views)*  
    + The query planner collects table metadata which can have a performance impact for a large number of shards  
  
#### `TABLE_DATE_RANGE(prefix, timestamp1, timestamp2)`  
  
Queries daily tables that overlap with the time range between `<timestamp1>` and `<timestamp2>`.  
Table names must have the following format: `<prefix><day>`, where `<day>` is in the format YYYYMMDD.  
You can use date and time functions to generate the timestamp parameters.  
For example:  
+ `TIMESTAMP('2012-10-01 02:03:04')`  
+ `DATE_ADD(CURRENT_TIMESTAMP(), -7, 'DAY')`  
  
#### `TABLE_DATE_RANGE_STRICT(prefix, timestamp1, timestamp2)`  
  
This function is equivalent to `TABLE_DATE_RANGE`.  
The only difference is that if any daily table is missing in the sequence,  
`TABLE_DATE_RANGE_STRICT` fails and returns a `Not Found: Table <table_name> error`.  
  
#### `TABLE_QUERY(dataset, expr)`  
  
Queries tables whose names match the supplied expr.  
The expr parameter must be represented as a string and must contain an expression to evaluate.  
For example, `'length(table_id) < 3'`.  
  
#### Wildcard Function Examples  
  
```bigquery  
SELECT ...  
FROM  
    TABLE_DATE_RANGE(  
        dataset.log,  
        TIMESTAMP('2015-01-01'),  
        TIMESTAMP('2015-01-03')  
     )  
```  
  
### Wildcard Tables - Standard SQL  
  
+ Query multiple tables using concise SQL statements  
+ Wildcard table represents union of all tables that match the wildcard expression (like wildcard functions)  
+ Useful when dataset contains multiple, similarly named tables with compatible schemas  
+ Each row in wildcard table contains special column containing value matched by wildcard character  
+ Example:  
    + `FROM bigquery-public-data.noaa_gsod.gsod*`  
        + Matches all tables in noaa_gsod that begin with string 'gsod'  
        + character is required (single, double quotes are invalid)  
+ Longer prefixes generally perform better than shorter prefixes  
    + For example: `.gsod200*` versus `.*`  
  
## Partitions  
  
### Table Partitioning - Current Approach  
  
+ Time-partitioned tables are cost-effective way to manage data, write queries spanning multiple days, months, years  
+ Create tables with time-based partitions and BigQuery automatically loads data in correct partition  
    + Declare the table as partitioned at creation time using `--time_partitioning_type` flag  
    + To create partitioned table with expiration time for data, use `time_partitioning_expiration` flag  
+ To query partitioned table, provide date or range of dates and query processes data for interval specified  
+ Only data scanned is in partitions specified by interval  
+ Queries are more performant, cheaper  
+ Currently only supported by legacy SQL  
  
#### Example - Table Partitioning  
  
```  
SELECT  
    ...  
FROM  
    sales  
WHERE  
    _PARTITIONTIME BETWEEN TIMESTAMP("20160101") AND TIMESTAMP("20160131")  
```  
  
## Query Performance Tips  
  
+ Denormalize tables for performance  
+ Select only needed columns - `Do not use Select *`  
+ Schedule batch queries at off-peak hours using jobs  
+ Use caching when possible  
    + Caching is best effort  
    + If table data changes, cache is invalidated  
    + Use jobs.getQueryResults to page through cached query results in a temporary table (no charge)  
+ Try to use ORDER BY and LIMIT in outermost queries  
    + `LIMIT` is applied to results by Master  
+ Build queries from the inside out by using subqueries  
    + Filter data in subqueries  
    + Perform arithmetic, ordering, case logic in outer query  
+ Use queries to create materialized intermediate tables  
    + Create subset of complex data in destination table  
    + Partially aggregate data in destination table  
+ Move heavyweight filters, such as regexp, to the end  
+ Avoid grouping on unbounded possible values  
    + Example: Web logs with arbitrary GET parameters in the suffix  
+ Consider using IF/CASE instead of self-joins because IF/CASE has lower processing overhead  
    + Self-joins require multiple disk reads  
+ Apply WHERE filters prior to JOINs  
    + Predicate pushdown  
  
---  
  
# Module 9: Troubleshooting Errors  
  
## Error Categories  
  
+ Request encoding errors  
    + Associated with the query request – Invalid query syntax, and so on  
    + Request Body 有錯誤，通常是由 Google 的 API 處理  
+ Application errors  
    + Errors associated in processing the request  
+ HTTP transport layer errors  
    + Programmatic communication errors using API  
  
## Request Encoding Errors  
  
在 Query History 裡頭，  
點開有錯誤的 Query 可以看到 Error code，  
可以點選超連結去察看該 Error 詳細的錯誤原因。  
  
+ Incomplete syntax  
+ Missing or invalid objects  
+ Missing columns in GROUP BY (for aggregations)  
+ Incorrect or missing punctuation  
+ Misspellings  
+ Ambiguous field references  
  
  
## Resource Errors  
  
+ Intended limitations exist in the query execution engine to protect resources  
    + Can cause well-formed queries to fail  
+ Two classes of resource errors  
    + Result too large  
    + Resources exceeded  
  
### Result Too Large  
  
+ BigQuery limits result sets to approximately 128MB compressed  
    + Queries returning larger results cannot fit into response  
+ Result too large:  
    + Commonly thrown on queries that use an ORDER BY with large cardinality  
    + Can happen in multiple stages of the serving tree  
  
#### Handling Result Too Large Errors  
  
+ Use filters to limit the result set  
+ Use LIMIT clause  
+ Remove ORDER BY for large datasets (order by without limit is meaningless)  
+ Specify destination table and use `allowLargeResults` flag  
    + Impacts query performance  
    + 可以保證資料都出得來，但效能會有影響，因為有些前置動作會比較不一樣，可以視需求決定要不要用這個 flag  
+ Limitations of `allowLargeResults` flag  
    + Cannot specify top-level ORDER BY, TOP or LIMIT clause  
        + Negates benefit of allowLargeResults because query output is no longer computed in parallel  
    + Using allowLargeResults flag with ORDER BY can cause resources exceeded errors  
        + Master applies final sorting  
    + Using allowLargeResults with window functions requires PARTITION BY clause  
  
### Resources Exceeded  
  
+ Resources exceeded error issued if a query exceeds the memory limit on a single shard  
    + Once data is read from disk, processing is done in memory  
+ Most common on:  
    + ORDER BY queries with large numbers of distinct values  
    + JOINs with more outputs than inputs  
    + Aggregations that require memory proportional to the number of input values  
    + Queries where data is heavily skewed toward one key value  
  
#### Handling Resources Exceeded Errors  
  
+ If possible, limit use of `ORDER BY`  
+ Use aggregation functions that generate fewer output results than input rows  
+ Avoid JOINs that generate more outputs than inputs  
+ Avoid queries that create data skew  
+ Queries on "guest" IDs or null values  
+ No rule that works for every case  
+ 或者先用一個 Query 把結果存成比較小的 Table (Destination Table)，再拿這個 Table 來 Query  
  
  
## HTTP Errors and Responses  
  
+ All BigQuery API calls are HTTP requests  
+ All HTTP requests return status codes  
+ Codes between 200 and 299 are success codes  
+ HTTP error codes are between 400 and 599  
+ BigQuery returns a standard JSON response on error  
+ 可以參考這個網頁：<https://cloud.google.com/bigquery/troubleshooting-errors>  
  
---  
  
# Module 10: Access Control  
  
## Access Control Lists  
  
從 Dataset 這個層面去做設定  
  
+ ACLs define permissions given to a role (or grantee) for a target (project/dataset)  
+ ACLs consist of one or more entries that grant permission to a role (or grantee)  
+ Permissions define the actions that can be performed against a project or dataset  
    + Scope defines to whom the permission applies  
    + 參考 <https://developers.google.com/apis-explorer/#p/bigquery/v2/>  
+ Roles:  
    + Project roles – Users can run jobs or manage the project  
    + Dataset roles – Define user access to datasets in a project  
  
## Project Roles  
  
+ Granted/revoked using Cloud Platform Console  
+ Roles are assigned by email address for:  
    + Individual users  
    + Groups  
    + Service accounts  
+ Project owners can modify project roles  
    + Automatically granted to project creator  
+ 要授權給一群 Google User 的話，可以考慮用 Google Groups 來做這件事，只要授權給一整個 Group 就行了，不用一個一個加。  
  
### Permissions for Project Roles  
  
+ Viewer  
    + Can start a job - Dataset roles also required depending on job type  
    + List and get all jobs they started  
    + Granted READER dataset role by default for new datasets in project  
+ Editor  
    + Same as Viewer, plus:  
        + Can create new dataset in project  
        + Is granted WRITER role by default for new datasets in project  
+ Owner  
    + Same as Editor, plus:  
        + Can list all datasets in the project  
        + Can delete any dataset in the project  
        + Can list and get all jobs run  
  
## Dataset Roles  
  
+ The project ACL becomes default ACL for datasets in the project  
    + Default access can be overridden on a per-dataset basis  
    + Tables inherit ACLs from dataset  
        + ACLs cannot be configured on tables  
+ Dataset ACLs allow resource separation  
    + No need for additional clusters and data duplication  
    + Saves money, simplifies operations  
+ Dataset roles are granted or revoked using:  
    + The BigQuery web UI  
    + Using the 'Share dataset' option  
    + The BigQuery API  
    + Using Datasets:`update`  
+ Roles are assigned by email address to:  
    + Single user  
    + Google Groups  
    + Predefined group of users, such as all users, or a group of users with same project role  
  
### Permissions for Dataset Roles  
  
+ Reader  
    + Can read, query, copy or export tables in the dataset  
        + Can call get on the dataset and tables in dataset  
        + Can call list on table data for tables in the dataset  
+ Writer  
    + Same as READER, plus:  
        + Can edit or append data in the dataset  
            + Can call insert, insertAll, update or delete  
            + Can use tables in the dataset as destinations for load, copy or query jobs  
+ Owner  
    + Same as WRITER, plus:  
        + Can call update on the dataset  
        + Can call delete on the dataset  
    + Note: A dataset must have at least one entity with the OWNER role.  
  
  
## Applying Views for Row-Level Security  
  
### Row-Level Security  
  
+ Not natively supported  
    + Define a view to give access to a specific view of the data  
+ View – a BigQuery SQL query that limits the rows and columns (a virtual table) that a user can see  
+ BigQuery views are re-executed every time the view is queried  
+ Create view in dataset separate from underlying table’s dataset and assign ACLs to both datasets  
+ Row-Leve Security Scenario  
    + 可以透過 View 來 select 只想被 share 出去的欄位，不需要開放整個 table 的權限。  
    + 從一個使用者 A 沒有權限的 dataset 把一個 View 存到使用者 A 有權限的 dataset，使用者 A 仍然無法使用該 View 得到他沒有權限的 dataset 的資料。  
  
## Identity and Access Management  
  
### Benefits of IAM for BigQuery  
  
+ Admins can isolate permissions to BigQuery  
    + For example, BigQuery roles have no authority to manage Compute Engine virtual machines  
+ Consistent IAM controls across all GCP products  
+ Narrow permissions allow more fine-grained control  
+ Backwards compatible  
    + Legacy project permissions are preserved, and the familiar UI, API, and CLI will continue to work as before with minimal changes  
  
### Organization Node (Beta)  
  
+ Organization node is root node for Google Cloud resources  
+ 2 organization roles:  
    + Organization Admin - Control over all cloud resources  
    + Project Creator - Controls project creation  
  
### IAM Resource Hierarchy  
  
+ A policy is set on a resource  
    + Each policy contains: Set of roles, role members  
+ Resources inherit policies from parent  
    + Resource policies are a union of parent and resource  
+ If parent policy less restrictive, overrides more restrictive resource policy  
  
### IAM Roles - Curated Roles  
  
The “can do what” part is defined by an IAM role.  
An IAM role is a collection of permissions.  
Most of the time to do any meaningful operations you need more than 1 permission.  
For example to manage instances in a project, you need to create, delete, start, stop and change an instance.  
So the permissions are grouped together into a role to make it easier to manage.  
  
### BigQuery IAM Roles  
  
+ User  
    + Runs jobs such as queries  
    + Can browse the project to see what data is available, but does not have access to it by default  
    + Can be assigned at project level or higher  
+ Admin  
    + All BigQuery related permissions - Access to read, write, delete all data, view jobs and/or cancel them  
    + Can be assigned at project level or higher  
+ Data viewer  
    + Can view all datasets and all data within those datasets within the scope of the role  
    + Can be assigned at dataset level or higher  
+ Data editor  
    + Can edit all datasets and all data within those datasets within the scope of the role  
    + Can be assigned at dataset level or higher  
  
---  
  
# Module 11: Exporting Data  
  
## Exporting Data  
  
+ Why export data?  
    + Using data with third-party tools  
    + Snapshots  
    + Backups  
+ Export using:  
    + Web UI  
    + CLI  
    + REST API  
+ Limitations  
    + Export up to 1 GB of data per file (multiple file export supported)  
    + Daily limit: 1,000 exports per day, up to 10 TB  
+ ACL requirements for exporting data:  
    + BigQuery: Dataset-level READER access  
    + Google Cloud Storage: WRITE access to Google Cloud Storage bucket(s)  
  
### Export Configuration Options  
  
+ Two aspects: Format and compression  
    + destinationFormat  
        + CSV  
        + JSON  
        + Avro  
    + compression  
        + GZIP  
        + NONE  
+ Notes:  
    + AVRO cannot be used with GZIP compression  
    + Nested and repeated data cannot be exported in CSV format  
    + Defaults: CSV with no compression  
  
### AVRO Export Format  
  
+ Exported files are Avro container files  
+ Each row is represented as an Avro record  
    + Nested data is represented by nested record objects  
+ *REQUIRED* fields represented as corresponding Avro types  
    + For example: An INTEGER type maps to an Avro LONG type  
+ *NULLABLE* fields represented as Avro Union of corresponding type and "null"  
+ *REPEATED* fields are represented as Avro arrays  
+ *TIMESTAMP* data types represented as Avro LONG types  
  
  
## Running Export Jobs  
  
### CLI  
  
+ `bq extract` - Perform an extract operation against `source_table` into `destination_uris`  
    + `bq extract <source_table> <destination_uris>`  
  
### Web UI  
  
+ 操作很簡單  
+ 有很大的檔案的話，儘量不要用 WebUI export，因為有可能中間被中斷就得重下載。請丟到 GCS 再去 download 下來  
  
### Configuration Example  
  
```JSON  
jobData = {  
    'projectId': projectId,  
    'configuration': {  
        'extract': {  
            'sourceTable': {  
                'projectId': projectId,  
                'datasetId': datasetId,  
                'tableId': tableId  
            },  
            'destinationUris': ['gs://<bucket>/<file>'],  
            'destinationFormat': 'NEWLINE_DELIMITED_JSON'  
        } ...  
```  
  
  
## Wildcard Exports  
  
+ If export is larger than 1GB, use a wildcard to partition the output into multiple files  
+ Include a glob character (`*`) in export file name  
    + Glob is replaced by shard value of 12 digits  
    + Starts with 000000000000 and increments by 1 for each file  
+ Wildcard exports are written in parallel  
    + Target files are smaller and parallel writers work on separate patterns immediately  
+ Wildcard exports are subject to quota limitations  
  
### Single & Multiple Wildcard URI  
  
+ Single Wildcard URI  
    + `'destinationUris': ['gs://my-bucket/file-name-*.json']`  
+ Multiple Wildcard URI  
    + `'destinationUris': ['gs://my-bucket/file-name-1-*.json', 'gs://my-bucket/file-name-2-*.json']`  
+ `destinationUris` property indicates export location(s) and file name(s)  
+ Data sharded into multiple files based on the pattern  
  
  
---  
  
# Module 12: Interfacing with External Tools  
  
## Interfacing with Spreadsheets  
  
### BigQuery Connector for Microsoft Excel  
  
+ Supports Excel 2007 and up  
+ Supports Windows and Mac  
+ Access through authorization key  
    + Time sensitive  
    + Min 1 hour – Max 30 days  
    + Key can be revoked  
+ Go to https://bigquery-connector.appspot.com  
+ Select Google account to use  
+ Record unique key and download IQY file  
+ Follow site instructions to execute query from Excel  
+ <https://cloud.google.com/bigquery/docs/bigquery-connector-for-excel>  
    + <https://bigquery-connector.appspot.com>  
  
### Using Google Sheets with BigQuery  
  
Although spreadsheet are not designed to handle big data, many business run on them and use them daily.  
Spreadsheets are understandable by both technical and non-technical staff.  
Spreadsheets allow for use of simple charts and graphs to be easily built.  
You could also connect to BigQuery from Excel via an ODBC connector.  
  
+ Extend Google Sheets using App Script  
+ Rich interface  
+ JavaScript-based language  
    + Create buttons, pulldowns, and so on  
    + Create dynamic query parameters  
    + Create visualizations  
+ OWOX BigQuery Reports Add-On  
    + Save queries with preset variables  
    + Create visualizations  
    + Share results  
+ Alternative to writing scripts  
+ Free version available  
  
## ODBC & JDBC Drivers  
  
### Simba ODBC/JDBC Drivers (Beta)  
  
+ Simba ODBC/JDBC Drivers 32-bit and 64-bit Available for Mac, Linux, Windows  
+ Supports ANSI SQL-92: SELECT, JOIN, WHERE, HAVING, GROUP  
+ BY, ORDER BY, TOP and most SQL-92 scalar and aggregate functions  
+ Supports BigQuery’s SQL subset: SELECT, HAVING, WHERE, GROUP BY, ORDER BY, LIMIT, CASE and all functions  
+ Supports all BigQuery data types (STRING, INTEGER, FLOAT, BOOLEAN, TIMESTAMP)  
  
Google has partnered with Simba Technologies to provide updated ODBC and JDBC drivers that leverage the power of BigQuery's Standard SQL (support is also provided for legacy SQL).  
For more information on the Simba ODBC/JDBC drivers for BigQuery, see: <https://cloud.google.com/bigquery/partners/simba-beta-drivers>.  
  
### Other JDBC Drivers  
  
還不 support insert 和 delete  
  
+ Starschema JDBC driver for BigQuery  
    + Supports server and OAuth2 authentication  
    + Supports handling metadata  
    + Query transformation capabilities  
    + Released to open source - No longer under active development  
+ CData JDBC driver for BigQuery  
    + <http://www.cdata.com/drivers/bigquery/>  
    + Abstracts BigQuery data source into tables, views, stored procedures use to access data  
    + 要用的時候要跟 Google 拿金鑰放在 JDBS 的 Driver 裏面  
  
Although the Starschema driver is available, no active work has been done since June 2013.  
This means that any enhancements to BigQuery may not be reflected in the driver.  
  
  
## Encrypted BigQuery Client  
  
### Encrypted Client  
  
`ebq` commnad  
<https://github.com/google/encrypted-bigquery-client>  
<https://github.com/google/encrypted-bigquery-client/blob/master/tutorial.md>  
  
+ An experimental extension to the BigQuery client  
+ Offers client-side encryption for a subset of query types  
+ Implemented in Python  
+ Encrypts data before loading and transforms query to work on top of encrypted data  
+ Only available as a replacement for bq CLI  
+ Supports multiple encryption modes  
    + `Pseudonym`  
        + encrypts the data the same way, given a particular key  
    + `Probabilistic`  
        + encrypts the same text differently every time  
    + `Homomorphic`  
        + Encrypts numeric fields with special mathematical properties allowing mathematical operations on encrypted data to yield encrypted results  
    + `Searchwords`  
        + Encrypts data so you can find a particular word within a longer string  
        + same word is encrypted the same way every time  
    + `Probabilistic_searchwords`  
        + combines the two types of encryption so that a word in encrypted a different way every time  
    + `None`  
        + No encryption  
  
### Client Interaction  
  
+ Normal client interaction  
    + Data on client in normal (unencrypted) state  
    + Data moves between client and BigQuery over SSH  
    + Data is encrypted in flight and at rest once in BigQuery  
+ Encrypted client interaction  
    + Interface encrypts input data on client  
    + Encrypted data moves between client and BigQuery over SSH  
    + Data encrypted in flight and at rest once in BigQuery  
    + Query results to client are encrypted  
    + Client interface decrypts the results  
  
  
## BigQuery and R  
  
+ Environment for statistical computing  
+ Contains large, integrated collection of data analysis tools  
+ Graphical facilities  
+ Simple and effective programming language  
+ BigQuery added as extension package  
+ BigQuery allows R to process very large datasets  
+ Hundreds of modeling packages available  
+ R provides very sophisticated analysis  
+ Easy setup and use  
  
---  
  
# Module 13: Working with Google Analytics Premium Data  
  
---  
  
# Module 14: Data Visualization  
  
+ <https://www.google.com/analytics/data-studio/>  
  
## Third-party tools  
  
+ BigQuery integrates with several open-source/commercial tools  
    + Tableau, Qlik, iCharts  
    + See [third-party tools and services](https://cloud.google.com/bigquery/third-party-tools)  
+ All tools provide report, dashboard creation capability  
+ Vendor offerings may be cloud-based, client-based, both  
+ Each tool may have a different underlying proprietary technology  
  
## Spreadsheet Visualization  
  
+ Cost-effective option  
+ Limited in business intelligence functionality  
+ Visualization capabilities may not be as robust as a business intelligence tool  
    + May require additional scripting  
    + 搭配 Google App Script 使用  
+ Use third-party application or ODBC driver  
    + BigQuery Connector for Microsoft Excel  
    + Simba ODBC Driver  
  
## Datalab  
  
+ <https://cloud.google.com/datalab/docs/quickstarts/>  
  
### Use Datalab on Google Cloud Shell  
  
好像只要直接在 Cloud Shell 用[在 local 用 docker 執行 datalab 的方法](https://cloud.google.com/datalab/docs/quickstarts/quickstart-local)就行了  
`docker run -it -p "127.0.0.1:8081:8080" -v "${HOME}:/content" -e "PROJECT_ID=${PROJECT_ID}" gcr.io/cloud-datalab/datalab:local`  
  
不需要用到 <https://cloud.google.com/datalab/docs/quickstarts/quickstart-gcp>  
`docker run -it -p "127.0.0.1:8081:8080" -v "${HOME}:/content" -e "GATEWAY_VM=project-id/zone/instance-name" gcr.io/cloud-datalab/datalab:local`  
因為用這個方法似乎還得額外開一台 VM。  
  
在 Cloud Shell 輸入  
`docker run -it -p "127.0.0.1:8081:8080" -v "${HOME}:/content" -e "PROJECT_ID=${DEVSHELL_PROJECT_ID}" gcr.io/cloud-datalab/datalab:local`  
(好像有些 Cloud Shell 不知道為何會沒有 `$DEVSHELL_PROJECT_ID`，沒有的話就手動輸入吧)  
好了之後再點選左上角第一個 Web preview，選擇 Change port 8081，應該就會開啟一個連到剛剛建立的 datalab 的分頁了  
  
---  
  
# BigQuery Public datasets  
  
+ <http://www.gdeltproject.org/data.html#googlebigquery>  
    + <http://nyctaximap.appspot.com/>  
+ <https://www.reddit.com/r/bigquery/>  
+ <https://cloud.google.com/bigquery/public-data/>  
