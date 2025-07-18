import os 
import sys 
from dataclasses import dataclass

@dataclass
class DataIngestionConfig:
    train_data_path : str = os.path.join('artifacts' , 'train.csv')
    test_data_path : str = os.path.join('artifacts' , 'test.csv')
    raw_data_path : str = os.path.join('artifacts' , 'raw.csv')
