import urllib.request as requests
import os
from src.datascience import logger
import zipfile 
from src.datascience.entity.config_entity import (data_ingestion_config)
import mimetypes
import requests

class data_ingestion:

    def __init__(self , config: data_ingestion_config):
        self.config = config


    def download_file(self):
     if not os.path.exists(self.config.local_data_file):
        headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.5993.117 Safari/537.36"
        }

        response = requests.get(self.config.source_url, headers=headers, stream=True, allow_redirects=True)

        # Check response
        content_type = response.headers.get("Content-Type", "")
        if "zip" not in content_type:
            raise ValueError(f"Expected a zip file but got content-type: {content_type}")

        os.makedirs(os.path.dirname(self.config.local_data_file), exist_ok=True)
        with open(self.config.local_data_file, "wb") as f:
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:
                    f.write(chunk)

        logger.info(f"Downloaded ZIP to {self.config.local_data_file}")

     else:
        logger.info(f"{self.config.local_data_file} already exists")    




    # def download_file(self):
    #     if not os.path.exists(self.config.local_data_file):
    #         filename , header = requests.urlretrieve(
    #             url = self.config.source_url,
    #             filename=self.config.local_data_file
    #         )
    #         logger.info(f'{filename} download with following info {header} !')

    #     else:
    #         logger.info(f'file already exists')    

    def extract_zip_file(self):
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path , exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file , 'r')  as zip_ref:
            zip_ref.extractall(unzip_path)    