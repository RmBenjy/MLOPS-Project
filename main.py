from MLProject import logger  # Thanks to __init__.py, we can directly call MLProject instead of src.MLProject
from MLProject.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline

STAGE_NAME = "Data Ingestion Stage"

try:
    logger.info(f">>>> stage {STAGE_NAME} started <<<<")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f">>>> stage {STAGE_NAME} completed <<<< \n\nx============x")
except Exception as e:
    logger.exception(e)
    raise e