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
    
    for feature, weight in weights.items():
      if feature not in user_features:
        raise ValueError(f"Missing feature: {feature}")
    user_value=user_features[feature]
    ideal_value=high_quality_avg[feature]
    diff=abs(user_value-ideal_value)
    correlation=max(0,1-diff/(ideal_value+1e-5))
    score+=correlation*weight
    total_weight+=weight
    normal=score/total_weight
    prediction=3+(normalized*6)
    return round(prediction, 2)
    
def recommend(self,user_features, top_n=5):
  df=self.datacopy()
  features=[
    "alcohol",
    "volatile acidity",
    "citric acid",
    "residual sugar",
    "pH",
    "sulphates"
    ]
    distances=[]
    
    for row in df.iterrows():
      distance=0
    for feature in features:
      distance+=(row[feature]-user_features[feature])**2
      
    
    
