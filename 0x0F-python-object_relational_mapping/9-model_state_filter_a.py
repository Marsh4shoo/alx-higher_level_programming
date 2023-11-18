#!/usr/bin/python3
"""
Retrieves and lists all State objects that contain the letter 'a'
from the database hbtn_0e_6_usa
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

def list_states_with_letter_a(username, password, database_name):
    try:
        engine = create_engine(
            f'mysql+mysqldb://{username}:{password}@localhost/{database_name}',
            pool_pre_ping=True
        )
        Session = sessionmaker(bind=engine)
        session = Session()

        # Query and display State objects containing the letter 'a'
        match = '%a%'
        states_with_a = session.query(State).filter(State.name.like(match)).order_by(State.id)
        for state in states_with_a:
            print(f"{state.id}: {state.name}")

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

    list_states_with_letter_a(username, password, database_name)

