# -*- coding: utf-8 -*-
"""
Created on Wed May 11 08:09:47 2022

@author: samrit
"""

import os
import sys
import pandas as pd
import numpy as np


sys.path.append(os.path.abspath(os.path.join('../')))

class Outlier:
    
    def __init__(self, df: pd.DataFrame)-> None:
        self.df= df
        
    def count_outliers(self, Q1, Q3, IQR):
        iqr_rule = IQR * 1.5
        temp_df = (self.df < (Q1 - iqr_rule)) | (self.df > (Q3 + iqr_rule))
        return [len(temp_df[temp_df[col] == True]) for col in temp_df]

    def calc_skew(self):
        return [self.df[col].skew() for col in self.df]

    def percentage(self, list):
        return [str(round(((value/self.df.shape[0]) * 100), 2)) + '%' for value in list]

    def remove_outliers(self, columns):
        for col in columns:
            Q1, Q3 = self.df[col].quantile(0.25), self.df[col].quantile(0.75)
            IQR = Q3 - Q1
            iqr_rule = IQR * 1.5
            lower = Q1 - iqr_rule
            upper= Q3 + iqr_rule
            
            self.df = self.df.drop(self.df[self.df[col] > upper].index)
            self.df = self.df.drop(self.df[self.df[col] < lower].index)
            
    def replace_outliers_with_iqr(self, columns):
            for col in columns:
                Q1, Q3 = self.df[col].quantile(0.25), self.df[col].quantile(0.75)
                IQR = Q3 - Q1
                cut_off = IQR * 1.5
                lower, upper = Q1 - cut_off, Q3 + cut_off
    
                self.df[col] = np.where(self.df[col] > upper, upper, self.df[col])
                self.df[col] = np.where(self.df[col] < lower, lower, self.df[col])


    def getOverview(self) -> None:

        Q1 = self.df.quantile(0.25)
        Q3 = self.df.quantile(0.75)
        IQR = Q3 - Q1
        skew = self.calc_skew()
        outliers = self.count_outliers(Q1, Q3, IQR)
        stat = self.df.describe()
        min = [stat[column]['min'] for column in stat]
        max = [stat[column]['max'] for column in stat]
        mean = [stat[column]['mean'] for column in stat]
        median = [stat[column]['50%'] for column in stat]
        iqr_rule= IQR *1.5
        lower = Q1 - iqr_rule
        upper = Q3 + iqr_rule
        

        columns = [
            'label',
            'Q1',
            'median',
            'Q3',
            'IQR',
            'skew',
            'number_of_outliers',
            'percentage_of_outliers',
            'min_value',
            'max_value',
            'mean',
            'lower',
            'upper',]
        data = zip(
            [column for column in self.df],
            Q1,
            median,
            Q3,
            IQR,
            skew,
            outliers,
            self.percentage(outliers),
            min,
            max,
            mean,
            lower,
            upper
        )
        new_df = pd.DataFrame(data=data, columns=columns)
        new_df.set_index('label', inplace=True)
        return new_df