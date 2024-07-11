

class WebPage(object):

    driver = None
    def __init__(self, driver, url, timeout=10):
        self.driver = driver
        self.driver.get(url)
        # self.url = url
        # self.driver.implicity_wait(timeout)
