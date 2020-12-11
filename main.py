from bs4 import BeautifulSoup
import requests
import json


def get_page_html(num):
    url = f"https://bandcamp.com/artist_index?page={num}"
    html = requests.get(url).text
    return html


def get_artist_info(html):
    soup = BeautifulSoup(html, 'html.parser')
    names = soup.find_all(class_="item")
    return [[n.get_text().strip(), n.find('a').get('href')] for n in names]


def get_artist_links(html):
    soup = BeautifulSoup(html, 'html.parser')
    names = soup.find_all(class_="item")
    return [n.find('a').get('href') for n in names]


def get_bands_on_page(page_number):
    return get_artist_links(get_page_html(page_number))


def write_file():
    for i in range(1, 3449):  # todo last page changes as more bands added
        with open(f"results-{i}.txt", "w") as f:
            bands = get_bands_on_page(i)
            # print(bands)
            f.write("\n".join(bands))


def write_json():
    with open("results.txt") as fin:
        dicty = {"bands": []}
        for line in fin.readlines():
            dicty["bands"].append(line.strip())
    with open("results.json", "w") as fout:
        json.dump(dicty, fout)


if __name__ == "__main__":
    write_file()
    # write_json()
