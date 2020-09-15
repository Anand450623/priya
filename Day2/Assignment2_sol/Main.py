from Assignment2.Utils import read_file_contents
from Assignment2.DbConnect import get_connection


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
