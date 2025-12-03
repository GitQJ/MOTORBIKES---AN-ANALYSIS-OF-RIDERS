#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov  2 21:32:49 2025

@author: Quentin
"""

import plotly
import plotly.graph_objs as go
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("/Users/Quentin/Desktop/Hdip Data Science and Analytics/Year 1/Semester 3/DATA8008 - Data Visualisation & Analytics/Assignment 1/RidersSummary.csv")

df=df[(df['class'] == 'MotoGP') & (df['season'] != 2025)]

df['motorcycle']= df['motorcycle'].replace('Suzuki GSX-RR','Suzuki')
df['motorcycle']= df['motorcycle'].replace('Yamaha YZR-M1','Yamaha')
df['motorcycle']= df['motorcycle'].replace('Aprilia RS-GP','Aprilia')
df['motorcycle']= df['motorcycle'].replace('Honda RC213V','Honda')
df['motorcycle']= df['motorcycle'].replace('Ducati Desmosedici GP23','Ducati')

###############################################################################
# Motorcycle Analysis:
# Which motorcycle brand has the most wins or podium finishes in the dataset?
sns.set_palette('muted')
plt.style.use('seaborn-v0_8-talk')

ax1 = sns.barplot(data=df,y='motorcycle',x='wins',estimator='sum',ci=None)
ax1.bar_label(ax1.containers[0], fontsize=12)

ax2 = sns.barplot(data=df,y='motorcycle',x='wins',estimator='mean',ci=None)
ax2.bar_label(ax2.containers[1], fontsize=12,color='white')
plt.title("Honda and Ducati dominating MotoGP",fontweight='bold')
plt.xlabel('Number of wins')
plt.ylabel('Motorcycle')
plt.legend(["Count", "Mean"], loc="upper right")
plt.show()

sns.set_palette('muted')
plt.style.use('seaborn-v0_8-talk')

ax1 = sns.barplot(data=df,y='motorcycle',x='podium',estimator='sum',ci=None)
ax1.bar_label(ax1.containers[0], fontsize=12)

ax2 = sns.barplot(data=df,y='motorcycle',x='podium',estimator='mean',ci=None)
ax2.bar_label(ax2.containers[1], fontsize=12,color='white')
plt.title("MotoGP podiums dominated by Ducati followed by Honda and Yamaha",fontweight='bold')
plt.xlabel('Number of podiums')
plt.ylabel('Motorcycle')
plt.legend(["Count", "Mean"], loc="upper right")
plt.show()


###############################################################################
###############################################################################
# What is the trend of wins for each motorcycle over the seasons?
data=[]

shapes = ['square','circle','triangle-up','diamond','cross','triangle-down']

motorcycle_group = df.groupby(['motorcycle','season'])['wins'].sum()

motorcycle_lists =[]

i=0
for index in motorcycle_group.index:
    motorcycle_season_wins = [index[0],index[1],motorcycle_group[i]]
    motorcycle_lists.append(motorcycle_season_wins)
    i+=1

motorcycle_season_wins_df = pd.DataFrame(motorcycle_lists,columns=['motorcycle','season','wins'])

i=0
for motorcycle in motorcycle_season_wins_df['motorcycle'].unique():

    motorcycle_df = motorcycle_season_wins_df[motorcycle_season_wins_df['motorcycle'] == motorcycle]
    trace = go.Scatter(x = motorcycle_df['season'],
                       y = motorcycle_df['wins'],
                       mode = 'lines+markers',
                       name = motorcycle,
                       marker_symbol=shapes[i],
                       marker_size=15)
    i+=1
    data.append(trace)

plotly.offline.plot({
    "data": data,
    "layout": go.Layout(title="Ducati overtaking the MotoGP since 2021",
                        xaxis_title='Season',
                        yaxis_title='Wins',
                        template="plotly_dark",
                        # hovermode="x unified",
                        legend_title='Riders')})

data=[]
motorcycle_group = df.groupby(['motorcycle','season'])['wins'].count()
motorcycle_lists = []

i=0
for index in motorcycle_group.index:
    motorcycle_team = [index[0],index[1],motorcycle_group[i]]
    motorcycle_lists.append(motorcycle_team)
    i+=1

motorcycle_team_df = pd.DataFrame(motorcycle_lists,columns=['motorcycle','season','nb_of_bikes'])

i=0
for motorcycle in motorcycle_team_df['motorcycle'].unique():

    motorcycle_df = motorcycle_team_df[motorcycle_team_df['motorcycle'] == motorcycle]
    trace = go.Scatter(x = motorcycle_df['season'],
                       y = motorcycle_df['nb_of_bikes'],
                       mode = 'lines+markers',
                       name = motorcycle,
                       marker_symbol=shapes[i],
                       marker_size=15)
    i+=1
    data.append(trace)

plotly.offline.plot({
    "data": data,
    "layout": go.Layout(title="Ducati engaging many more bikes than its competitors",
                        xaxis_title='Season',
                        yaxis_title='Number of Bikes',
                        template="plotly_dark",
                        # hovermode="x unified",
                        legend_title='Riders')})