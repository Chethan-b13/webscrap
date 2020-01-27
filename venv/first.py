import pandas as pd
from bs4 import BeautifulSoup
import requests

page = requests.get('https://www.indiatoday.in/india?page=2')

soup = BeautifulSoup(page.content, 'html.parser')

headings = soup.find_all(class_='detail')

titles = [heading.find("a").get_text() for heading in headings]

news = pd.DataFrame(
    {
        'Top news': titles
    }
)
news.to_csv('news.csv')
