import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture
def browser(no_window):
    options = Options()
    if no_window:
        options.add_argument("--headless=new")
    chrome_browser = webdriver.Chrome(options=options)
    yield chrome_browser
    chrome_browser.quit()

