
import os
import sys
from YOLO_Object_Detection.logging import logger
from YOLO_Object_Detection.exception import AppException
from YOLO_Object_Detection.components.data_ingestion import DataIngestion
from YOLO_Object_Detection.entity.config_entity import DataIngestionConfig
from YOLO_Object_Detection.entity.artifacts_entity import DataIngestionArtifact


class TrainPipeline:
    def __init__(self):
        self.data_ingestion_config = DataIngestionConfig()

    def start_data_ingestion(self) -> DataIngestionArtifact:
        try:
            logger.info("Initiating Data Ingestion stage (Reached TrainPipeline class)...")
            data_ingestion = DataIngestion(self.data_ingestion_config)
            data_ingestion_artifact = data_ingestion.initiate_data_ingestion()
            logger.info("Finished Data Ingestion stage (Exited TrainPipeline class)...")

            return data_ingestion_artifact
        except Exception as e:
            raise AppException(e, sys)

    def run_pipeline(self) -> None:
        try:
            data_ingestion_artifact = self.start_data_ingestion()

        except Exception as e:
            raise AppException(e, sys)
