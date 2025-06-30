
import os
from src.datascience import logger
import pandas as pd
from src.datascience.entity.config_entity import (DataValidationConfig)
import mimetypes
import requests


class data_validation:

    def __init__(self, config: DataValidationConfig):
        self.config = config

    def data_validation_all_columns(self) -> bool:
        try:
            data = pd.read_csv(self.config.unzip_data_dir)
            all_col = list(data.columns)
            expected_col = self.config.all_schema.keys()

            missing_cols = [col for col in expected_col if col not in all_col]
            extra_cols = [col for col in all_col if col not in expected_col]

            validation_status = len(missing_cols) == 0 and len(extra_cols) == 0

            # ✅ Ensure the folder exists before writing status
            status_dir = os.path.dirname(self.config.STATUS_FILE)
            os.makedirs(status_dir, exist_ok=True)

            with open(self.config.STATUS_FILE, 'w') as f:
                f.write(f"validation status: {validation_status}\n")
                if not validation_status:
                    f.write(f"Missing columns: {missing_cols}\n")
                    f.write(f"Extra columns: {extra_cols}\n")

            logger.info(f"Validation completed. Status: {validation_status}")
            return validation_status

        except Exception as e:
            logger.error("Error during data validation", exc_info=True)
            raise e