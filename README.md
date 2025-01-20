clone the repo
cd /clickhouse-vs-mysql
docker-compose up --build (make sure you have docker installed and running in the background)
you should see :- 
<img width="571" alt="image" src="https://github.com/user-attachments/assets/0c620641-1203-43c7-86d6-3ba718eb4e14" />

You can add your own queries in query.py for comparison
Modify /db/schema/clickhouse.sql and /db/schema/mysql.sql to support your query
To generate insert queries use prepare_sql.py


