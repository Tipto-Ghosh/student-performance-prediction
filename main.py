import sys 
from src.logging import logging 
from src.exception import CustomException

try:
    a = 12 / 0 
except ZeroDivisionError as zd:
    logging.exception("Divided by zero")
    raise CustomException(zd , sys)