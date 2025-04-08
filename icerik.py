import requests
from bs4 import BeautifulSoup

def content(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')

   
    title_tag = soup.find('h1')  
    title = title_tag.get_text(strip=True) if title_tag else 'Başlık yok'


    date_tag = soup.find('time') 
    tarih = date_tag.get_text(strip=True) if date_tag else 'taih yok'

   
    content_tags = soup.find_all('p')  
    icerik = ' '.join([p.get_text(strip=True) for p in content_tags])

    
    data = '{};{};{}'.format(tarih, title, icerik)
    with open("haber.txt", "a", encoding="utf-8") as file:
        file.write(data + '\n')


content("https://www.sabah.com.tr/")