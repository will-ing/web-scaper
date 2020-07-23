from app.scraper import get_citation_needed_count as cite_count, get_citations_needed_report as cite_report


URL = 'https://en.wikipedia.org/wiki/History_of_Mexico#cite_ref-60'


def test_exist():
    assert True == True


def test_count():
    assert cite_count(
        URL) == 'Number of citations needed are 5'


def test_report():
    assert 'The first people to settle in Mexico encountered a climate far milder than the current one. In particular, the Valley of Mexico contained several large paleo-lakes (known collectively as Lake Texcoco) surrounded by dense forest. Deer were found in this area, but most fauna were small land animals and fish and other lacustrine animals were found in the lake region.[citation needed][7] Such conditions encouraged the initial pursuit of a hunter-gatherer existence.' in cite_report(
        URL)
