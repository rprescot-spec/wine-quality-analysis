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
  highest_quality_avg = self.analyzer.get_high_quality_feature_summary()

  weights = {
    "alchohol": 2.0,
    "voltaile acidity": 2.0,
    "sulphates": 1.5,
    "citric acid" 1.0,
    "residual sugar": 1.0,
    "pH": 1.0
    }

    score = 0
    total_weight = 0
    
