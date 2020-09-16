from Day2.Assignment1_sol.DbConnect import get_connection
from Day2.Assignment1_sol.Utils import read_json

if __name__ == "__main__":

    json_data = read_json("input.json")
    con = get_connection()
    cur = con.cursor()

    cur.execute("select count(*) from employee")
    data = cur.fetchone()
    print("Number of records before insertion = ", data[0])

    for temp in json_data:
        cur.execute("insert into employee(id, name) values(%s, %s)", (temp['id'], temp['name']))

    cur.execute("select count(*) from employee")
    data = cur.fetchone()
    print("Number of records after insertion = ", data[0])

    con.commit()

    cur.close()
    con.close()
