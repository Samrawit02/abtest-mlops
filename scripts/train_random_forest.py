import pickle

from sklearn.ensemble import RandomForestClassifier

from config import Config
from train_model import TrainModel

"""
  simple script for training logistic regression using TrainModel class
"""


def model(param):
    model = RandomForestClassifier(random_state=42)
    return model


params = ["newton-cg", "lbfgs", "liblinear", "sag", "saga"]

train_model = TrainModel(model, "Random forest", params=params)

final_model, best_param, avg_metrics = train_model.get_optimal_model()

pickle.dump(
    final_model,
    open(str(Config.MODELS_PATH / "random_forest_model.pickle"), "wb"),
)
