import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd = "FlavorTown281195!",
    database = 'testdb'
)

mycursor = mydb.cursor(buffered = True)

# mycursor.execute("CREATE DATABASE testdb")

# mycursor.execute("CREATE TABLE users (ID INTEGER PRIMARY KEY AUTO_INCREMENT, name VARCHAR(255), password VARCHAR(255), email VARCHAR(255))")

# Q2 = "CREATE TABLE Images (userId int PRIMARY KEY, FOREIGN KEY (userID) REFERENCES users(ID))"

# email = 'byronfry95@icloud.com'
# params = [email]
# mycursor.execute('SELECT * FROM users WHERE email = %s ', params)

# for x in mycursor:
#     print(x)
# mycursor = mydb.cursor()
#         mycursor.execute("SELECT * FROM users WHERE ID = %s", [id])
#         result = mycursor.fetchall()
#         user = User(id = result[0][0], email = result[0][3], name = result[0][1], password = result[0][2])
#         return user

# mycursor = mydb.cursor()
#         params = [Email]
#         mycursor.execute("SELECT * FROM users WHERE email = %s", params)
#         result = mycursor.fetchall()

# mycursor.execute("INSERT INTO users (name, password, email) VALUES (%s, %s, %s)", (name, password, Email))
#             mydb.commit()
#             mycursor.execute("SELECT * FROM users WHERE email = %s", params)
#             result = mycursor.fetchall()
#             print(result)
#             user = User(id = result[0][0], email = Email, name = name, password = password)
#             login_user(user, remember=True)
#             mycursor.close()