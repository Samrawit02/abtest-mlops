import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
import dvc.api
import mlflow
# from config import Config
from pathlib import Path

RANDOM_SEED = 42
ASSETS_PATH = Path("../")
REPO = "C:/Users/samrit/Documents/10Academy/week2/SmartAd contribution/abtest-ml/abtest-mlops"
DATASET_FILE_PATH = "data/AdSmartABdata.csv"
DATASET_PATH = "data"
FEATURES_PATH = ASSETS_PATH / "features"
MODELS_PATH = ASSETS_PATH / "models"
METRICS_FILE_PATH = ASSETS_PATH / "metrics"

np.random.seed(RANDOM_SEED)
version = 'v1'  # git tag

data_url = dvc.api.get_url(path=str(DATASET_FILE_PATH), repo=str(REPO), rev=version)

df = pd.read_csv(data_url, sep=',')


df = df.query("not (yes == 0 & no == 0)")
df_train, df_test = train_test_split(df, test_size=0.1, random_state=RANDOM_SEED,)

# Log data params
mlflow.log_param('data_url', data_url)
mlflow.log_param('input_rows', df.shape[0])
mlflow.log_param('input_cols', df.shape[1])

df_train.to_csv(str( "C:/Users/samrit/Documents/10Academy/week2/SmartAd contribution/abtest-ml/abtest-mlops/data/train.csv"), index=None)
df_test.to_csv(str("C:/Users/samrit/Documents/10Academy/week2/SmartAd contribution/abtest-ml/abtest-mlops/data/test.csv"), index=None)