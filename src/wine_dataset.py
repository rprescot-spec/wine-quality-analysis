from pathlib import Path
import pandas as pd

class WineDataset:
  '''
  Load and clean wine quality csv dataset. 

  This class loads the csv files, checks that the required columns are present, 
  removed duplicate rows, fills missing values with column averages, and stores
  the clean data for analysis.
  '''
  
  # Create WineDataset object
  def __init__(self, file_path, wine_type="unknown"):
    self.file_path = Path(file_path)
    self.wine_type = wine_type
    self.data = None
    self.required_columns = (
      "fixed acidity",
      "volatile acidity",
      "citric acid",
      "residual sugar",
      "chlorides",
      "free sulfur dioxide",
      "total sulfur dioxide",
      "density",
      "pH",
      "sulphates",
      "alcohol",
      "quality"
    )

  # Return description of dataset object
  def __str__(self):
    if self.data is None:
      return f"WineDataset({self.wine_type} wine, not loaded yet)"

    return f"WineDataset({self.wine_type} wine, {len(self.data)} rows loaded)"

  # Return number of rows in cleaned dataset
  def __len__(self):
    if self.data is None:
      return 0

    return len(self.data)

  # Load wine dataset from csv file
  def load_data(self):
    # Error if the csv file does not exist
    if not self.file_path.exists():
      raise FileNotFoundError(f"Could not find the file: {self.file_path}")

    # Split the data by semicolon as per dataset formatting
    self.data = pd.read_csv(self.file_path, sep=";")

    # Error if the csv file is empty
    if len(self.data) == 0:
      raise ValueError("The dataset is empty")

    return self.data

  # Check that the dataset has all required columns
  def check_required_columns(self):
    # Error if data is not loaded before checking columns
    if self.data is None:
      raise ValueError("Data must be loaded before checking columns")

    # List to store missing column names if any are found
    missing_columns = []

    for column in self.required_columns:
      if column not in self.data.columns:
        missing_columns.append(column)

    # Error if any columns are flagged as missing
    if len(missing_columns) > 0:
      raise ValueError(f"Missing required columns: {missing_columns}")

    return True

  # Clean the loaded wine dataset
  def clean_data(self):
    # Error is data is not loaded before cleaning
    if self.data is None:
      raise ValueError("Data must be loaded before cleaning")

    # Check required columns before cleaning
    self.check_required_columns()

    # Baseline cleaning summary
    cleaning_summary = {
      "starting_rows": len(self.data),
      "duplicates_removed": 0,
      "missing_values_filled": 0,
      "ending_rows": 0
    }

    # Identify number of initial row
    starting_rows = len(self.data)

    # Count amount of duplicates and update summary
    self.data = self.data.drop_duplicates()

    ending_rows_after_duplicates = len(self.data)
    cleaning_summary["duplicates_removed"] = starting_rows - ending_rows_after_duplicates

    # Fill in missing values with averages and update summary
    for column in self.required_columns:
      missing_count = self.data[column].isna().sum()

      if missing_count > 0:
        column_average = self.data[column].mean()
        self.data[column] = self.data[column].fillna(column_average)
        cleaning_summary["missing_values_filled"] += missing_count

    self.data["quality"] = self.data["quality"].round().astype(int)

    # Count the number of ending rows after cleaning and update summary
    cleaning_summary["ending_rows"] = len(self.data)

    return cleaning_summary

  # Load the csv file and clean the dataset
  def load_and_clean(self):
    self.load_data()
    summary = self.clean_data()
    return summary

  # Count number of wines with each quality score
  def get_quality_counts(self):
    # Error if data is not loaded yet
    if self.data is None:
      raise ValueError("Data must be loaded and cleaned first")

    quality_counts = {}

    for quality in self.data["quality"]:
      if quality in quality_counts:
        quality_counts[quality] += 1
      else:
        quality_counts[quality] =1

    return quality_counts