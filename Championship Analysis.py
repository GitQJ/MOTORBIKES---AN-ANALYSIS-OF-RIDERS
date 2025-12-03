#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  3 09:38:41 2025

@author: Quentin
"""

import plotly
import plotly.graph_objs as go
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

df = pd.read_csv("/Users/Quentin/Desktop/Hdip Data Science and Analytics/Year 1/Semester 3/DATA8008 - Data Visualisation & Analytics/Assignment 1/RidersSummary.csv")

df=df[df['season'] != 2025]

motogp_df=df[df['class'] == 'MotoGP']

# Champion Analysis:
    
###############################################################################
###############################################################################
# Which riders have won the most world championships, and how many points did it take them to achieve each championship?
sns.set_palette('muted')
plt.style.use('seaborn-v0_8-talk')

ax1 = sns.barplot(data=df,y='rider_name',x='world_championships',estimator='sum',ci=None)
ax1.bar_label(ax1.containers[0], fontsize=12)

ax2 = sns.barplot(data=df,y='rider_name',x='world_championships',estimator='mean',ci=None)
ax2.bar_label(ax2.containers[1], fontsize=12,color='white')
plt.title("Marquez awarded champion 8 times, almost 50% of the time in all classes",fontweight='bold')
plt.xlabel('Number of World Championship')
plt.ylabel('Rider')
plt.legend(["Count", "Mean"], loc="upper right")
plt.show()

sns.set_palette('muted')
plt.style.use('seaborn-v0_8-talk')

ax1 = sns.barplot(data=motogp_df,y='rider_name',x='world_championships',estimator='sum',ci=None)
ax1.bar_label(ax1.containers[0], fontsize=12)

ax2 = sns.barplot(data=motogp_df,y='rider_name',x='world_championships',estimator='mean',ci=None)
ax2.bar_label(ax2.containers[1], fontsize=12,color='white')
plt.title("Marquez awarded champion 6 times, 50% of the time in MotoGP",fontweight='bold')
plt.xlabel('Number of World Championship')
plt.ylabel('Rider')
plt.legend(["Count", "Mean"], loc="upper right")
plt.show()

marquez_df = df[df['rider_name'] == 'Marc Marquez']

data=[]

trace = go.Scatter(x = marquez_df['season'],
                   y = marquez_df['points'],
                   name='Points',
                   mode = 'lines')
data.append(trace)

i=0
names = ['No','Yes']

for rank in marquez_df['world_championships'].unique():
    final_df = marquez_df[marquez_df['world_championships'] == rank]
    trace = go.Scatter(x = final_df['season'],
                      y = final_df['points'],
                      mode = 'markers',
                      name = names[i],
                      marker_symbol='circle',
                      marker_size=10,
                      hovertemplate="<b>Class: </b>" + marquez_df['class'] +
                      "<br><b>Season: </b>" + "%{x}" +
                      "<br><b>Points : </b>" + "%{y}")
    data.append(trace)
    i+=1

plotly.offline.plot({
    "data": data,
    "layout": go.Layout(title="Marquez awarded champion if earning more than 298 points, except in 2024",
                        xaxis_title='Season',
                        yaxis_title='Points',
                        template="plotly_dark",
                        legend_title='World Champion')})




