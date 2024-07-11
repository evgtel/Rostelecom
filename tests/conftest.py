import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

no_window = False

@pytest.fixture
def browser():
    options = Options()
    if no_window:
        options.add_argument("--headless=new")
    chrome_browser = webdriver.Chrome(options=options)
    yield chrome_browser
    chrome_browser.quit()

