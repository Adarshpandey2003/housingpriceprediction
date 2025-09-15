from abc import ABC, abstractmethod
import pandas as pd


# Abstract base class for basic data inspection

class DataInspectionStrategy(ABC):
    @abstractmethod
    def inspect(self, df: pd.DataFrame):
        "Abstract method to inspect data in a DataFrame."
        pass
# Concrete class for basic data inspection
class DataTypesInspectionStrategy(DataInspectionStrategy):
    def inspect(self, df: pd.DataFrame):
        # Inspect and print data types of each column in the DataFrame
        print('\nData types and non-null counts of each column:')
        print(df.dtypes)

# concrete strategy for summary statistics inspection
class SummaryStatisticsInspectionStrategy(DataInspectionStrategy):
    def inspect(self, df:pd.DataFrame):
        # print summary statistics of numerical columns in the DataFrame

        print('\nSummary statistics of numerical columns:')
        print(df.describe())
        print('\nSummary statistics of categorical columns:')
        print(df.describe(include=["O"]))

# context class to use the inspection strategies
class DataInspector:
    def __init__(self,strategy:DataInspectionStrategy):
        # initialize with a specific inspection strategy
        self._strategy=strategy
    def set_strategy(self,strategy:DataInspectionStrategy):
        # set a new inspection strategy
        self._strategy=strategy
    
    def execute_inspection(self,df:pd.DataFrame):
        # execute the inspection using the current strategy
        self._strategy.inspect(df)

# Example usage
if __name__ == "__main__":
    # Example usage of the DataInspector with different strategies.

    # Load the data
    # df = pd.read_csv('../extracted-data/your_data_file.csv')

    # Initialize the Data Inspector with a specific strategy
    # inspector = DataInspector(DataTypesInspectionStrategy())
    # inspector.execute_inspection(df)

    # Change strategy to Summary Statistics and execute
    # inspector.set_strategy(SummaryStatisticsInspectionStrategy())
    # inspector.execute_inspection(df)
    pass
