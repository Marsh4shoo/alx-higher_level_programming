#!/usr/bin/python3
"""
Updates the name of a State object in the database hbtn_0e_6_usa
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

def update_state_name(username, password, database_name, state_id, new_name):
    try:
        engine = create_engine(
            f'mysql+mysqldb://{username}:{password}@localhost/{database_name}',
            pool_pre_ping=True
        )
        Session = sessionmaker(bind=engine)
        session = Session()

        # Query for the state by ID
        state = session.query(State).filter_by(id=state_id).first()

        if state:
            # Update the state's name
            state.name = new_name
            session.commit()
            print(f"State name updated to: {new_name}")
        else:
            print("State not found")

        session.close()
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 6:
        print("Usage: python3 script.py <username> <password> <database> <state_id> <new_name>")
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]
    state_id = int(sys.argv[4])
    new_name = sys.argv[5]

    update_state_name(username, password, database_name, state_id, new_name)

