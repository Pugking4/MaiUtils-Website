from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# Create a SQLite database engine
engine = create_engine('sqlite:///test.sqlite3')

# Create a session factory
Session = sessionmaker(bind=engine)

# Create a base class for declarative models
Base = declarative_base()

# Define a model for the data
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)

# Create the table in the database
Base.metadata.create_all(engine)

# Insert data into the table
session = Session()
user1 = User(name='Alice', age=25)
user2 = User(name='Bob', age=30)
session.add(user1)
session.add(user2)
session.commit()

# Query the data
users = session.query(User).all()
for user in users:
    print(user.name, user.age)
