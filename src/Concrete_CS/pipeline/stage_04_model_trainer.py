from Concrete_CS.config import ConfigurationManager
from Concrete_CS.components import ModelTrainer
from Concrete_CS import logger

STAGE_NAME= "Model Trainer Stage"

def main():
    config= ConfigurationManager()
    model_trainer_config= config.get_model_trainer_config()
    model_trainer= ModelTrainer(config= model_trainer_config)
    model_trainer.save_file()

if __name__=="__main__":
    try:
        logger.info(f">>>>>>Stage: {STAGE_NAME} Started<<<<<<")
        main()
        logger.info(f">>>>>>Stage: {STAGE_NAME} Completed<<<<<<")
    except Exception as e:
        logger.exception(e)
        raise e