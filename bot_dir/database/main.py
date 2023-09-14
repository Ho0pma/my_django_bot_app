import psycopg2

connection = psycopg2.connect(
    database='django_bot_db',
    user='user',
    password='pass',
    host='db',
    port='5432'
)

print("Database opened successfully")


