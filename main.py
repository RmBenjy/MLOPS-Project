import os

# Set MLflow environment variables
os.environ["MLFLOW_TRACKING_URI"] = "https://dagshub.com/RmBenjy/MLOPS-Project.mlflow"
os.environ["MLFLOW_TRACKING_USERNAME"] = "RmBenjy"
os.environ["MLFLOW_TRACKING_PASSWORD"] = "ba8c84e91b9a47bfeb4b083b748f8e057a71c22a"

from MLProject import logger  # Thanks to __init__.py, we can directly call MLProject instead of src.MLProject
from MLProject.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from MLProject.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
from MLProject.pipeline.stage_03_data_transformation import DataTransformationTrainingPipeline
from MLProject.pipeline.stage_04_model_trainer import ModelTrainerTrainingPipeline
from MLProject.pipeline.stage_05_model_evaluation import ModelEvaluationTrainingPipeline

STAGE_NAME = "Data Ingestion Stage"

try:
    logger.info(f">>>> stage {STAGE_NAME} started <<<<")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f">>>> stage {STAGE_NAME} completed <<<< \n\nx============x")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Data Validation Stage"

try:
    logger.info(f">>>> stage {STAGE_NAME} started <<<<")
    obj = DataValidationTrainingPipeline()
    obj.main()
    logger.info(f">>>> stage {STAGE_NAME} completed <<<< \n\nx============x")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Data Transformation Stage"

try:
    logger.info(f">>>> stage {STAGE_NAME} started <<<<")
    obj = DataTransformationTrainingPipeline()
    obj.main()
    logger.info(f">>>> stage {STAGE_NAME} completed <<<< \n\nx============x")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Model Trainer Stage"

try:
    logger.info(f">>>> stage {STAGE_NAME} started <<<<")
    obj = ModelTrainerTrainingPipeline()
    obj.main()
    logger.info(f">>>> stage {STAGE_NAME} completed <<<< \n\nx============x")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Model Evaluation Stage"

try:
    logger.info(f">>>> stage {STAGE_NAME} started <<<<")
    obj = ModelEvaluationTrainingPipeline()
    obj.main()
    logger.info(f">>>> stage {STAGE_NAME} completed <<<< \n\nx============x")
except Exception as e:
    logger.exception(e)
    raise e