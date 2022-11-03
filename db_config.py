import os

# from dotenv import load_dotenv

import psycopg2
import psycopg2.extras

# load_dotenv()

user_name = os.environ.get('PSQL_USER_NAME')
password = os.environ.get('PSQL_PASSWORD')
host = os.environ.get('PSQL_HOST')
database_name = os.environ.get('PSQL_DB_NAME')


def main():
    try:

        connect_str = "postgresql://{user_name}:{password}@{host}/{database_name}".format(
            user_name=user_name,
            password=password,
            host=host,
            database_name=database_name
        )
        print("Connection string: " + connect_str)

        connection = psycopg2.connect(connect_str)

        connection.autocommit = True

        with connection.cursor() as cursor:
            cursor.execute(
                "SELECT version();"
            )
            print(f"Server version: {cursor.fetchone()}")

    except psycopg2.DatabaseError as exception:
        print(exception)

    finally:
        if 'connection' in locals():
            connection.close()



