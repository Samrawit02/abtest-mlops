from pathlib import Path


class Config:
  RANDOM_SEED = 42
  ASSETS_PATH = Path("../")
  REPO = "/Users/samrit/Documents/10Academy/week2/SmartAd contribution/abtest-ml/abtest-mlops"
  DATASET_FILE_PATH = "data/AdSmartABdata.csv"
  DATASET_PATH = ASSETS_PATH / "data"
  FEATURES_PATH = ASSETS_PATH / "features"
  MODELS_PATH = ASSETS_PATH / "models"
  METRICS_FILE_PATH = ASSETS_PATH / "metrics"