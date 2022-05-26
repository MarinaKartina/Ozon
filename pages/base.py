from urllib.parse import urlparse


class BasePage(object):
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    def get_relative_link(self):
        url = urlparse(self.driver.current_url)
        return url.path

    def get_query(self):
        url = urlparse(self.driver.current_url)
        return url.query

    def get_url(self):
        url = urlparse(self.driver.current_url)
        return url.geturl()
