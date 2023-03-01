import sqlite3

import requests
from bs4 import BeautifulSoup
from Configs import *
from pprint import pprint
from InsertData import InsertCategory, GetCategoryLink, GetCategoryId, InsertArticle
import time
import re
import sqlite3

class Indicator:
    def __init__(self):
        self.Url = URL
        self.Host = HOST
        self.Header = HEADER

    def CategoryParser(self):
        # Html = requests.get(self.Url, headers=self.Header).text
        # Soup = BeautifulSoup(Html, 'html.parser')
        # CategoryBlock = Soup.find('div', class_='jsx-3410637377')
        # Categories = CategoryBlock.find_all('a', class_='jsx-2749182516 _2DVGnFy1')
        #
        # for Category in Categories:
        #     time.sleep(3)
        #     CategoryLink = self.Host + Category.get('href')
        #     CategoryName = Category.get_text(strip=True)
        #     # CategoryId = GetCategoryId(CategoryName)
        #     InsertCategory(CategoryName, CategoryLink)

        DataCategories = GetCategoryLink()
        for i in DataCategories:
            CategoryName = i[0]
            CategoryLink = i[1]
            CategoryId = GetCategoryId(CategoryName)
            self.CategoryPageParser(CategoryLink, CategoryId)

    def CategoryPageParser(self, CategoryLink, CategoryId):
        time.sleep(2)
        Html = requests.get(CategoryLink, self.Header).text
        Soup = BeautifulSoup(Html, 'html.parser')
        Pages = Soup.find('div', class_='jsx-3362376990 text').get_text(strip=True)
        _, Page = Pages.split('из')
        for i in range(1, int(Page) + 1):
            time.sleep(2)
            PageSoup = self.GetHtml(CategoryLink, i)
            Container = PageSoup.find('div', class_='jsx-1556240810 _39FNd9SD')
            try:
                Articles = Container.find_all('a', class_='jsx-1889858572')
                for Article in Articles:
                    time.sleep(2)
                    ArticleLink = self.Host + Article.get('href')
                    self.ArticleParser(ArticleLink, CategoryId)
            except:
                pass

    def GetHtml(self, CategoryLink, i):
        Html = requests.get(CategoryLink + f'?page={i}').text
        Soup = BeautifulSoup(Html, 'html.parser')
        return Soup

    def ArticleParser(self, ArticleLink, CategoryId):
        time.sleep(1)
        Html = requests.get(ArticleLink, headers=self.Header).text
        Soup = BeautifulSoup(Html, 'html.parser')
        Container = Soup.find('div', class_='jsx-1556240810 _39FNd9SD')
        TextBLock = Container.find('div', class_='jsx-4164395053 text txkWXQba')
        Texts = TextBLock.find_all('p', class_='jsx-4247481572')
        ImageBlock = Soup.find('div', class_='_3WUoFFvr _1NIlGju2')
        ArticleTitle = Container.find('h1', class_='jsx-1660569506 jsx-1316785399 heading').get_text(strip=True)
        ArticleImage = self.Host + ImageBlock.find('link').get('href')
        Correcting = re.search(r'filters:quality\([0-9][0-9]\)\/', ArticleImage)[0]
        ArticleImageLink = ArticleImage.replace(Correcting, '')
        ArticleAuthor = Soup.find('a', class_='jsx-2902502616 link').get_text(strip=True)
        print(CategoryId)
        Content = []
        for Text in Texts[:1]:
            ArticleText = Text.get_text(strip=True)
            Content.append(ArticleText)
        # print(ArticleTitle)
        # print(ArticleImageLink)
        # print(Content)
        InsertArticle(ArticleTitle, ArticleImageLink, *Content, ArticleAuthor, CategoryId)


Parser = Indicator()
Parser.CategoryParser()
