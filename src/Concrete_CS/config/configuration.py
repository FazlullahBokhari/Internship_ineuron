from Concrete_CS.constant import *
from Concrete_CS.utils import read_yaml, create_directories
from Concrete_CS.entity import (DataIngestionConfig,
                                DataValidationConfig,
                                DataTransformationConfig,
                                ModelTrainerConfig
                                )
from pathlib import Path
import os

class ConfigurationManager:
    def __init__(self,
                config_filepath= CONFIG_FILE_PATH,
                params_filepath= PARAMS_FILE_PATH):
                self.config= read_yaml(config_filepath)
                self.params= read_yaml(params_filepath)
                create_directories([self.config.artifacts_root])

    def get_data_ingestion_config(self)-> DataIngestionConfig:
        config= self.config.data_ingestion
        create_directories([config.root_dir])
        data_ingestion_config= DataIngestionConfig(
            root_dir= config.root_dir,
            source_url= config.source_url,
            local_data_file= config.local_data_file)
        return data_ingestion_config

    def get_data_validation_config(self)-> DataValidationConfig:
        config= self.config.data_validation
        create_directories([config.root_dir])

        data_validation_config= DataValidationConfig(
                                root_dir= Path(config.root_dir),
                                data_validation_path= Path(config.data_validation_path),
                                updated_data_validation_path= Path(config.updated_data_validation_path),
                                simple_imputer_strategy=self.params.impute.params.strategy
                                )
        return data_validation_config
    def get_data_transformation_config(self)-> DataTransformationConfig:
        config= self.config.data_transformation
        create_directories([config.root_dir])

        data_transformation_config= DataTransformationConfig(
                                root_dir= Path(config.root_dir),
                                data_transformation_path= Path(config.data_transformation_path),
                                train_dataset_features_path= Path(config.train_dataset_features_path),
                                train_dataset_target_path= Path(config.train_dataset_target_path),
                                test_dataset_features_path= Path(config.test_dataset_features_path),
                                test_dataset_target_path= Path(config.test_dataset_target_path),
                                test_size= float(self.params.train_test_split.params.test_size),
                                random_state= int(self.params.train_test_split.params.random_state)
                                )
        return data_transformation_config
    def get_model_trainer_config(self)-> ModelTrainerConfig:
        config= self.config.model_trainer
        create_directories([config.root_dir])

        model_trainer_config= ModelTrainerConfig(
                              root_dir= Path(config.root_dir),
                              training_features_path= Path(config.training_features_path),
                              training_target_path= Path(config.training_target_path),
                              testing_features_path= Path(config.testing_features_path),
                              testing_target_path= Path(config.testing_target_path),
                              saved_file= Path(config.saved_file),
                              n_estimators= list(self.params.randomized_search.params.n_estimators),
                              max_features= list(self.params.randomized_search.params.max_features),
                              max_depth= list(self.params.randomized_search.params.max_depth),
                              min_samples_split= list(self.params.randomized_search.params.min_samples_split),
                              min_samples_leaf= list(self.params.randomized_search.params.min_samples_leaf),
                              scoring= str(self.params.randomized_search.scoring),
                              n_iter= int(self.params.randomized_search.n_iter),
                              cv= int(self.params.randomized_search.cv),
                              verbose= int(self.params.randomized_search.verbose),
                              random_state= int(self.params.randomized_search.random_state)
                              )
        return model_trainer_config
