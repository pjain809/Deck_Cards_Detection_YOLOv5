
import os
import sys
import yaml
import base64
from YOLO_Object_Detection.logging import logger
from YOLO_Object_Detection.exception import AppException


def read_yaml(file_path: str) -> dict:
    try:
        with open(file_path, "rb") as yaml_file:
            logger.info(f"YAML File: {file_path} successfully read.")
            return yaml.safe_load(yaml_file)

    except Exception as e:
        raise AppException(e, sys) from e


def write_yaml_file(file_path: str, content: object, replace: bool = False) -> None:
    try:
        if replace and os.path.exists(file_path):
            os.remove(file_path)

        os.makedirs(os.path.dirname(file_path), exist_ok=True)

        with open(file_path, "w") as f:
            yaml.dump(content, f)
            logger.info(f"YAML File: {file_path} successfully written.")

    except Exception as e:
        raise AppException(e, sys) from e


def decodeImage(imgstring, fileName):
    imgdata = base64.b64decode(imgstring)

    with open("./data/" + fileName, "wb") as f:
        f.write(imgdata)


def encodeImageIntoBase64(croppedImagePath):
    with open(croppedImagePath, "rb") as f:
        return base64.b64encode(f.read())
