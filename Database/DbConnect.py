import psycopg2


def get_connection():

    conn = psycopg2.connect("dbname=priya user=postgres password=0000")
    return conn
