from Concrete_CS.config import ConfigurationManager
from Concrete_CS.components import DataValidation
from Concrete_CS import logger

STAGE_NAME= "Data Validation Stage"

def main():
    config= ConfigurationManager()
    data_validation_config= config.get_data_validation_config()
    data_validation= DataValidation(config= data_validation_config)
    data_validation.save_data()

if __name__=="__main__":
    try:
        logger.info(f">>>>>>Stage: {STAGE_NAME} Started<<<<<<")
        main()
        logger.info(f">>>>>>Stage: {STAGE_NAME} Completed<<<<<<")
    except Exception as e:
        logger.exception(e)
        raise e