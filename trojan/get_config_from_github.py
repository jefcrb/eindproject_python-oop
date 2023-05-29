import requests

class Config:
    def __init__(self):
        self.url = "https://raw.githubusercontent.com/jefcrb/eindproject_python-oop/master/config.json"

    def get_config(self):
        try:
            r = requests.get(self.url)
            data = r.json()

            return data

        except requests.exceptions.RequestException as e:
            print(e)
