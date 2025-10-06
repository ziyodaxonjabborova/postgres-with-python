from psycopg2 import connect
from datetime import datetime

db=connect(
    host='localhost',
    port='5432',
    user='postgres',
    password='13202010',
    database='info'
)

dbc=db.cursor()


dbc.execute(f"select MIN({datetime.now().year}-year) from students")
min_age=dbc.fetchall()

dbc.execute(f"select name from students where {datetime.now().year}-year={min_age[0][0]} ")
min_student=dbc.fetchall()





print(f"Eng kichik yoshdagi talaba(lar): ")
for i in  min_student:
    print(i[0])



dbc.close()
db.close()
