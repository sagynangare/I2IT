import sqlite3
con=sqlite3.connect('I2it.db')
c=con.cursor()
def create_table():
    c.execute("create table students (Id int, Name text,\
              Marks float, Year int)")
#create_table()
def insert_data():
    c.execute('insert into students (Id, Name, Marks, Year)\
            values(1, "Pandas", 87.98, 4)')
    con.commit()
    con.close()
#insert_data()
def read_data():
    c.execute("select * from students")
    print(c.fetchall())
#read_data()
def update_table():
    c.execute("update students set Name='Prasad' where Id=2")
    con.commit()
    con.close()
#update_table()
def delete_data():
    c.execute("delete from students where Id=2")
    con.commit()
    con.close()
#delete_data()
















