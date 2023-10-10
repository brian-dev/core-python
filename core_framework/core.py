import yaml

from core_framework.api.api import Api
from core_framework.driver.browser import Browser


def load_project_properties():
    with open(f'yaml_files/properties.yaml') as file_read:
        props = yaml.load(file_read, Loader=yaml.FullLoader)
    return props


def load_framework_properties():
    with open(f'../properties.yaml') as file_read:
        props = yaml.load(file_read, Loader=yaml.FullLoader)
    return props


class Core:
    project_props = load_project_properties()
    core_props = load_framework_properties()

    def initialize_core(self, browser_name='', headless=''):
        if self.project_props['project_type'] == 'api':
            return Api()
        else:
            browser = ''

            match browser_name:
                case 'chrome':
                    browser = Browser(headless).chrome_browser()
                case 'firefox':
                    return Browser(headless).firefox_browser()
                # case 'brave':
                #     browser = Browser(headless).brave_browser()
            return browser

    def get_core_props(self):
        return self.project_props
