import csv
import os
import mariadb
from sys import exit

print(os.environ.keys())

try:
    conn = mariadb.connect(
        user=os.environ.get("USER"),
        password=os.environ.get("PSWD"),  # сменить
        host=os.environ.get("DB_HOST"),
        port=3306,
        database=os.environ.get("DATABASE")
    )
except mariadb.Error as e:
    print(f"Error connecting to MariaDB Platform: {e}")
    exit(-1)

cur = conn.cursor()
tbl = """CREATE TABLE Users (
id MEDIUMINT NOT NULL AUTO_INCREMENT,
name CHAR(30),
age INT,
PRIMARY KEY (id)
);
"""
try:
    cur.execute(tbl)
except mariadb.Error as e:
    print(e)

with open("data.csv") as f:
    reader = csv.reader(f)
    reader.__next__()
    for row in reader:
        name, age = row[0].split(";")
        #print(name, age)
        sql = f"INSERT INTO Users(name,age) VALUES ('{name}',{int(age)});"
        cur.execute(sql)
        #print(cur.)

conn.commit()
cur.execute("SELECT * FROM Users;")
res = cur.fetchall()
print(*res)

conn.close()
exit(0)
