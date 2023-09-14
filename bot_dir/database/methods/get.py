from database.main import connection
from psycopg2 import Error


def select_tables():
    try:
        with connection.cursor() as cursor:
            query = '''
                 SELECT *
                    FROM main_app_user
         '''
            cursor.execute(query)
            user_info = cursor.fetchone()

            return user_info

    except (Exception, Error) as error:
        print(error)
