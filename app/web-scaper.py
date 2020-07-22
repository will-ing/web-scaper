import requests
from bs4 import BeautifulSoup as bfs

URL = 'https://en.wikipedia.org/wiki/Python_(programming_language)'


def get_citation_count(url):

    res = requests.get(URL)

    content = res.content

    soup = BeautifulSoup(content, 'html.parser')

    results =
