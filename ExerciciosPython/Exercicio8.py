import requests
from bs4 import BeautifulSoup
url = "https://www.nytimes.com"
r = requests.get(url)
soup = BeautifulSoup(r.content, 'html.parser')

article_titles = soup.select('.css-xdandi')

def main():
    for title in article_titles:
        print(title.get_text())

if __name__ == "__main__":
    main()