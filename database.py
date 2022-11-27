import psycopg2

with open('logindb.txt') as file_object:
    user = file_object.readline().strip()
    password = file_object.readline().strip()
    host = file_object.readline().strip()
    port = file_object.readline().strip()
    database = file_object.readline().strip()

connection = psycopg2.connect(user=user,
                              password=password,
                              host=host,
                              port=port,
                              database=database)

def create_table_users():
    with connection.cursor() as cursor:
        cursor.execute("""CREATE TABLE IF NOT EXISTS sent_users(
                       id SERIAL NOT NULL PRIMARY KEY,
                       user_id VARCHAR(15) NOT NULL,
                       profile_id VARCHAR(15) NOT NULL);"""
                       )
    connection.commit()

def add_in_table(user_id, profile_id):
    with connection.cursor() as cursor:
        cursor.execute(f"""INSERT INTO sent_users (user_id, profile_id)
                       VALUES ('{user_id}', '{profile_id}');"""
                       )
    connection.commit()

def select_of_table(user_id, profile_id):
    with connection.cursor() as cursor:
        cursor.execute(f"""SELECT user_id, profile_id FROM sent_users
                       WHERE user_id = '{user_id}' and profile_id = '{profile_id}' """)
        result_select = cursor.fetchall()
    connection.commit()
    return result_select
