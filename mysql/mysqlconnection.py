from flask.ext.sqlalchemy import SQLAlchemy
from sqlalchemy.sql import text

class MySQLConnection(object):
    def __init__(self, app, db):
        config = {
                'host' : 'manjaro-mysql',
                'database' : db,
                'user' : 'root',
                'password' : 'password',
                'port' : '3306'
        }
        DATABASE_URI = "mysql://{}:{}@{}:{}/{}".format(config['user'],config['password'],config['host'],config['port'],config['database'])
        app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URI
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
        #actually connect app to db
        self.db = SQLAlchemy(app)
        # this is the method we will use to query the database
    def query_db(self, query, data=None):
        result = self.db.session.execute(text(query), data)
        if query[0:6].lower() == 'select':
            # if the query was a select
            # convert the result to a list of dictionaries
            list_result = [dict(r) for r in result]
            # return the results as a list of dictionaries
            return list_result
        elif query[0:6].lower() == 'insert':
            # if the query was an insert, return the id of the
            # commit changes
            self.db.session.commit()
            # row that was inserted
            return result.lastrowid
        else:
            # if the query was an update or delete, return nothing and commit changes
            self.db.session.commit()

# This is the module method to be called by the user in server.py. Make sure to provide the db name!
def MySQLConnector(app, db):
    return MySQLConnection(app, db)
