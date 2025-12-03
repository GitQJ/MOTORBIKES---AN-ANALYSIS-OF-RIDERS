#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  3 09:19:21 2025

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

motogp_df=df[(df['class'] == 'MotoGP') & (df['season'] != 2025)]

###############################################################################
# Specific Performance Metrics:
###############################################################################
###############################################################################
# Which riders have the highest number of pole positions or fastest laps?
sns.set_palette('muted')
plt.style.use('seaborn-v0_8-talk')

ax1 = sns.barplot(data=df,y='rider_name',x='pole',estimator='sum',ci=None)
ax1.bar_label(ax1.containers[0], fontsize=12)

ax2 = sns.barplot(data=df,y='rider_name',x='pole',estimator='mean',ci=None)
ax2.bar_label(ax2.containers[1], fontsize=12,color='white')
plt.title("Marquez and Martin with highest Number and Mean Number of Pole in all classes",fontweight='bold')
plt.xlabel('Number of Pole')
plt.ylabel('Rider')
plt.legend(["Count", "Mean"], loc="upper right")
plt.show()

ax1 = sns.barplot(data=motogp_df,y='rider_name',x='pole',estimator='sum',ci=None)
ax1.bar_label(ax1.containers[0], fontsize=12)

ax2 = sns.barplot(data=motogp_df,y='rider_name',x='pole',estimator='mean',ci=None)
ax2.bar_label(ax2.containers[1], fontsize=12,color='white')
plt.title("Marquez and Martin with highest Number and Mean Number of Pole in MotoGP",fontweight='bold')
plt.xlabel('Number of Pole')
plt.ylabel('Rider')
plt.legend(["Count", "Mean"], loc="upper right")
plt.show()

sns.set_palette('muted')
plt.style.use('seaborn-v0_8-talk')

ax1 = sns.barplot(data=df,y='rider_name',x='fastest_lap',estimator='sum',ci=None)
ax1.bar_label(ax1.containers[0], fontsize=12)

ax2 = sns.barplot(data=df,y='rider_name',x='fastest_lap',estimator='mean',ci=None)
ax2.bar_label(ax2.containers[1], fontsize=12,color='white')
plt.title("Marquez and Acosta with highest Number and Mean Number of fastest lap in all classes",fontweight='bold')
plt.xlabel('Number of fastest lap')
plt.ylabel('Rider')
plt.legend(["Count", "Mean"], loc="upper right")
plt.show()

ax1 = sns.barplot(data=motogp_df,y='rider_name',x='fastest_lap',estimator='sum',ci=None)
ax1.bar_label(ax1.containers[0], fontsize=12)

ax2 = sns.barplot(data=motogp_df,y='rider_name',x='fastest_lap',estimator='mean',ci=None)
ax2.bar_label(ax2.containers[1], fontsize=12,color='white')
plt.title("Marquez and Bagnaia with highest Number and Mean Number of fastest lap in MotoGP",fontweight='bold')
plt.xlabel('Number of fastest lap')
plt.ylabel('Rider')
plt.legend(["Count", "Mean"], loc="upper right")
plt.show()


###############################################################################
###############################################################################
# What is the relationship between the number of races participated in and the points scored?

data=[]

i=0
for category in df['class'].unique():
    class_df = df[df['class'] == category]
    trace = go.Scatter(x = class_df['races_participated'],
                      y = class_df['placed'],
                      mode = 'markers',
                      name = category,
                      marker_symbol='circle',
                      marker_size=10,
                      hovertemplate="<b>Rider: </b>" + class_df['rider_name'] +
                      "<br><b>races_participated : </b>" + "%{x}" +
                      "<br><b>placed : </b>" + "%{y}")
    data.append(trace)

plotly.offline.plot({
    "data": data,
    "layout": go.Layout(title="From 13 race participated, there is no relationship with Final Rank",
                        xaxis_title='Number of race participated',
                        yaxis_title='Rank',
                        yaxis_autorange = 'reversed',
                        template="plotly_dark",
                        legend_title='Categories')})


data=[]

i=0
for category in df['class'].unique():
    class_df = df[df['class'] == category]
    trace = go.Scatter(x = class_df['races_participated'],
                      y = class_df['points'],
                      mode = 'markers',
                      name = category,
                      marker_symbol='circle',
                      marker_size=10,
                      hovertemplate="<b>Rider: </b>" + class_df['rider_name'] +
                      "<br><b>races_participated : </b>" + "%{x}" +
                      "<br><b>points : </b>" + "%{y}")
    data.append(trace)

plotly.offline.plot({
    "data": data,
    "layout": go.Layout(title="Unsurprisingly, the more race participated, the more points",
                        xaxis_title='Number of race participated',
                        yaxis_title='points',
                        template="plotly_dark",
                        legend_title='Categories')})


champion_df=df[df['world_championships'] == 1]
data=[]

i=0
for category in champion_df['class'].unique():
    class_df = champion_df[champion_df['class'] == category]
    trace = go.Scatter(x = class_df['races_participated'],
                      y = class_df['points'],
                      mode = 'markers',
                      name = category,
                      marker_symbol='circle',
                      marker_size=10,
                      hovertemplate="<b>Rider: </b>" + class_df['rider_name'] +
                      "<br><b>races_participated : </b>" + "%{x}" +
                      "<br><b>points : </b>" + "%{y}")
    data.append(trace)

plotly.offline.plot({
    "data": data,
    "layout": go.Layout(title="Champions generally participate in 18 races",
                        xaxis_title='Number of race participated',
                        yaxis_title='points',
                        template="plotly_dark",
                        legend_title='Categories')})



print("Minimum points for a Champion: ", min(champion_df['points']),
      "\nRider: ",champion_df[champion_df['points']==min(champion_df['points'])] ['rider_name'].values[0],
      "\nClass: ",champion_df[champion_df['points']==min(champion_df['points'])] ['class'].values[0],
      "\nSeason: ",champion_df[champion_df['points']==min(champion_df['points'])] ['season'].values[0])
print('\n')
print("Minimum wins for a Champion: ", min(champion_df['wins']),
      "\nRider: ",champion_df[champion_df['wins']==min(champion_df['wins'])] ['rider_name'].values[0],
      "\nClass: ",champion_df[champion_df['wins']==min(champion_df['wins'])] ['class'].values[0],
      "\nSeason: ",champion_df[champion_df['wins']==min(champion_df['wins'])] ['season'].values[0])











