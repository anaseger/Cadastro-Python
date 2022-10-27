import pymysql
#database connection
connection = pymysql.connect(host="localhost", user="root", passwd="88888888", database="testes", port=3306)
cursor = connection.cursor()

#inserting data to db
def add_text(name,idade):
    cursor.execute("INSERT INTO form(ID, name,idade) VALUES (DEFAULT, %s,%s)", (name,idade))
    connection.commit()
    return 1

def get_data():
    cursor.execute("SELECT * FROM form")
    rows = cursor.fetchall()    
    return rows