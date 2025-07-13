# we need find_namespace_packages to find all the package of the project
from setuptools import find_namespace_packages , setup
from typing import List

# read the README.md file for project 
with open("README.md" , "r" , encoding = "utf-8") as file:
    long_description = file.read()

# prevent requirements.txt -e . to be added in requirements list
HYPEN_E_DOT = '-e .'
# read the requirements.txt file
def get_requirements(req_file: str) -> List[str]:
    requirements = []
    
    with open(req_file) as req:
        requirements = req.readlines()
        requirements = [req.replace('\n' , '') for req in requirements]   
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    
    return requirements

# All meta-data's
project_name = "student-performance-prediction"
version = "0.0.1"
author_name = "Tipto-Ghosh"
author_email = "tiptoghosh@gmail.com"
src_repo = "src"
url = "https://github.com/Tipto-Ghosh/student-performance-prediction"

setup( 
   name = project_name, 
   version = version, 
   author = author_name, 
   author_email = author_email, 
   packages = find_namespace_packages(), 
   description = "An end-to-end ML pipeline and Flask app for predicting students performance mark",
   long_description = long_description,
   long_description_content_type = "text/markdown", 
   url = url,
   install_requires = get_requirements('requirements.txt') 
)

