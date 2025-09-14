import os
import zipfile
import pandas as pd
from abc import ABC, abstractmethod

# Abstract base class for data ingestion
class DataIngestor(ABC):
    @abstractmethod
    def ingest(self, file_path: str) -> pd.DataFrame:
        "Abstract method to ingest data from a file."
        pass

# implement a concrete class for zip ingestion
class ZipDataIngestor(DataIngestor):
    def ingest(self,file_path:str)-> pd.DataFrame:
        # extract zip file and returns the content as a pandas DataFrame
        if not file_path.endswith('.zip'):
            raise ValueError('File is not a zip file')
        