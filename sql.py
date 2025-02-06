import sqlite3


##connect sqlite3
connection = sqlite3.connect("student.db")

##create a cursor object to insert record,create table,retrieve 

cursor = connection.cursor()

##create student table

table_info ="""

Create table STUDENT(NAME VARCHAR(25) ,CLASS VARCHAR(25) ,SECTION VARCHAR(25) ,
 MARKS INT);
"""

cursor.execute(table_info)

###insert some more records

cursor.execute('''Insert into STUDENT values('Sanoj','Data science','A','90')''')

cursor.execute('''Insert into STUDENT values('Sam','Design and development','A','100')''')

cursor.execute('''Insert into STUDENT values('jessy','Project Manager','A','90')''')

cursor.execute('''Insert into STUDENT values('Sijo','Devops','A','85')''')


cursor.execute('''Insert into STUDENT values('abc','Cyber Security','A','60')''')


##display all the record


print("the inserted records are ")

data = cursor.execute('''select * from STUDENT''')

for row in data:
    print(row)


####close connection


connection.commit()
connection.close()