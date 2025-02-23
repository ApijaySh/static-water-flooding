from app.tools.containers import ArgsContainer, HandlerConfig
from app.configs.paths import PATHS
import tomllib as tom
from pathlib import Path
import os

class VerifyArgs:

    @staticmethod
    def is_filepath_valid(path:str) -> bool:
        if isinstance(path,str) or isinstance(path,os.PathLike):
            _path = Path(path)
            if _path.is_file(): return True
            else: return False
        else:
            return False
    
    @staticmethod
    def is_directory_valid(path:str) -> bool:
        if isinstance(path,str) or isinstance(path,os.PathLike):
            _path = Path(path)
            if _path.is_dir(): return True
            else: return False
        else:
            return False

class ParamsHandler:

    def __init__(self,raw_input:dict):
        with open(PATHS.VARIABLE_MAPS_CONFIG,'rb') as f: self.variable_mappings = tom.load(f)
        self.raw_input = raw_input
    
    def verify(self):
        process_args = {}
        for param in self.variable_mappings['mapping'].keys():
            process_args[param] = self.raw_input[self.variable_mappings['mapping'][param]]
            if param in HandlerConfig.PATHS[0]:
                if not VerifyArgs.is_filepath_valid(self.raw_input[self.variable_mappings['mapping'][param]]):
                    process_args[param] = None
            if param in HandlerConfig.PATHS[1]:
                if not VerifyArgs.is_directory_valid(self.raw_input[self.variable_mappings['mapping'][param]]):
                    process_args[param] = None
        return ArgsContainer(**process_args)
