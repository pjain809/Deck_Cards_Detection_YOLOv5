
ARTIFACTS_DIR: str = "artifacts"

"""
Data Ingestion Related Configuration
"""

DATA_INGESTION_DIR_NAME: str = "data_ingestion"
DATA_INGESTION_FEATURE_STORE_DIR: str = "feature_store"
DATA_FILE_NAME = "Deck-Cards-data.zip"
DATA_DOWNLOAD_URL: str = "https://drive.google.com/file/d/1uSKxw0yMbSy8TXZix0AM4KOvKRZDQFSi/view?usp=sharing"


"""
Data Validation Related Configuration
"""

DATA_VALIDATION_DIR_NAME: str = "data_validation"
DATA_VALIDATION_STATUS_FILE: str = "status.txt"
DATA_VALIDATION_ALL_REQUIRED_FILES: list = ["train", "test", "valid", "data.yaml"]


"""
Model Training Related Configuration
"""

MODEL_TRAINER_DIR_NAME: str = "model_trainer"
MODEL_TRAINER_PRETRAINED_WEIGHT_NAME: str = "yolov5s.pt"
MODEL_TRAINER_NO_EPOCHS: int = 1
MODEL_TRAINER_BATCH_SIZE: int = 16
