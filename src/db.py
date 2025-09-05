from sqlalchemy import create_engine

db_path = "sqlite:///db/f1.db"

def get_engine():
    return create_engine(db_path)