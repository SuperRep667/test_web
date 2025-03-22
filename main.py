import requests as re
from bs4 import BeautifulSoup

res = re.get('https://www.film.ru/compilation/100-luchshih-filmov-xxi-veka-po-versii-zhurnala-empire')
soup = BeautifulSoup(res.text, features='lxml')
divs = soup.find_all('div', class_='redesign_afisha_movie_main') 
for div in divs:
    data = [i.strip() for i in div.text.split('\n') if i != '']
    print(data[:10])
