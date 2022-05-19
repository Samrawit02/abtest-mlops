# -*- coding: utf-8 -*-
"""
Created on Tue May 17 15:15:01 2022

@author: samrit
"""

import os
import sys
import pandas as pd

sys.path.append(os.path.abspath(os.path.join('../')))


#my_logger = log.get_logger("RWDataset")


class RWDataset():

  def __init__(self):
    pass

  def save_csv(self, df, csv_path, index=False):
   # try:
      df.to_csv(csv_path, index=index)
     # my_logger.info("file saved as csv")

   # except Exception:
    # exception("save failed")

  def read_csv(self, csv_path, missing_values=[]):
  #  try:
      df = pd.read_csv(csv_path, na_values=missing_values)
    #  my_logger.debug("file read as csv")
      return df
  #  except FileNotFoundError:
   #   my_logger.exception("file not found")