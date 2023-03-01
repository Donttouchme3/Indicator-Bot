import sqlite3
# DROP TABLE IF EXISTS Articles;
# DROP TABLE IF EXISTS Category;
DataBase = sqlite3.connect('Indicator.db')
Cursor = DataBase.cursor()
Cursor.executescript('''

CREATE TABLE IF NOT EXISTS Category(
    CategoryId INTEGER PRIMARY KEY AUTOINCREMENT,
    CategoryName TEXT UNIQUE,
    CategoryLink TEXT
);
CREATE TABLE IF NOT EXISTS Articles(
    ArticleId INTEGER PRIMARY KEY AUTOINCREMENT,
    Title TEXT UNIQUE,
    Image TEXT,
    Content VARCHAR(30000),
    Author TEXT,
    CategoryId INTEGER REFERENCES Category(CategoryId)
);
''')
DataBase.commit()
DataBase.close()


DataBase = sqlite3.connect('Indicator.db')
Cursor = DataBase.cursor()
Cursor.execute('''
SELECT * FROM Category;
''')
Cs = Cursor.fetchall()
DataBase.close()
print(Cs)