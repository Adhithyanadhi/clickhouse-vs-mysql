import db.db as db
import query

def performance_test(query):
    conn, cur = db.create_mysql_connection()
    mysql_time_taken = cur.execute(query)
    cur.fetchall()
    conn.close()

    client = db.create_clickhouse_client()
    clickhouse_timetaken = client.query(query)
    client.close()
    
    print(f"ClickHouse is {(mysql_time_taken - clickhouse_timetaken)/clickhouse_timetaken} faster than Mysql\n")

def main():
    performance_test(query.SUM_OF_CREATED_AT_ACCOUNT)
    performance_test(query.GROUP_BY_OF_CREATED_BY_ACCOUNT)

if __name__ == "__main__":
    main()
