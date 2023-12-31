
import os
import logging
from pathlib import Path

logging.basicConfig(level= logging.INFO, format= '[%(asctime)s]: %(message)s')

PROJECT_NAME = "YOLO_Object_Detection"
LIST_OF_FILES = [
    "data/.gitkeep", "templates/index.html",
    "app.py", "requirements.txt",
    "setup.py", "research/trials.ipynb",
    "params.yaml",  "Dockerfile",
    ".github/workflows/.gitkeep",
    "config/config.yaml", "main.py",
    f"src/{PROJECT_NAME}/__init__.py",
    f"src/{PROJECT_NAME}/components/__init__.py",
    f"src/{PROJECT_NAME}/utils/__init__.py",
    f"src/{PROJECT_NAME}/utils/main_utils.py",
    f"src/{PROJECT_NAME}/logging/__init__.py",
    f"src/{PROJECT_NAME}/exception/__init__.py",
    f"src/{PROJECT_NAME}/config/__init__.py",
    f"src/{PROJECT_NAME}/config/configuration.py",
    f"src/{PROJECT_NAME}/pipeline/__init__.py",
    f"src/{PROJECT_NAME}/pipeline/training_pipeline.py",
    f"src/{PROJECT_NAME}/entity/__init__.py",
    f"src/{PROJECT_NAME}/entity/config_entity.py",
    f"src/{PROJECT_NAME}/entity/artifacts_entity.py",
    f"src/{PROJECT_NAME}/constants/__init__.py",
    f"src/{PROJECT_NAME}/constants/application.py",
    f"src/{PROJECT_NAME}/constants/training_pipeline/__init__.py"]

for filepath in LIST_OF_FILES:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if os.path.exists(filepath):
        logging.info(f"File : <{filename}> already exists.")
        continue

    if filedir != "":
        if not (os.path.exists(filedir)):
            os.makedirs(filedir, exist_ok=True)
            logging.info(f"Creating Directory <{filedir}> for the File : {filename}.")
        else:
            logging.info(f"Existing Directory <{filedir}> for the File : {filename}.")

    if not(os.path.exists(filepath)):
        with open(filepath, 'w') as f:
            pass
        logging.info(f"Creating Empty File : <{filepath}>")
