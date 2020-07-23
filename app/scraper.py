import requests
from bs4 import BeautifulSoup as bfs

URL = 'https://en.wikipedia.org/wiki/History_of_Mexico#cite_ref-60'


def get_citation_needed_count(url):
    """
    This gets the count of citations on a wiki page

    Args:
        url (str): Needs to be a valid url

    Returns:
        str: the number of cites needed
    """

    res = requests.get(url)

    content = res.content

    soup = bfs(content, 'html.parser')

    first_el = soup.find(id='mw-content-text')

    find_cites = first_el.find_all(
        class_='noprint Inline-Template Template-Fact')

    citations = len(find_cites)

    print(f'Number of citations needed are {citations}\n')

    return f'Number of citations needed are {citations}'


get_citation_needed_count(URL)


def get_citations_needed_report(url: str) -> str:
    """
    Gives you the elements in on the page that needed cites

    Args:
        url (str): Valid URL on wikipedia

    Returns:
        str: All the paragraphs that need cites.
    """

    res = requests.get(url)

    content = res.content

    soup = bfs(content, 'html.parser')

    first_el = soup.find(id='mw-content-text')

    p_tag = first_el.find_all('p')

    show_which = ''

    for p in p_tag:
        if 'citation needed' in p.text:
            show_which += p.text + '\n'

    print(show_which.strip())
    return show_which


get_citations_needed_report(URL)
