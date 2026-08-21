# print("hello world")


import mysql.connector
mydb=mysql.connector.connect(username="root",host="127.0.0.1",password="root@123",database="mayank_testdb")
print(mydb)

mycursor=mydb.cursor()

# mycursor.execute("show databases")
# print(mycursor)
#
#
# data = mycursor.fetchall()
# print(data)
#
# for i in data:
#     print(i)

# mycursor.execute("CREATE DATABASE mayank_testdb")

# mycursor.execute("create table student (id int, name varchar(25))")


# mycursor.execute("show tables")
# data = mycursor.fetchall()
# print(data)
#
# mycursor.execute("insert into student value(101,'mayank')")
#
# mydb.commit()


# mycursor.execute("select * from student")
# data = mycursor.fetchall()
# print(data)


# mycursor.execute("insert into student values(102,'sawan'),(103,'yash'),(104,'jayant'),(105,'shubham')")
#
# mydb.commit()
#
# mycursor.execute("select * from student")
# data = mycursor.fetchall()
# print(data)

# mycursor.execute("select id from student where name='mayank' or name='sawan'")
# data=mycursor.fetchall()
# print(data)

# mycursor.execute("select * from student limit 2")
# data=mycursor.fetchall()
# print(data)

# mycursor.execute("select * from student limit 2  offset 2")
# data=mycursor.fetchall()
# print(data)

# mycursor.execute("select * from student order by name")
# data=mycursor.fetchall()
# print(data)