
import os
import sys
import shutil
from YOLO_Object_Detection.logging import logger
from YOLO_Object_Detection.exception import AppException
from YOLO_Object_Detection.entity.config_entity import DataValidationConfig, DataIngestionConfig
from YOLO_Object_Detection.entity.artifacts_entity import (DataIngestionArtifact, DataValidationArtifact)


class DataValidation:
    def __init__(self,
                 data_ingestion_artifact: DataIngestionArtifact,
                 data_validation_config: DataValidationConfig):
        try:
            self.data_ingestion_artifact = data_ingestion_artifact
            self.data_validation_config = data_validation_config

        except Exception as e:
            raise AppException(e, sys)

    def validate_all_files(self) -> bool:
        try:
            validation_status = True
            feature_store_path = self.data_ingestion_artifact.feature_store_path
            req_files = self.data_validation_config.required_file_list
            all_files = os.listdir(self.data_ingestion_artifact.feature_store_path)

            for file in req_files:
                if file == "data.yaml" and file in all_files:
                    continue
                if file not in all_files or (len(os.listdir(os.path.join(feature_store_path, file))) == 0):
                    validation_status = False

            os.makedirs(self.data_validation_config.data_validation_dir, exist_ok=True)
            with open(self.data_validation_config.valid_status_file_dir, 'w') as f:
                f.write(f"Validation Status: {validation_status}")

            return validation_status

        except Exception as e:
            raise AppException(e, sys)

    def initiate_data_validation(self) -> DataValidationArtifact:
        logger.info("Initiated Data Validation stage (Reached DataValidation class)...")
        try:
            status = self.validate_all_files()
            data_validation_artifact = DataValidationArtifact(validation_status=status)

            logger.info(f"Data Validation Artifact: {data_validation_artifact}")
            logger.info("Finished Data Validation stage (Exited DataValidation class)...")

            if status:
                if not os.path.exists(os.path.join(os.getcwd(), DataIngestionConfig().data_file_name)):
                    logger.info(f"Copying {DataIngestionConfig().data_file_name} in root directory...")
                    shutil.copy(self.data_ingestion_artifact.data_zip_file_path, os.getcwd())
                    logger.info(f"Copied {DataIngestionConfig().data_file_name} in root directory...")
                else:
                    logger.info(f"Copy of {DataIngestionConfig().data_file_name} already exists in root directory...")

            return data_validation_artifact

        except Exception as e:
            raise AppException(e, sys)
