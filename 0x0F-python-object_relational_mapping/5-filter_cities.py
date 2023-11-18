#!/usr/bin/python3
"""
Retrieves and lists all cities of a specific state from the database
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
        state_name = sys.argv[4]
        query = f"SELECT cities.id, cities.name, states.name " \
                f"FROM cities JOIN states ON cities.state_id = states.id " \
                f"WHERE states.name = '{state_name}';"
        cur.execute(query)
        cities = cur.fetchall()

        city_names = [city[1] for city in cities]
        print(", ".join(city_names))

        db.close()
    except MySQLdb.Error as e:
        print(f"Error accessing the database: {e}")
        sys.exit(1)

