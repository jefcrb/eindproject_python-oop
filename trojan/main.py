from get_config_from_github import Config


class Trojan:
    def __init__(self):
        self.get_config()
        print(self.config)


    def get_config(self):
        self.config = Config().get_config()


if __name__ == '__main__':
    Trojan()