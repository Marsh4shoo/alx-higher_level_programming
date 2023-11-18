#!/usr/bin/python3
"""
This script retrieves and displays all states from a specified database.
"""

import MySQLdb
import sys

def fetch_states(username, password, database_name):
    try:
        # Connect to the database
        db = MySQLdb.connect(user=username, passwd=password,
                             db=database_name, port=3306)
        cur = db.cursor()

        # Fetch all states
        cur.execute("SELECT * FROM states;")
        states = cur.fetchall()

        # Display states
        for state in states:
            print(state)

        # Close database connection
        db.close()
    except MySQLdb.Error as e:
        print(f"Error accessing the database: {e}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python3 script.py <username> <password> <database>")
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]

    fetch_states(username, password, database_name)
