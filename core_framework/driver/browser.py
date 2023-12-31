from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager


def get_chrome_options():
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    return options


def get_firefox_options():
    ff_options = Options()
    ff_options.headless = True
    return ff_options


class Browser:
    def __init__(self, headless):
        self.headless = headless

    def chrome_browser(self):
        if self.headless:
            options = get_chrome_options()
            chrome = webdriver.Chrome(options=options)
        else:
            chrome = webdriver.Chrome()
        return chrome

    # def brave_browser(self):
    #     if self.headless:
    #         options = get_chrome_options()
    #         browser = webdriver.Chrome(
    #             service=BraveService(ChromeDriverManager(chrome_type=ChromeType.BRAVE).install()),
    #             chrome_options=options
    #         )
    #     else:
    #         browser = webdriver.Chrome(
    #             service=BraveService(ChromeDriverManager(chrome_type=ChromeType.BRAVE).install()))
    #     return browser

    def firefox_browser(self):
        if self.headless:
            options = get_firefox_options()
            browser = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=options)
        else:
            browser = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
        return browser
