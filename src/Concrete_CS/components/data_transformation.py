from Concrete_CS.entity import DataTransformationConfig
from Concrete_CS import logger
import pandas as pd
from sklearn.model_selection import train_test_split

class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config= config
    def train_test_data(self):
        logger.info("Loading the data fot transformation...")
        data= pd.read_csv(self.config.data_transformation_path)
        training_data= data.iloc[:,1:-1]
        testing_data= data.iloc[:,-1]
        logger.info("transforming the data into training and testing sets...")
        X_train, X_test, y_train, y_test= train_test_split(training_data,
                                                           testing_data,
                                                           test_size=self.config.test_size,
                                                           random_state= self.config.random_state)
        logger.info("Splitting is completed...")
        logger.info("saving the training and testing datasets in differint files.")
        logger.info("four files are generated based on features and target values of training and testing datasets.")
        self.save_data(X_train, self.config.train_dataset_features_path)
        self.save_data(y_train, self.config.train_dataset_target_path)
        self.save_data(X_test, self.config.test_dataset_features_path)
        self.save_data(y_test, self.config.test_dataset_target_path)
    def save_data(self,save_file,save_file_path):
        logger.info("trying to save the file...")
        data= pd.DataFrame(save_file)
        data.to_csv(save_file_path)
        logger.info("given file is saved in csv format.")
        new_data= pd.read_csv(save_file_path)
        return new_data