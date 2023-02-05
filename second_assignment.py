import requests

TOKEN = ''
url = 'https://cloud-api.yandex.net/v1/disk/resources'


class YandexDisk:
    def __init__(self, token):
        self.token = token

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': f'OAuth {self.token}'
        }

    def get_parameters(self):
        return {
            'path': '/test_assignment'
        }

    def put_methode_create_folder(self, url_address):
        response = requests.put(url=url_address, params=self.get_parameters(), headers=self.get_headers())
        folder_status = response.status_code
        return folder_status


if __name__ == "__main__":
    ya = YandexDisk(TOKEN)
    print(ya.put_methode_create_folder(url))


