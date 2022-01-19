import sqlite3

conn = sqlite3.connect('StudentInfo.db')
c = conn.cursor()

def create_table():
    c.execute('CREATE TABLE studentdata( id INTEGER PRIMARY KEY,fname TEXT,lname TEXT,gender TEXT,grade INTEGER)')

def data_entry():
    c.execute("INSERT INTO studentdata VALUES(101,'Siddhesh','Panchal','M',100)")
    conn.commit()
    c.close()
    conn.close()

def remove():
    c.execute("DROP TABLE studentdata")

def create_table1():
    c.execute('CREATE TABLE student_db( id INTEGER PRIMARY KEY,first_name TEXT,last_name TEXT,gender TEXT,grade INTEGER)')


create_table1()
