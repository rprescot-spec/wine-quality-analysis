import numpy as np
import pandas as pd

from src.wine_dataset import WineDataset

class WineQualityAnalyzer:
  '''
  Analyze a cleaned WineDataset object. 

  Calculate summary statistics, fine top-quality wine, 
  compare averages, and group wine data by quality score. 
  '''
  
  def __init__(self, wine_dataset):
    '''
    Create a WineQualityAnalyzer object.
    '''
    if not isinstance(wine_dataset, WineDataset):
      raise TypeError("wine_dataset must be a WineDataset object")

    if wine_dataset.data is None:
      raise ValueError("The WineDataset must be loaded and cleaned before analysis")

    self.wine_dataset = wine_dataset
    self.data = wine_dataset.data
    self.wine_type = wine_dataset.wine_type

  def __str__(self):
    '''
    Return a readable description of the analyzer object
    '''
    return f"WineQualityAnalyzer({self.wine_type} wine, {len(self.data)} rows)"

  def __eq__(self, other):
    '''
    Compare two analyzers based on wine type and number of rows
    '''
    if not isinstance(other, WineQualityAnalyzer):
      return False

    return self.wine_type == other.wine_type and len(self.data) == len(other.data)

  def get_numeric_columns(self):
    '''
    Return a list of numeric columns in the dataset
    '''
    numeric_columns = []

    for column in self.data.columns:
      if pd.api.types.is_numeric_dtype(self.data[column]):
        numeric_columns.append(column)

    return numeric_columns

  def get_basic_summary(self):
    '''
    Calculate basic summary information about the wine dataset
    '''
    summary = {
      "wine_type": self.wine_type,
      "number_of_wines": len(self.data),
      "average_quality": round(np.mean(self.data["quality"]), 2),
      "average_alcohol": round(np.mean(self.data["alcohol"]), 2),
      "highest_quality": int(self.data["quality"].max()),
      "lowest_quality": int(self.data["quality"].min()),
    }

    return summary

  def get_column_average(self, column_name):
    '''
    Calculate the average value of a selected numeric column
    '''
    if column_name not in self.data.columns:
      raise ValueError(f"{column_name} is not a column in the dataset")

    if not pd.api.types.is_numeric_dtype(self.data[column_name]):
      raise ValueError(f"{column_name} must be numeric")

    return round(np.mean(self.data[column_name}), 3)

  def get_average_by_quality(self, column_name):
    '''
    Calculate the average of a selected column for each quality score
    '''
    if column_name not in self.data.columns:
      raise ValueError(f"{column_name} is not a column in the dataset")

    averages = {}

    quality_scores = sorted(set(self.data["quality"]))

    for quality in quality_scores:
      quality_rows = self.data[self.data["quality"] == quality]
      average[quality] = round(quality_rows[column_name].mean(), 3)

    return averages

  def get_top_wines(self, number_of_wines=5):
    '''
    Return the highest-quality wines in the dataset
    '''
    if number_of_wines <= 0:
      raise ValueError("number_of_wines must be greater than 0")

    top_wines = self.data.sort_values(
      by=["quality", "alcohol"],
      ascending=[False, False]
    )

    return top_wines.head(number_of_wines)

  def count_quality_categories(self):
    '''
    Count wines in low, medium, and high quality categories
    '''
    categories = {
      "low": 0,
      "medium": 0,
      "high": 0
    }

    for quality in self.data["quality"]:
      if quality <= 4:
        categories["low"] += 1
      elif quality <= 6:
        categories["medium"] += 1
      else:
        categories["high"] += 1

    return categories 

  def get_high_quality_features_summary(self):
    '''
    Calculate average feature values for high-quality wines
    '''
    high_quality_wines = self.data[self.data["quality"] >= 7]

    if len(high_quality_wines) == 0:
      raise ValueError("There are no high-quality wines in this dataset")

    important_columns - [
      "alcohol",
      "volatile acidity",
      "citric acid",
      "residual sugar",
      "pH",
      "sulphates"
    ]

    feature_summary = {}

    for column in important_columns:
      feature_summary[column] = round(high_quality_qines[column].mean(), 3)

    return feature_summary

  def compare_average_quality(self, other_analyzer):
    '''
    Compre the average quality of this dataset with another analyzer
    '''
    if not ininstance(other_analyzer, WineQualityAnalyzer):
      raise TypeError("other_analyzer must be a WineQualityAnalyzer object")

    this_average = self.get_basic_summary()["average_quality"]
    other_average = other_analyzer.get_basic_summary()["average_quality"]

    if this_average > other_average:
      return f"{self.wine_type} wine has a higher average quality than {other_analyzer.wine_type} wine"
    elif this_average < other_average:
      return f"{other_analyzer.wine_type} wine has a higher average quality than {self.wine_type} wine"
    else:
      return f"{self.wine_type} wine and {other_analyzer.wine_type} wine have the same average quality"
