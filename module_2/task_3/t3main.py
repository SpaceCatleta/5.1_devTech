import database as DB


QUERY = """
SELECT g.name, ct.name FROM category_has_good cg
INNER JOIN category ct
ON ct.id = cg.category_id
INNER JOIN good g
ON g.id = cg.good_id
"""


# получает список всех таблиц в  базе данных
def get_tables():
    DB.open('taskDB.db')
    conn, cursor = DB.get_connection()
    cursor.execute('SELECT name from sqlite_master where type= "table"')
    rows = cursor.fetchall()
    DB.close()
    return [row for row in rows]


# получает данные по заданию
def get_data():
    DB.open('taskDB.db')
    conn, cursor = DB.get_connection()
    cursor.execute(QUERY)
    rows = cursor.fetchall()
    DB.close()
    return [(row[0], row[1]) for row in rows]


# печатает в консоли таблицу
def print_data(head, data):
    column_count = len(head)
    columns_width = []
    for title in head:
        columns_width.append(len(title))

    for line in data:
        for i in range(column_count):
            if columns_width[i] >= len(line[i]):
                columns_width[i] = len(line[i])

    print(columns_width)


# print_data(('good_ame', 'category_name'), get_data())

print(get_tables())
