
import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

__version__ = "0.0.0"

REPO_NAME = "Deck_Cards_Detection_YOLOv5"
AUTHOR_USER_NAME = "Paras Jain"
SRC_REPO = "YOLO_Object_Detection"
AUTHOR_EMAIL = "Paras.Jain@eclerx.com"


setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="Object Detection using YOLOv5",
    long_description=long_description,
    long_description_content="text/markdown",
    url=f"https://github.com/pjain809/{REPO_NAME}",
    project_urls={"Bug Tracker": f"https://github.com/pjain809/{REPO_NAME}/issues"},
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)
