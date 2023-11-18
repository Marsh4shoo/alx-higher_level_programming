#!/usr/bin/python3
"""
Fetches city-state pairs and displays them
from the database hbtn_0e_6_usa
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City

def fetch_city_state_pairs(username, password, database_name):
    try:
        engine = create_engine(
            f'mysql+mysqldb://{username}:{password}@localhost/{database_name}',
            pool_pre_ping=True
        )
        Session = sessionmaker(bind=engine)
        session = Session()

        city_state_pairs = session.query(City, State).filter(City.state_id == State.id)\
            .order_by(City.id).all()

        for city, state in city_state_pairs:
            print(f"{state.name}: ({city.id}) {city.name}")

        session.close()
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python3 script.py <username> <password> <database>")
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]

    fetch_city_state_pairs(username, password, database_name)

