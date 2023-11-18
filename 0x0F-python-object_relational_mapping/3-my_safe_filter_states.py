#!/usr/bin/python3
"""
Displays values in the states table of hbtn_0e_0_usa where name matches the argument.
This script is secure from MySQL injections.
"""
import sys
import MySQLdb

if __name__ == '__main__':
    if len(sys.argv) != 5:
        print("Usage: python3 script.py <username> <password> <database> <state_name>")
        sys.exit(1)

    try:
        db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2],
                             db=sys.argv[3], port=3306)

        cur = db.cursor()
        query = "SELECT * FROM states WHERE name = %s;"
        cur.execute(query, (sys.argv[4],))
        states = cur.fetchall()

        for state in states:
            print(state)

        db.close()
    except MySQLdb.Error as e:
        print(f"Error accessing the database: {e}")
        sys.exit(1)

