from Concrete_CS.config import ConfigurationManager
from Concrete_CS.components import DataIngestion
from Concrete_CS import logger

STAGE_NAME= "Data Ingestion Stage"

def main():
    config= ConfigurationManager()
    data_ingestion_config= config.get_data_ingestion_config()
    data_ingestion= DataIngestion(config= data_ingestion_config)
    data_ingestion.download_file()
    data_ingestion.load_data()

if __name__=="__main__":
    try:
        logger.info(f">>>>>>Stage: {STAGE_NAME} Started<<<<<<")
        main()
        logger.info(f">>>>>>Stage: {STAGE_NAME} Completed<<<<<<")
    except Exception as e:
        logger.exception(e)
        raise e