from app.configs.paths import PATHS
import tomllib as tom

class Greeter:

    def __init__(self):
        with open(PATHS.BASE_CONFIG,'rb') as f: self.config = tom.load(f)

    def welcome(self):
        print("--" * 20)
        print(f"{self.config['app']['title']}")
        print(f"{self.config['app']['name']} v{self.config['app']['version']}")
        print("--" * 20)