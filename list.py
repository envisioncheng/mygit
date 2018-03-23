import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session,sessionmaker


app = Flask(__name__)
POSTGRES = {
    'user': 'postgres',
    'pw': 'test2018',
    'db': 'lecture5',
    'host': 'localhost',
    'port': '5432',
}

app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://%(user)s:\%(pw)s@%(host)s:%(port)s/%(db)s' % POSTGRES

db = SQLAlchemy()
db.init_app(app)

engine = create_engine(os.getenv("SQLALCHEMY_DATABASE_URI"))
db = scoped_sesssion(sessionmaker(bind=engine))

def main():
    flights=db.execute("select * from flights")
    for flight in flights:
        print(f"{flight.origin}")

if __name__ == "__main__":
    main()