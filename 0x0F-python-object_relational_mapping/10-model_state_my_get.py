#!/usr/bin/python3
"""
Retrieves and prints the State object with the provided name
from the database hbtn_0e_6_usa
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

def find_state_by_name(username, password, database_name, state_name):
    try:
        engine = create_engine(
            f'mysql+mysqldb://{username}:{password}@localhost/{database_name}',
            pool_pre_ping=True
        )
        Session = sessionmaker(bind=engine)
        session = Session()

        # Query for the state with the provided name
        state = session.query(State).filter_by(name=state_name).first()

        if state:
            print(f"State ID: {state.id}")
        else:
            print("Not found")

        session.close()
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: python3 script.py <username> <password> <database> <state_name>")
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]
    state_name = sys.argv[4]

    find_state_by_name(username, password, database_name, state_name)

