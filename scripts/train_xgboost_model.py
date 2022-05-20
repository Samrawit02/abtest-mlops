# -*- coding: utf-8 -*-
"""
Created on Fri May 13 10:16:34 2022

@author: samrit
"""


import pickle
from config import Config
from xgboost import XGBClassifier
import train_model

'''
  simple script for training XGBoost using TrainModel class
'''

def model(param):
  model = XGBClassifier(random_state=42, eval_metric='logloss', **param)
  return model



final_model = train_model(model, "XGBoost")

# final_model, best_param, avg_metrics = train_model.get_optimal_model()

pickle.dump(final_model, open(str(Config.MODELS_PATH / "xgboost_model.pickle"), "wb"))
