from Day2.Assignment1_sol.DbConnect import get_connection
from Day2.Assignment1_sol.Utils import read_file_contents

if __name__ == "__main__":

    con = get_connection()
    cur = con.cursor()

    for command in read_file_contents("Script.sql"):
        print(f"currently executing command...\n{command}")
        cur.execute(command)
        print("*****************************")

    con.commit()

    cur.close()
    con.close()
