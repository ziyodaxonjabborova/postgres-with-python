from psycopg2 import connect

db=connect(
    host='localhost',
    port='5432',
    user='postgres',
    password='13202010',
    database='info'
)

dbc=db.cursor()


dbc.execute("SELECT address FROM users WHERE email LIKE '%@gmail.com'")
data=dbc.fetchall()


print("Emaili “@gmail.com” bo'lgan userlarni manzillari:")
for i in data:
    print(i)




dbc.close()
db.close()
