from pathlib import Path
import os
import rasterio as rio
from PIL import Image

IMAGE_EXTENSIONS = [".png",".jpg",".jpeg",".tif",".tiff"]
JSON_EXTENSIONS = [".json",".geojson"]


class _ReadImageType:

    def __init__(self,path:str):
        self.IMAGE_PATH = path
        self.IMAGE_FLAG = True
        if path.endswith(".png"): 
            self._png()
        elif path.endswith(".jpg") or path.endswith(".jpeg"): 
            self._jpg()
        elif path.endswith(".tif") or path.endswith(".tiff"): 
            self._tiff()
        else:
            self.IMAGE_FLAG = False        

    def _png(self):
        pass

    def _jpg(self):
        pass

    def _tiff(self):
        pass

    def get(self):
        pass

class _ReadJsonType:

    def _json(path):
        pass

    def _geojson(path):
        pass

class IO:

    def __init__(self):
        pass

    def read(self,path:str):
        _path = Path(path)
        if os.path.exists(_path):
            if _path.suffix in IMAGE_EXTENSIONS:
                return _ReadImageType(path)
            elif _path.suffix in JSON_EXTENSIONS:
                return _ReadJsonType(path)
        else:
            return None
