
import os
import sys
from YOLO_Object_Detection.logging import logger
from YOLO_Object_Detection.exception import AppException
from YOLO_Object_Detection.components.data_ingestion import DataIngestion
from YOLO_Object_Detection.components.data_validation import DataValidation
from YOLO_Object_Detection.components.model_trainer import ModelTrainer
from YOLO_Object_Detection.entity.config_entity import (DataIngestionConfig, DataValidationConfig, ModelTrainerConfig)
from YOLO_Object_Detection.entity.artifacts_entity import (DataIngestionArtifact, DataValidationArtifact,
                                                           ModelTrainerArtifact)


class TrainPipeline:
    def __init__(self):
        self.data_ingestion_config = DataIngestionConfig()
        self.data_validation_config = DataValidationConfig()
        self.model_trainer_config = ModelTrainerConfig()

    def start_data_ingestion(self) -> DataIngestionArtifact:
        try:
            logger.info("Initiated Data Ingestion stage (Reached TrainPipeline class)...")
            data_ingestion = DataIngestion(self.data_ingestion_config)
            data_ingestion_artifact = data_ingestion.initiate_data_ingestion()
            logger.info("Finished Data Ingestion stage (Exited TrainPipeline class)...")

            return data_ingestion_artifact
        except Exception as e:
            raise AppException(e, sys)

    def start_data_validation(self, data_ingestion_artifact: DataIngestionArtifact) -> DataValidationArtifact:
        try:
            logger.info("Initiating Data Validation stage (Reached TrainPipeline class)...")
            data_validation = DataValidation(data_ingestion_artifact=data_ingestion_artifact,
                                             data_validation_config=self.data_validation_config)
            data_validation_artifact = data_validation.initiate_data_validation()
            logger.info("Finished Data Validation stage (Exited TrainPipeline class)...")

            return data_validation_artifact
        except Exception as e:
            raise AppException(e, sys)

    def start_model_trainer(self) -> ModelTrainerArtifact:
        try:
            model_trainer = ModelTrainer(model_trainer_config=self.model_trainer_config)
            model_trainer_artifact = model_trainer.initiate_model_trainer()

            return model_trainer_artifact
        except Exception as e:
            raise AppException(e, sys)

    def run_pipeline(self) -> None:
        try:
            data_ingestion_artifact = self.start_data_ingestion()
            data_validation_artifact = self.start_data_validation(data_ingestion_artifact=data_ingestion_artifact)
            if data_validation_artifact.validation_status:
                model_trainer_artifact = self.start_model_trainer()
            else:
                raise Exception("Incorrect Data Format [Data Validation not satisfied]")

        except Exception as e:
            raise AppException(e, sys)
