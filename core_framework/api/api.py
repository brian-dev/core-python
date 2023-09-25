import requests
import yaml


def auth_headers(token):
    return {'x-auth-token': token}


def get_base_url():
    with open(f'yaml_files/properties.yaml') as file_read:
        props = yaml.load(file_read, Loader=yaml.FullLoader)
    return props['base_url']


class Api:
    base_url = get_base_url()

    def post_req(self, endpoint, payload):
        url = f"{self.base_url}/{endpoint}"
        return requests.post(url, payload)

    def get_req(self, endpoint):
        url = f"{self.base_url}/{endpoint}"
        return requests.get(url)

    def post_req_with_auth(self, endpoint, payload, token):
        url = f"{self.base_url}/{endpoint}"
        return requests.post(url, payload, headers=auth_headers(token))

    def del_req(self, endpoint, token):
        url = f"{self.base_url}/{endpoint}"
        return requests.delete(url, headers=auth_headers(token))

    def get_req_with_auth(self, endpoint, token):
        url = f"{self.base_url}/{endpoint}"
        return requests.get(url, headers=auth_headers(token))

    def patch_req_with_auth(self, endpoint, payload, token):
        url = f"{self.base_url}/{endpoint}"
        return requests.patch(url, payload, headers=auth_headers(token))
