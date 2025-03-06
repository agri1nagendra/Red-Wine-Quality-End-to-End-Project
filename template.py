import os 
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]:%(message)s:')

project_name = "wine_mlproject"

list_of_files = [
    f"src/{project_name}/__init__.py",       # Module initialization
    f"src/{project_name}/components/_init_.py",  # Components
    f"src/{project_name}/utils/_init_.py",       # Utility functions
    f"src/{project_name}/utils/common.py",       # Utility functions
    f"src/{project_name}/config/_init_.py",   # Configuration file
    f"src/{project_name}/config/configuration.py",# Configuration file
    f"src/{project_name}/pipeline/_init_.py",# Data processing script
    f"src/{project_name}/entity/_init_.py", # Entity
    f"src/{project_name}/entity/config_entity.py", # Entity
    f"src/{project_name}/constants/_init_.py",
    "config/config.yaml",
    "params.yaml",
    "main.py",
    "app.py",
    "requirements.txt",
    "setup.py",
    "research/trails.ipynb"
    "templates/index.html", # To Add Flask
 ] 

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir,filename = os.path.split(filepath)


    if filedir !="":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory;{filedir} for the file:{filename}")

    if(not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
        with open(filepath,"w") as f:
            pass
            logging.info(f"Creating empty file:{filepath}")

    else:
        logging.info(f"{filename} is already exists")
