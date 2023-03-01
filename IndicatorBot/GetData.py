import sqlite3


def GetCategories():
    DataBase = sqlite3.connect('..//IndicatorParser/Indicator.db')
    Cursor = DataBase.cursor()
    Cursor.execute('''
    SELECT CategoryName FROM Category WHERE CategoryName != ?;
    ''', ('Редакция',))
    Categories = Cursor.fetchall()
    DataBase.close()
    return Categories


def CheckCategory(Category):
    DataBase = sqlite3.connect('..//IndicatorParser/Indicator.db')
    Cursor = DataBase.cursor()
    Cursor.execute('''
    SELECT CategoryId FROM Category WHERE CategoryName = ?
    ''', (Category, ))
    CategoryData = Cursor.fetchone()
    DataBase.close()
    return CategoryData


def GetArticleId(CategoryId):
    DataBase = sqlite3.connect('..//IndicatorParser/Indicator.db')
    Cursor = DataBase.cursor()
    Cursor.execute('''
    SELECT ArticleId FROM Articles WHERE CategoryId = ?
    ''', (CategoryId,))
    ArticleId = Cursor.fetchall()
    ArticleFirstId = ArticleId[0]
    ArticleLastId = ArticleId[-1]
    DataBase.close()
    return ArticleFirstId, ArticleLastId


def GetArticleData(ArticleId):
    DataBase = sqlite3.connect('..//IndicatorParser/Indicator.db')
    Cursor = DataBase.cursor()
    Cursor.execute('''
    SELECT Title, Image, Content, Author FROM Articles WHERE ArticleId = ?
    ''', (ArticleId, ))
    ArticleData = Cursor.fetchone()
    return ArticleData