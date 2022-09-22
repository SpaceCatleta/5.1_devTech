import database as DB


def get_tables():
    DB.open('taskDB.db')
    conn, cursor = DB.get_connection()
    cursor.execute('SELECT name from sqlite_master where type= "table"')
    rows = cursor.fetchall()
    DB.close()
    return [row for row in rows]


DB.open('taskDB.db')

with open('CreationScript.sql') as SQLFile:
    sqlText = SQLFile.read()

tableTexts = sqlText.split('=====\n')
for text in tableTexts:
    DB.cursor.execute(text)
    DB.connection.commit()
    print(text.split('\n')[1])
print('tables created')

DB.close()

print(get_tables())