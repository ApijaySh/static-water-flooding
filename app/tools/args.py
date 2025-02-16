from app.configs.paths import PATHS
import argparse
import tomllib as tom

class SmallTools:

    @staticmethod
    def isType(param):
        if param.lower() == "str": return str
        elif param.lower() == "int": return int
        elif param.lower() == "float": return float
        elif param.lower() == "bool": return bool
        else: return str

class StitchArgs(argparse.Action):
    def __call__(self, parser, namespace, values, option_string = None):
        setattr(namespace,self.dest,"".join(values).replace("'","").replace('"',''))

class ArgParserTool:

    def __init__(self):
        with open(PATHS.BASE_CONFIG,'rb') as f: self.config = tom.load(f)
        with open(PATHS.PARAMS_CONFIG,'rb') as f: self.param_config = tom.load(f)
        self.parser = argparse.ArgumentParser(
            prog=self.config['description']['prog'],
            description=self.config['description']['description'],
            epilog=self.config['description']['epilog']
        )
        params = self.param_config['params']
        