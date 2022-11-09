from Concrete_CS.constant import *
from Concrete_CS.utils import read_yaml, create_directories
from Concrete_CS.entity import (DataIngestionConfig,
                                DataValidationConfig
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