import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


@pytest.fixture
def expected_href():
    return 'https://www.python.org'


def test_basic(expected_href):
    subject = 'Python'
    browser = webdriver.Chrome()
    site = "https://www.bing.com/"
    browser.get(site)
    assert 'Bing' in browser.title
    elem = browser.find_element_by_name('q')
    elem.send_keys(subject)
    elem.send_keys(Keys.RETURN)
    selector = '#b_results > li:nth-child(1) > div.b_caption > div > cite'
    link = browser.find_element_by_css_selector(selector)
    assert link.text == expected_href
