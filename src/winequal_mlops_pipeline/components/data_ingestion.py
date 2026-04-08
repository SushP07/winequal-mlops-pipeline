import os 
import urllib.request as request
from src.winequal_mlops_pipeline import logger
import zipfile
from src.winequal_mlops_pipeline.entity.config_entity import (DataIngestionConfig)

## component - Data ingestion component
class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config
    ## downloading the file from source URL to local data file
    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            filename, headers = request.urlretrieve(url = self.config.source_URL, filename = self.config.local_data_file)
            logger.info(f"{filename} downloaded with following info: \n{headers}")
        else:
            logger.info(f"File already exists of size: {os.path.getsize(self.config.local_data_file)} bytes")

    # Extract zip file
    def extract_zip_file(self):
        """ Extract the zip file
            zip_file_path: str
            unzip_dir: str
            Function returns: None"""

        unzip_path  = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok = True)
        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)



