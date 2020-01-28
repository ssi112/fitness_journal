from flask import Flask, render_template

app = Flask(__name__)

# --------------------------------------------------
from models import Base, Customers
import connection
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy import exc # exception

# Create an engine that stores data in the local db file
engine = create_engine('postgresql://ssi112:madHatter!99@localhost:5432/fitness_log')

# Create an engine that stores data in the local db file
# engine = create_engine('postgresql://USER:PW@localhost:5432//fitness_log')
try:
    engine = create_engine(connection.db_connect)
    print("*** Fitness Journal: Inside routes.py ***")
    print(connection.db_connect)
except exc.SQLAlchemyError:
    print("\n *** Oh crap. Something went wrong! *** \n")

# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind = engine)
session = DBSession()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

if __name__ == "__main__":
    app.run(debug=True)


