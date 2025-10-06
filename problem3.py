from psycopg2 import connect

db=connect(
    host='localhost',
    port='5432',
    user='postgres',
    password='13202010',
    database='info'
)

dbc=db.cursor()


dbc.execute("select COUNT(*) from employees")
data=dbc.fetchall()


print(f"Jami xodimlar soni: {data[0][0]}")



dbc.close()
db.close()
