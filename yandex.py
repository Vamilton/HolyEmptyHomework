import configparser
import requests
import json
import sys


class YaUploader:
    def __init__(self) -> object:
        self.path = 'settings.ini'
        self.config = configparser.ConfigParser()
        self.config.read(self.path)
        self.token = self.config.get("Tokens", "ya_token")
        self.header = {
            'Content-Type': 'application/json',

            'Authorization': f'OAuth {self.token}'
        }

    def new_folder(self, name):
        flag = True
        while flag:
            folder_name = name
            its_url = f'https://cloud-api.yandex.net/v1/disk/resources?path={folder_name}'
            response = requests.put(its_url, headers=self.header)
            flag = True if response.status_code == 409 else False
            return 'Такая папка существует' if flag == True else 'Ok'
        if response.status_code != 201:
            print(response.status_code)
            sys.exit('Что-то пошло не так, давай сначала.')
        return folder_name

    def del_folder(self, name):
        folder_name = name
        its_url = f'https://cloud-api.yandex.net/v1/disk/resources?path={folder_name}'
        response = requests.delete(its_url, headers=self.header)


