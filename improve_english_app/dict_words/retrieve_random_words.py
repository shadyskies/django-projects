import os
from bs4 import BeautifulSoup
import mysql.connector
from dotenv import load_dotenv

HEADERS = ({'User-Agent':
                'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36',
            'Accept-Language': 'en-US, en;q=0.5'})


def get_words(count=2):
    load_dotenv()
    mydb = mysql.connector.connect(
        host="localhost",
        user="django_projects",
        password=os.getenv('DB_PWD'),
        database="entries"
    )

    mycursor = mydb.cursor()
    query = "SELECT word, definition FROM entries ORDER BY RAND() LIMIT " + str(count)
    mycursor.execute(query)

    myresult = mycursor.fetchall()
    return myresult


# TODO: implementing sentence for particular word
def get_sentence(result):
    for i in result:
        try:
            print(i[0].lower())
            url = 'https://sentence.yourdictionary.com/' + i[0].lower()
            page = requests.get(url, headers=HEADERS)
            soup = BeautifulSoup(page.content, features='html.parser')
            sentences = soup.find_all('div', {'class': 'sentence-item'})
            print(sentences)
        except:
            print('word not found')


def search(word):
    load_dotenv()
    mydb = mysql.connector.connect(
        host="localhost",
        user="django_projects",
        password=os.getenv('DB_PWD'),
        database="entries"
    )

    mycursor = mydb.cursor()
    query = "SELECT word, definition FROM entries WHERE word = " + f"'{word}'"
    mycursor.execute(query)

    result = mycursor.fetchall()
    print(result)
    return result
