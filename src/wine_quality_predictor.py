from src.wine_analyzer import WineQualityAnalyzer

class WinePredictor:
"""
This uses the WineQualityAnanlyzer class from the analyzer function to predict the quality of a wine based on a user input or recommend a wine based on a user input of different quality standards.
"""
def __init__(self, analyzer: WineQualityAnalyzer):
  if not isinstance(analyzer, WineQualityAnalyzer):
    raise TypeError("The analyzer must be an object in WineQualityAnalyzer. try again.")

self.analyzer = analyzer
self.data = analyzer.data

def predict_quality(self, user_features):
  
