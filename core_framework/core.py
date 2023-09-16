import yaml

from core_framework.api import Api


def load_project_properties():
    with open(f'yaml_files/properties.yaml') as file_read:
        props = yaml.load(file_read, Loader=yaml.FullLoader)
    return props


def load_framework_properties():
    with open(f'../properties.yaml') as file_read:
        props = yaml.load(file_read, Loader=yaml.FullLoader)
    return props


class Core:
    project_name = 'python_api'
    project_props = load_project_properties()
    core_props = load_framework_properties()

    def initialize_core(self):
        if self.project_props['project_type'] == 'api':
            return Api()
        else:
            raise Exception('You cannot do that')

    def get_core_props(self):
        return self.project_props
