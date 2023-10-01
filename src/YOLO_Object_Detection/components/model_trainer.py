
import os
import shutil
import sys
import yaml
import zipfile
import subprocess
from YOLO_Object_Detection.logging import logger
from YOLO_Object_Detection.exception import AppException
from YOLO_Object_Detection.utils.main_utils import read_yaml
from YOLO_Object_Detection.entity.config_entity import (ModelTrainerConfig, DataIngestionConfig)
from YOLO_Object_Detection.entity.artifacts_entity import ModelTrainerArtifact


class ModelTrainer:
    def __init__(self, model_trainer_config: ModelTrainerConfig):
        self.data_ingestion_config = DataIngestionConfig()
        self.model_trainer_config = model_trainer_config

    def initiate_model_trainer(self) -> ModelTrainerArtifact:
        logger.info("Initiated Model Trainer stage (Reached ModelTrainer class)...")

        if os.path.exists(os.path.join(self.model_trainer_config.model_trainer_dir, "best.pt")):
            logger.info(f"Trained model already available at : "
                        f"{os.path.join(self.model_trainer_config.model_trainer_dir, 'best.pt')}")
        else:
            try:
                logger.info("Unzipping data in root directory.")

                if not(os.path.exists(os.path.join(os.getcwd(), "train")) and
                       os.path.exists(os.path.join(os.getcwd(), "valid")) and
                       os.path.exists(os.path.join(os.getcwd(), "data.yaml"))):
                    with zipfile.ZipFile(self.data_ingestion_config.data_file_name, 'r') as zip_ref:
                        zip_ref.extractall(os.getcwd())

                os.remove(f"{self.data_ingestion_config.data_file_name}")

                with open("data.yaml", "r") as stream:
                    num_classes = str(yaml.safe_load(stream)['nc'])

                model_config_name = self.model_trainer_config.weight_name.split(".")[0]
                config = read_yaml(f"yolov5/models/{model_config_name}.yaml")
                config['nc'] = int(num_classes)

                with open(f"yolov5/models/custom_{model_config_name}.yaml", "w") as f:
                    yaml.dump(config, f)

                subprocess.run(f"python yolov5/train.py --img 416 --batch {self.model_trainer_config.batch_size} "
                               f"--epochs {self.model_trainer_config.no_epochs} --data ./data.yaml "
                               f"--cfg yolov5/models/custom_yolov5s.yaml --weights {self.model_trainer_config.weight_name} "
                               f"--name yolov5s_results --cache", shell=True)

                shutil.copy("./yolov5/runs/train/yolov5s_results/weights/best.pt", "./yolov5/")
                os.makedirs(self.model_trainer_config.model_trainer_dir, exist_ok=True)
                shutil.copy("yolov5/runs/train/yolov5s_results/weights/best.pt", f"./{self.model_trainer_config.model_trainer_dir}/")

                shutil.rmtree("./yolov5/runs")
                shutil.rmtree("./train")
                shutil.rmtree("./test")
                shutil.rmtree("./valid")
                shutil.rmtree("./data.yaml")

                model_trainer_artifact = ModelTrainerArtifact(
                    trained_model_file_path=os.path.join(self.model_trainer_config.model_trainer_dir, "best.pt"))

                logger.info("Exited Model Trainer stage (Exited ModelTrainer class)...")
                logger.info(f"Model Trainer Artifact: {model_trainer_artifact}")
                return model_trainer_artifact

            except Exception as e:
                raise AppException(e, sys)
