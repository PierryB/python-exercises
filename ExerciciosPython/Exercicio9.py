import requests
from bs4 import BeautifulSoup
url = "https://www.nytimes.com"
r = requests.get(url)
soup = BeautifulSoup(r.content, 'html.parser')

article_titles = soup.select('.css-xdandi')

# with open("arquivo.txt", "w") as open_file:
#     for title in article_titles:
#         open_file.write(title.get_text())


def main():
    with open("arquivo.txt", "w") as open_file:
        for title in article_titles:
            open_file.write(title.get_text())


if __name__ == "__main__":
    main()