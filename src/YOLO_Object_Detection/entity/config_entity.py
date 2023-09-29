
import os
from datetime import datetime
from dataclasses import dataclass
from YOLO_Object_Detection.constants.training_pipeline import *


@dataclass
class TrainingPipelineConfig:
    artifacts_dir: str = ARTIFACTS_DIR


training_pipeline_config: TrainingPipelineConfig = TrainingPipelineConfig()


@dataclass
class DataIngestionConfig:
    data_file_name: str = DATA_FILE_NAME
    data_download_url: str = DATA_DOWNLOAD_URL
    data_ingestion_dir: str = os.path.join(training_pipeline_config.artifacts_dir, DATA_INGESTION_DIR_NAME)
    feature_store_file_path: str = os.path.join(data_ingestion_dir, DATA_INGESTION_FEATURE_STORE_DIR)


@dataclass
class DataValidationConfig:
    required_file_list = DATA_VALIDATION_ALL_REQUIRED_FILES
    data_validation_dir: str = os.path.join(training_pipeline_config.artifacts_dir, DATA_VALIDATION_DIR_NAME)
    valid_status_file_dir: str = os.path.join(data_validation_dir, DATA_VALIDATION_STATUS_FILE)
