# Wine Quality Analysis
#### Rachael Prescott, rprescot@stevens.edu, 20006395
#### Isabella Dona, idona@stevens.edu, 20006555
#### Overview
Our project analyzes the quality of wines from the UCI Wine Quality dataset and allows the data to be manipulated by the user.
The UCI dataset contains chemical measurements for major components of red and white wine variations, including acidity, sugar content, alcohol content, pH, and sulfur content, which can be used to determine the quality of the wine. The purpose of this project is to load and clean the wine data, analyze patterns in the quality, create visualizations, estimate wine quality using rule-based logic, and recommend wines based on user prefrences. 

##Dataset
Dataset used: UCI Wine Quality Dataset
Source: https://archive.ics.uci.edu/dataset/186/wine+quality
Files used:
- 'winequality-red.csv'
- 'winequality-white.csv'
- 'winequality.names'
These were all stored in the data folder

## Libraries used
This project uses the following python libraries:
- 'pandas' for reading and processing CSV data
- 'numpy' for numerical calculation
- 'matplotlib' for creating visualizations
- 'pytest' for testing project logic
- 'pathlib' for working with file paths
- 'random' for random wine selection

## File Structure
Wine_Quality_Analysis/
- Wine_Quality_Analysis.ipynb
- README.md
- requirments.txt
- data/
-   'winequality-red.csv'
-   'winequality-white.csv'
-   'winequality.names'
- src/
-   __init__.py
-   wine_dataset.py
-   wine_analyzer.py
-   wine_visuals.py
-   wine_quality_predictor.py
- tests/
-   test_wine_project.py
- figures/
-   generated graph images 

## Project Section
#### Project setup
Imports the required modules and checks that the dataset files are available
##### Load and Clean Dataset
Uses the WineDataset class to load the red and white wine CSV files, check required columns, remove duplicate rows, fill missing values if needed, and store a cleaning summary. 
##### Analyze the Cleaned Dataset
Uses the WineQualityAnalyzer to calculate summary statistics, compare red and white wines, group wines by quality category, find top-quality wines, and compare quality score sets. 
##### Visualize the Results
Use functions from wine_visuals.py to create graphs showing wine quality distributions and average alcohol level by quality score. 
##### Quality Prediction and Wine Recommendation
Used WinePredictor class. Predicts wine quality based on features input by the user and recommends similar wines, recommends a wine based on single-feature preferences, and can randomly choose a wine from the dataset for the user.
##### Exception Handling
Dispalys examples of handling exceptions, including missing files, invalid columsn, and missing user input features.
##### PyTest Testing
Uses Pytest to test important parts of the prject, including dataset loading, analyzer summaries, invalid input handling, and quality prediction.
#### Running the Program
1. Download the repository
2. Install the required libraries
3. Open the main notebook
4. Run all the notebook cells in order

## Contributions
#### Rachael
- Created the WineDataset class for loading, checking and cleaning the dataset. 
- Implemented data I/O using the UCI red and white wine CSV files.
- Created the WineQualityAnalyzer class for summary statistics, quality comparisons, and set-based quality score analysis.
- Created visualizations using Matplotlib.
- Added exception handling examples in the notebook.
- Helped organize the main notebook workflow and project documentation.
#### Isabella
- Created the WinePredictor class for rule-based quality prediction and wine recommendation.
- Added user-preference functionality for recommending wines based on selected features.
- Added random wine selection and generator-based wine selection.
- Created and ran Pytest tests to validate project logic.
- Helped update documentation and final project organization.
