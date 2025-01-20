import pymysql
import time
import env
import clickhouse_connect

class TimedCursor(pymysql.cursors.DictCursor):
    def execute(self, query, args=None):
        start_time = time.time()
        super().execute(query, args)
        end_time = time.time()
        print(f"Mysql:      Query executed in {end_time - start_time:.4f} seconds")
        return end_time-start_time
    
class TimedClickHouseClientCursor():
    def __init__(self):
        self.client = clickhouse_connect.get_client(
            host=env.DB_CLICKHOUSE_HOST,
            username="default",
            password='',
            database='default',
            port=8123
        )

    def query(self, q, args=None):
        start_time = time.time()
        self.client.query(q, args)
        end_time = time.time()
        print(f"ClickHouse: Query executed in {end_time - start_time:.4f} seconds")
        return end_time-start_time
    
    def close(self):
        self.client.close()        

def create_mysql_connection():
    connection = pymysql.connect(
        host= env.DB_HOST,
        user= env.DB_USER,
        password= env.DB_PASS,
        database= env.DB_NAME,
        cursorclass=TimedCursor
    )
    return connection, connection.cursor(TimedCursor)

def create_clickhouse_client():
    return TimedClickHouseClientCursor()
