from pathlib import Path
import matplotlib.pyplot as plt

def plot_quality_distribution(analyzer, output_folder="figures"):
  '''
  Create a bar chart showing how many wines have each quality score
  '''
  output_path = Path(output_folder)
  output_path.mkdir(parents=True, exist_ok=True)

  quality_counts = analyzer.wine_dataset.get_quality_counts()

  quality_scores = sorted(quality_counts.keys())
  counts = []

  for quality in quality_scores:
    counts.append(quality_counts[quality])

  plt.figure(figsize=(8, 5))
  plt.bar(quality_scores, counts)
  plt.xlabel("Wine Quality Score")
  plt.ylabel("Number of Wines")
  plt.title(f"{analyzer.wine_type.title()} Wine Quality Distribution")
  plt.tight_layout()

  file_name = output_path / f"{analyzer.wine_type}_quality_distribution.png"
  plt.savefig(file_name)
  plt.show()
  plt.close()

  return file_name

def plot_average_by_quality(analyzer, column_name, output_folder="figures"):
  '''
  Create a line graph showing the average value of a column by quality score
  '''
  output_path = Path(output_folder)
  output_path.mkdir(parents=True, exist_ok=True)

  averages = analyzer.get_average_by_quality(column_name)

  quality_scores = sorted(averages.keys())
  average_values = []

  for quality in quality_scores:
    average_values.append(averages[quality])

  plt.figure(figsize=(8, 5))
  plt.plot(quality_scores, average_values, marker="o")
  plt.xlabel("Wine Quality Score")
  plt.ylabel(f"Average {column_name}")
  plt.title(f"Average {column_name.title()} by {analyzer.wine_type.title()} Wine Quality")
  plt.tight_layout()

  safe_column_name = column_name.replace(" ", "_")
  file_name = output_path / f"{analyzer.wine_type}_{safe_column_name}_by_quality.png"
  plt.savefig(file_name)
  plt.show()
  plt.close()

  return file_name
