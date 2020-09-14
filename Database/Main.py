import psycopg2
from Database.DbConnect import get_connection


# Ref: https://www.psycopg.org/docs/usage.html#passing-parameters-to-sql-queries
if __name__ == "__main__":
    # conn = get_connection()
    conn = psycopg2.connect("dbname=priya user=postgres password=0000")
    cur = conn.cursor()

    cur.execute("select count(*) from employee")
    data = cur.fetchone()
    print("Number of records before insertion = ", data[0])

    cur.execute("insert into employee(id, name) values(%s, %s)", (1, "anand"))

    cur.execute("select count(*) from employee")
    data = cur.fetchone()
    print("Number of records after insertion = ", data[0])

    conn.commit()

    cur.close()
    conn.close()
