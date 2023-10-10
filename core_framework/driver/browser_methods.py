import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BrowserMethods:
    def __init__(self, context):
        self.context = context

    def sleep(self, num_secs):
        time.sleep(num_secs)

    def goto(self, url):
        if url == self.get_current_url():
            print("URL matches not doing anything")
        self.context.browser.get(url)

    def click(self, element):
        element.click()

    def get_element_by_id(self, value):
        return self.context.browser.find_element(By.ID)

    def get_current_url(self):
        return self.context.browser.current_url

    def validate_url(self, page):
        current_url = self.get_current_url()
        url_file = self.context.yaml_utils.get_env_urls()
        if page == 'home':
            expected_url = url_file['base_url']
        else:
            expected_url = url_file['base_url'] + url_file[page]
        return current_url, expected_url

    def wait_until_visible(self, strategy, locator_text):
        matcher = ''
        match strategy:
            case 'class':
                matcher = By.CLASS_NAME
            case 'id':
                matcher = By.ID
            case 'name':
                matcher = By.NAME
            case 'css':
                matcher = By.CSS_SELECTOR

        WebDriverWait(self.context.browser, 10).until(EC.visibility_of_all_elements_located(
            (matcher, locator_text)))


