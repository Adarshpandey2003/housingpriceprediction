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
        
        # Extract the zip file
        with zipfile.ZipFile(file_path,'r') as zip_ref:
            zip_ref.extractall('extracted_data')
        
        # find the extracted csv file (assuiming there's only one
        extracted_files=os.listdir('extracted_data')
        csv_files=[f for f in extracted_files if f.endswith('.csv')]

        if len(csv_files)==0:
            raise ValueError('No CSV file found in the zip archive')
        if len(csv_files)>1:
            raise ValueError('Multiple CSV files found in the zip archive')
        # read the csv file into a pandas DataFrame
        csv_file_path=os.path.join('extracted_data',csv_files[0])
        df=pd.read_csv(csv_file_path)

        # return the df
        return df
    
# implement a factory class to create dataIngestors

class DataIngestorFactory:
    @staticmethod
    def get_data_ingestor(file_extension:str)-> DataIngestor:
        # return the appropriate data ingestor based on file extension
        if file_extension=='.zip':
            return ZipDataIngestor()
        else:
            raise ValueError(f'No data ingestor found for file extension: {file_extension}')
        
# Example usage
if __name__=='__main__':
    # # Specify the file path
    # file_path = "/Users/ayushsingh/Desktop/end-to-end-production-grade-projects/prices-predictor-system/data/archive.zip"

    # # Determine the file extension
    # file_extension = os.path.splitext(file_path)[1]

    # # Get the appropriate DataIngestor
    # data_ingestor = DataIngestorFactory.get_data_ingestor(file_extension)

    # # Ingest the data and load it into a DataFrame
    # df = data_ingestor.ingest(file_path)

    # # Now df contains the DataFrame from the extracted CSV
    # print(df.head())  # Display the first few rows of the DataFrame
    pass