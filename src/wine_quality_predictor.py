import random
from src.wine_analyzer import WineQualityAnalyzer

class WinePredictor:
  """
  This uses the WineQualityAanlyzer class from the analyzer function to predict the quality of a wine based on a user input or recommend a wine based on a user input of different quality standards.
  """
  def __init__(self, analyzer):
    #This makes sure the analyzer is an object that exists within the WineQualityAnalyzer so the functions can move forward.
    if not isinstance(analyzer, WineQualityAnalyzer):
      raise TypeError("The analyzer must be an object in WineQualityAnalyzer. Try again.")

    self.analyzer = analyzer
    self.data = analyzer.data

  def predict_quality(self, user_features):
    '''
    Estimate a wine quality score based on user-provided features.
    '''
    high_quality_avg = self.analyzer.get_high_quality_feature_summary()
    
    weights = {
      "alcohol": 2.0,
      "volatile acidity": 2.0,
      "sulphates": 1.5,
      "citric acid": 1.0,
      "residual sugar": 1.0,
      "pH": 1.0
      }

    score = 0
    total_weight = 0
    
    for feature, weight in weights.items():
      #This makes sure the wine feature specified by the user exists
      if feature not in user_features:
        raise ValueError(f"Missing feature: {feature}")
        
      user_value=user_features[feature]
      ideal_value=high_quality_avg[feature]

      #This finds the difference between the users' inputted feature values and the ideal value for that feature to determine if it is good or bad quality in relation to the ideal quality
      diff=abs(user_value-ideal_value)
      correlation=max(0,1-diff/(ideal_value+1e-5))

      score+=correlation*weight
      total_weight+=weight

    normalized=score/total_weight
    prediction=3+(normalized*6)
    return round(prediction, 2)
    
  def recommend(self,user_features, top_n=5):
    '''
    Recommend wines that are closest to the user's preferred feature values
    '''
    if top_n <= 0:
      raise ValueError("top_n must be greater than 0.")
    
    df=self.data.copy()
    features=[
      "alcohol",
      "volatile acidity",
      "citric acid",
      "residual sugar",
      "pH",
      "sulphates"
      ]

    for feature in features:
      if feature not in user_features:
        raise ValueError(f"Missing feature: {feature}")
    #'Distances' refers to the spaces moved in the dataset to match up with the wine that is being recommended
    distances=[]
    
    for index, row in df.iterrows():
      distance=0
    
      for feature in features:
        distance+=(row[feature]-user_features[feature])**2
      distances.append(distance)
    
    df["distance"]=distances

    return df.sort_values("distance").head(top_n)

  def generate_wine(self):
    """
    This generates  wine from the dataset for the user.
    """
    #This utilizes the Yield as a generator function, but makes sure it is not an infinite generation of wines
    for wine in wines.iterrows():
      yield wine

  def pick_random_wine(self):
    """
    This returns a completely random wine from the dataset using the Random function.
    """
    random_wine=self.data.sample(n-1)
    generator=self.wine_generator(random_wine)
    return next(generator)

  def wine_by_feature(
    self,
    minimum_quality=None,
    minimum_alcohol=None,
    maximum_acidity=None
  ):
    """
    This allows the user to generate a wine from the dataset based on their preferred features
    """
    filtered=self.data.copy()
    if minimum_quality is not None:
      filtered=filtered[
      filtered["quality"]>=minimum_quality
      ]
    if minimum_alcohol is not None:
      filtered=filtered[
      filtered["alcohol"]<= minimum_alcohol
      ]
    if maximum_acidity is not None:
      filtered=filtered[
      filtered["volatile acidity"]<= maximum_acidity
      ]
      if len(filtered)==0:
        raise ValueError("We do not have wines that match the given features. Try again.")
      random_wine=filtered.sample(n-1)
      generator=self.wine_generator(random_wine)
      return next(generator)

  def wine_selection(self, mode="random", **preferences):
    """
    This allows the user to choose if they want a random wine or one by their preferred features.
    """
    if mode=="random":
      return self.pick_random_wine()
    elif mode=="features":
      return self.wine_by_feature(**preferences)
    else:
      raise ValueError("The selected mode must be either random or features")
      
