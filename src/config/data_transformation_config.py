import os , sys 
from dataclasses import dataclass 

@dataclass
class DataTransformationConfig:
    preprocessor_object_file_path = os.path.join('artifacts' , 'preprocessor.pkl')
