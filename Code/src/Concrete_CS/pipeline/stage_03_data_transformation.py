from Concrete_CS.config import ConfigurationManager
from Concrete_CS.components import DataTransformation
from Concrete_CS import logger

STAGE_NAME= "Data Transformation Stage"

def main():
    config= ConfigurationManager()
    data_transformation_config= config.get_data_transformation_config()
    data_transformation= DataTransformation(config= data_transformation_config)
    data_transformation.train_test_data()

if __name__=="__main__":
    try:
        logger.info(f">>>>>>Stage: {STAGE_NAME} Started<<<<<<")
        main()
        logger.info(f">>>>>>Stage: {STAGE_NAME} Completed<<<<<<")
    except Exception as e:
        logger.exception(e)
        raise e