#!/usr/bin/python3
"""
Retrieves and lists all cities along with their respective states from the database
"""
import sys
import MySQLdb

if __name__ == '__main__':
    if len(sys.argv) != 4:
        print("Usage: python3 script.py <username> <password> <database>")
        sys.exit(1)

    try:
        db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2],
                             db=sys.argv[3], port=3306)

        cur = db.cursor()
        query = "SELECT cities.id, cities.name, states.name " \
                "FROM cities JOIN states ON cities.state_id = states.id;"
        cur.execute(query)
        city_state_pairs = cur.fetchall()

        for city_state_pair in city_state_pairs:
            print(city_state_pair)

        db.close()
    except MySQLdb.Error as e:
        print(f"Error accessing the database: {e}")
        sys.exit(1)

