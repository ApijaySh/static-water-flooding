from dataclasses import dataclass

class HandlerConfig:

    PATHS = ["elevation_file_path","image_file_path","bbox_file_path"],["output_directory"]

@dataclass
class ArgsContainer:
    show_interface:bool
    elevation_file_path:str
    image_file_path:str
    bbox_file_path:str
    output_directory:str
    water_level_max:float
    water_level_min:float
    water_level_rise_per_frame:float
    water_color:tuple[int,int,int]
    video_resolution:tuple[int,int]
    video_fps:int
    clip_to_bbox:bool
