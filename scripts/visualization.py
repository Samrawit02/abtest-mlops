# -*- coding: utf-8 -*-
"""
Created on Fri May 13 10:16:34 2022

@author: samrit
"""

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import plotly.express as px



def plot_univariate(df:pd.DataFrame, x, title):
    plt.figure(figsize=(12, 6))
    sns.countplot(data=df, x=x)
    plt.title(title)
    plt.xticks(rotation=45)
    plt.show()

def bi_plot(df:pd.DataFrame, x_col:str, y_col:str, title:str, rotation=0):
    plt.figure(figsize=(12, 6))
    sns.countplot(data=df, x=x_col , hue = y_col)
    plt.title(title)
    plt.xticks(rotation=rotation)
    plt.show()
    
def hist(sr):
    x = ["Id: " + str(i) for i in sr.index]
    fig = px.histogram(x=x, y=sr.values)
    fig.show()
   

def plot_scatter(df: pd.DataFrame, x_col: str, y_col:str, title: str) -> None:
    plt.figure(figsize=(12, 7))
    sns.scatterplot(data = df, x=x_col, y=y_col)
    plt.title(title, size=20)
    plt.xticks(fontsize=14)
    plt.yticks(fontsize=14)
    plt.show()

def plot_heatmap(df:pd.DataFrame, title:str, cmap='Reds')->None:
    plt.figure(figsize=(12,7))
    sns.heatmap(df, annot=True, cmap=cmap, vmin=0, vmax=1, fmt='.2f', linewidths=.7, cbar=True )
    plt.title(title, size=20, fontweight='bold')
    plt.show()