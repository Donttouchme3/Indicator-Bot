import sqlite3


def InsertCategory(CategoryName, CategoryLink):
    DataBase = sqlite3.connect('Indicator.db')
    Cursor = DataBase.cursor()
    Cursor.execute('''
    INSERT OR IGNORE INTO Category(CategoryName, CategoryLink) VALUES('Медицина', 'https://indicator.ru/medicine');
    ''')
    DataBase.commit()
    Cursor.execute('''
    INSERT OR IGNORE INTO Category(CategoryName, CategoryLink) VALUES (?,?);
    ''', (CategoryName, CategoryLink))
    DataBase.commit()
    DataBase.close()


def InsertArticle(ArticleTitle, ArticleImageLink, Content, ArticleAuthor, CategoryId):
    DataBase = sqlite3.connect('Indicator.db')
    Cursor = DataBase.cursor()
    Cursor.execute('''
    INSERT INTO Articles(Title, Image, Content, Author, CategoryId) VALUES (?,?,?,?,?);
    ''', (ArticleTitle, ArticleImageLink, Content, ArticleAuthor, CategoryId))
    DataBase.commit()
    DataBase.close()



def GetCategoryLink():
    DataBase = sqlite3.connect('Indicator.db')
    Cursor = DataBase.cursor()
    Cursor.execute('''
    SELECT CategoryName, CategoryLink FROM Category;
    ''')
    CategoryData = Cursor.fetchall()
    return CategoryData


def GetCategoryId(CategoryName):
    Data = sqlite3.connect('Indicator.db')
    Base = Data.cursor()
    Base.execute('''
    SELECT CategoryId FROM Category WHERE CategoryName = ?
    ''', (CategoryName,))
    CategoryId = Base.fetchone()[0]
    return CategoryId




