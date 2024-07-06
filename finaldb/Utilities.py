import getpass
from pprint import pformat
from mongoengine import ValidationError, NotUniqueError
from mongoengine.queryset.visitor import Q
from mongoengine.context_managers import switch_db
from pymongo import MongoClient
from pymongo.errors import OperationFailure
from mongoengine import *
import io
from mongoengine.connection import _connections, _connection_settings
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
    

#     @staticmethod
#     def print_exception(thrown_exception: Exception):
#         """
#         Analyze the supplied selection and return a text string that captures what violations of the
#         schema & any uniqueness constraints that caused the input exception.  Note that the structure
#         of the exception returned from MongoEngine is much simpler in structure than the exceptions
#         that we receive from MongoDB, which makes it harder to format the exception message into a
#         human-readable format easily.
#         :param thrown_exception:    The exception that MongoDB threw.
#         :return:                    The formatted text describing the issue(s) in the exception.
#         """
#         # Use StringIO as a buffer to accumulate the output.
#         with io.StringIO() as output:
#             output.write('***************** Start of Exception print *****************\n')
#             output.write(f'The exception is of type: {type(thrown_exception).__name__}\n')
#             # DuplicateKeyError is a subtype of WriteError.  So I have to check for DuplicateKeyError first, and then
#             # NOT check for WriteError to get this to work properly.
#             if isinstance(thrown_exception, NotUniqueError):
#                 """As near as I can see, it looks as though the exception thrown by MongoEngine for a violated uniqueness
#                 constraint only returns the first uniqueness constraint.  So if there are multiple uniqueness constraints
#                 that the user input violates, this function will only report the first one, which could be annoying since
#                 the user will not know until the resubmit their input that clears up the first uniqueness constraint 
#                 violation that there are others."""
#                 error = thrown_exception.args[0]  # get the full text of the error message.
#                 message = error[error.index('index:') + 7:error.index('}')]  # trim off the unwanted parts
#                 index_name = message[:message.index(' ')]
#                 field_list = message[message.index('{') + 2:]  # Extract a string dictionary of the index fields.
#                 fields = []  # The list of fields in the violated uniqueness constraint.
#                 while field_list.find(':') > 0:  # Keep going until we've gotten all of the fields.
#                     field_length = field_list.find(':')
#                     field = field_list[:field_length]
#                     fields.append(field)
#                     # Trim off the latest field and get ready to get the next field name.
#                     if (field_list.find(', ')) > 0:  # at least one more field to report.
#                         field_list = field_list[field_list.find(', ') + 2:]
#                     else:  # signal that we're done.
#                         field_list = ''
#                 output.write(f'Uniqueness constraint violated: {index_name} with fields:\n{fields}')
#             elif isinstance(thrown_exception, ValidationError):
#                 output.write(f'{pformat(thrown_exception.message)}\n')
#                 errors = thrown_exception.errors
#                 for error in errors.keys():
#                     output.write(f'field name: {error} has issue: \n{pformat(errors.get(error))}\n')
#             results = output.getvalue().rstrip()
#         return results


# def check_unique(model, data, unique_fields):
#     """
#     Check if a document with the specified unique fields already exists in the collection.
#     :param model: The MongoEngine document model to check against.
#     :param data: A dictionary containing the data to check.
#     :param unique_fields: A list of fields that must be unique.
#     :return: True if a duplicate exists, False otherwise.
#     """
#     query = Q()
#     for field in unique_fields:
#         query &= Q(**{field: data[field]})
#     return model.objects(query).count() > 0

# def check_all_uniques(model, data):
#     """
#     Check all unique constraints for a given MongoEngine model.
#     :param model: The MongoEngine document model to check against.
#     :param data: A dictionary containing the data to check.
#     :return: A list of violated uniqueness constraints.
#     """
#     unique_constraints = []
#     for index in model._meta['index_specs']:
#         if index.get('unique', False):
#             unique_fields = index['fields']
#             if check_unique(model, data, unique_fields):
#                 unique_constraints.append(unique_fields)
#     return unique_constraints

# def test_try(func, msg):
#     """
#     Attempt to execute a function and handle any MongoDB-related exceptions.
#     :param func: The function to execute.
#     :param msg: A message to display upon success.
#     """
#     try:
#         func()
#         print(msg)
#     except ValidationError as e:
#         print_exception(e)
#     except NotUniqueError as e:
#         print_exception(e)
#     except Exception as e:
#         print_exception(e)