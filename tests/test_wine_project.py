import pytest 

from src.wine_dataset import WineDataset
from src.wine_analyzer import WineQualityAnalyzer
from src.wine_quality_predictor import WinePredictor

def test_red_wine_dataset_loads_and_cleans():
  '''
  Test that the red wine dataset loads and cleans successfully
  '''
  red_wine = WineDataset("data/winequality-red.csv", wine_type="red")
  summary = red_wine.load_and_clean()

  assert len(red_wine) > 0
  assert summary["starting_rows"] == 1599
  assert summary["ending_rows"] == 1359
  assert "quality" in red_wine.data.columns

def test_quality_counts_return_dictionary():
  '''
  test that quality counts are returned as a dictionary
  '''
  red_wine = WineDataset("data/winequality-red.csv", wine_type="red")
  red_wine.load_and_clean()

  quality_counts = red_wine.get_quality_counts()

  assert isinstance(quality_counts, dict)
  assert 5 in quality_counts
  assert quality_counts[5] > 0

def test_analyzer_basic_summary():
  '''
  Test that WineQualityAnalyzer returns correct summary information
  '''
  red_wine = WineDataset("data/winequality-red.csv", wine_type="red")
  red_wine.load_and_clean()

  analyzer = WineQualityAnalyzer(red_wine)
  summary = analyzer.get_basic_summary()

  assert summary["wine_type"] == "red"
  assert summary["number_of_wines"] == len(red_wine)
  assert summary["highest_quality"] >= summary["lowest_quality"]

def test_invalid_column_raises_value_error():
  '''
  test that an invalid column name raises a ValueError
  '''
  red_wine = WineDataset("data/winequality-red.csv", wine_type="red")
  red_wine.load_and_clean()

  analyzer = WineQualityAnalyzer(red_wine)

  with pytest.raises(ValueError):
    analyzer.get_column_average("not a real column")

def test_predictor_estimates_quality_score():
  '''
  test that WinePredictor returns a quality score in a reasonable range
  '''
  red_wine = WineDataset("data/winequality-red.csv", wine_type="red")
  red_wine.load_and_clean()

  analyzer = WineQualityAnalyzer(red_wine)
  predictor = WinePredictor(analyzer)

  user_wine = {
    "alcohol": 11.5,
    "volatile acidity": 0.35,
    "sulphates": 0.7,
    "citric acid": 0.35,
    "residual sugar": 2.0,
    "pH": 3.3
  }

  estimated_quality = predictor.predict_quality(user_wine)

  assert estimated_quality >= 3
  assert estimated_quality <= 9

def test_predictor_missing_feature_raises_value_error():
  '''
  test that missing user input feature raises a ValueError
  '''
  red_wine = WineDataset("data/winequality-red.csv", wine_type="red")
  red_wine.load_and_clean()

  analyzer = WineQualityAnalyzer(red_wine)
  predictor = WinePredictor(analyzer)

  incomplete_user_wine = {
    "alcohol": 11.5,
    "volatile acidity": 0.35
  }

  with pytest.raises(ValueError):
    predictor.predict_quality(incomplete_user_wine)
