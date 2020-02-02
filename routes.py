"""
routes.py - maps URLs to functions

Think it will be necessary to scrap this shit and start over
check out the examples:
https://flask-sqlalchemy.palletsprojects.com/en/2.x/quickstart/#a-minimal-application

"""
from flask import Flask, render_template, request
from forms import SignupForm
# --------------------------------------------------
from models import Base, Customers
import connection
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy import exc # exception

app = Flask(__name__)
# <<<< TEST >>>>
#app.config["SQLALCHEMY_DATABASE_URI"] = (connection.db_connect)
#app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False


app.secret_key = "development-key"

# Create an engine that stores data in the local db file
# engine = create_engine('postgresql://USER:PW@localhost:5432/fitness_log')
try:
    engine = create_engine(connection.db_connect)
    print("*** Fitness Journal: Inside routes.py ***")
    print(connection.db_connect)

    # <<<<< TEST >>>>>
    connection = engine.connect()
    result = connection.execute("SELECT * FROM fitness_log.customers;")
    for row in result:
        print("row:", row['first_name'], row['last_name'], row['birthdate'])
    # <<<<< TEST >>>>>
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

@app.route("/signup", methods=['GET', 'POST'])
def signup():
    form = SignupForm()

    if request.method == "POST":
        if form.validate() == False:
            return render_template('signup.html', form = form)
        else:
            newuser = Customers(form.first_name.data, form.last_name.data, form.birthdate, form.email.data, form.password.data)
            session.add(newuser)
            session.commit()
            return "Success!"
    elif request.method == "GET":
        return render_template("signup.html", form = form)

if __name__ == "__main__":
    app.run(debug=True)


