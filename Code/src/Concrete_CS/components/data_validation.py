from Concrete_CS.entity import DataValidationConfig
from Concrete_CS import logger
import pandas as pd
from sklearn.impute import SimpleImputer

class DataValidation:
    def __init__(self, config: DataValidationConfig):
        self.config= config
    def handeling_missing_attributes(self):
        logger.info("Here we will deal with missing attributes.")
        logger.info("Missing attributes would be replaced by the median value of the given column.")
        concrete_raw_data= pd.read_excel(self.config.data_validation_path)
        imputed_concrete_data= SimpleImputer(strategy= self.config.simple_imputer_strategy)
        imputed_concrete_data= imputed_concrete_data.fit(concrete_raw_data)
        logger.info("The final dataset is generated.")
        return concrete_raw_data
    def save_data(self):
        logger.info("Trying to load the data in Data Frame format.")
        data= pd.DataFrame(self.handeling_missing_attributes())
        logger.info("Trying to save the data in csv format in the given path.")
        data.to_csv(self.config.updated_data_validation_path)
        logger.info("Trying to read the data.")
        new_data= pd.read_csv(self.config.updated_data_validation_path)
        logger.info("Here is your final saved data.")
        return new_data