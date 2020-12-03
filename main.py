from bs4 import BeautifulSoup
import requests
import json


def get_page_html(num):
    url = "https://bandcamp.com/artist_index?page={num}"
    html = requests.get(url).text
    return html


def get_artist_info(html):
    soup = BeautifulSoup(html, 'html.parser')
    names = soup.find_all(class_="item")
    return [[n.get_text().strip(), n.find('a').get('href')] for n in names]


def get_artist_names(html):
    soup = BeautifulSoup(html, 'html.parser')
    names = soup.find_all(class_="item")
    return [n.find('a').get('href') for n in names]


def paginate(start_page, end_page):
    return [get_artist_names(get_page_html(page)) for page in list(range(start_page, end_page))]


if __name__ == "__main__":
    p = paginate(1, 3436)  # todo last page changes as more bands added
    flat = [name for page in p for name in page]
    # print("\n".join(flat))
    with open(f"results.txt", "a") as f:
        f.write("\n".join(flat))
