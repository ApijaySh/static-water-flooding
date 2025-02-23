from app.configs.paths import PATHS
from app.tools.containers import ArgsContainer
from app.tools.handlers import ParamsHandler
import argparse
import tomllib as tom

class StitchArgs(argparse.Action):
    def __call__(self, parser, namespace, values, option_string = None):
        setattr(namespace,self.dest,"".join(values).replace("'","").replace('"',''))

class ArgsTools:

    ACTION_CLASS = [("stitchargs",StitchArgs)]

    @staticmethod
    def define_type(param:str):
        if param.lower() == "str": return str
        elif param.lower() == "int": return int
        elif param.lower() == "float": return float
        elif param.lower() == "bool": return bool
        else: return str

    @staticmethod
    def define_action(param:str):
        if param.lower() == ArgsTools.ACTION_CLASS[0][0]: return ArgsTools.ACTION_CLASS[0][1]
        else: return param
    
    @staticmethod
    def convert_int(param:str):
        try: return int(param)
        except: return param

class ArgParserTool:

    def __init__(self):
        with open(PATHS.BASE_CONFIG,'rb') as f: self.config = tom.load(f)
        with open(PATHS.PARAMS_CONFIG,'rb') as f: self.param_config = tom.load(f)
        self.args = None
        self.params_handler = None
        self.parser = argparse.ArgumentParser(
            prog=self.config['description']['prog'],
            description=self.config['description']['description'],
            epilog=self.config['description']['epilog'],
            formatter_class=argparse.ArgumentDefaultsHelpFormatter
        )
        for param in self.param_config.keys():
            if param not in self.param_config['EXCLUDE_PARAMS']:
                self.parser.add_argument(
                    self.param_config[param]["short_name"],
                    self.param_config[param]["name"],
                    type=ArgsTools.define_type(self.param_config[param]["type"]),
                    nargs=ArgsTools.convert_int(self.param_config[param]["nargs"]),
                    required=self.param_config[param]["required"],
                    action=ArgsTools.define_action(self.param_config[param]["action"]),
                    default=self.param_config[param]["default"],
                    help=self.param_config[param]["help"],
                    dest=self.param_config[param]["dest"]
                )
        
    def parse_(self,args:dict):
        self.params_handler = ParamsHandler(args)
        return self.params_handler.verify()
