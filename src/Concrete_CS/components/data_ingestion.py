from Concrete_CS.entity import DataIngestionConfig
from Concrete_CS import logger
from Concrete_CS.utils import get_size
import pandas as pd
import urllib.request as request
import os
from pathlib import Path

class DataIngestion:
    def __init__(self,config: DataIngestionConfig):
        self.config = config
    def download_file(self):
        logger.info("Trying to download file...")
        if not os.path.exists(self.config.local_data_file):
            logger.info("Download started...")
            filename, headers= request.urlretrieve(
                url= self.config.source_url,
                filename= self.config.local_data_file)
            logger.info(f"File name: {filename} downloaded with following information: \n {headers}")
        else:
            logger.info(f"file is already exist with size {get_size(Path(self.config.local_data_file))}")
    def load_data(self):
        logger.info("file is loading")
        data_main= self.config.local_data_file
        return pd.read_excel(data_main)