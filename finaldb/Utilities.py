import getpass
from pprint import pformat
from pymongo import MongoClient
from pymongo.errors import OperationFailure
from mongoengine import *
from m_credentials import *


class Utilities:
    """I have several variations on a theme in this project, and each one will need to start up
    with the same MongoDB database.  So I'm putting any sort of random little utilities in here
    as I need them.

    startup - creates the connection and returns the database client."""

    @staticmethod
    def startup():
        print("Prompting for the password.")
        while True:
            password = getpass.getpass('Mongo DB password -->') or m_password
            user_name = input('Database username [cjmzone] -->') or m_user_name
            project = input('Mongo project name [cecs323] -->') or m_project
            hash_name = input('7-character database hash [dp4wxsa] -->') or m_hash_name
            cluster = f"mongodb+srv://{user_name}:{password}@{project}.{hash_name}.mongodb.net/?retryWrites=true&w=majority"
            print(f"Cluster: mongodb+srv://{user_name}:****@{project}.{hash_name}.mongodb.net/?retryWrites=true&w=majority")
            try:
                client = MongoClient(cluster)
                db = client["Demonstration"]
                connect(db="Demonstration", host=cluster)
                client.server_info()  # Test the connection
                return db
            except OperationFailure as OE:
                print(OE)
                print("Error, invalid password. Try again.")