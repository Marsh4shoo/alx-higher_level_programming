#!/usr/bin/python3
"""
Retrieves and displays the first State object from the database hbtn_0e_6_usa
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

def display_first_state(username, password, database_name):
    try:
        engine = create_engine(
            f'mysql+mysqldb://{username}:{password}@localhost/{database_name}',
            pool_pre_ping=True
        )
        Session = sessionmaker(bind=engine)
        session = Session()

        # Retrieve and display the first State object
        first_state = session.query(State).order_by(State.id).first()
        if first_state:
            print(f"{first_state.id}: {first_state.name}")
        else:
            print("Nothing")

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

    display_first_state(username, password, database_name)

