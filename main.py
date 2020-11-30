from bs4 import BeautifulSoup
import requests
from time import time

def get_page_html(num):
    url = "https://bandcamp.com/artist_index?page={num}"
    html = requests.get(url).text
    return html

def get_artist_names(html):
    soup = BeautifulSoup(html, 'html.parser')
    names = soup.find_all(class_="item")
    return [[n.get_text().strip(), n.find('a').get('href')] for n in names]

def paginate(total_pages):
    return [get_artist_names(get_page_html(page)) for page in range(total_pages)]

if __name__ == "__main__":
    print(get_artist_names(get_page_html(1)))
    # print(paginate(1))
    # t = time()
    # s = "\n".join(paginate(1)[0])
    # with open(f"results-{t}", "a") as f:
    #     f.write(s)