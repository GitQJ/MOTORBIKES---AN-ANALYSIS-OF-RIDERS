#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov  2 09:57:04 2025

@author: Quentin
"""



import plotly
import plotly.graph_objs as go
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("/Users/Quentin/Desktop/Hdip Data Science and Analytics/Year 1/Semester 3/DATA8008 - Data Visualisation & Analytics/Assignment 1/RidersSummary.csv")
df=df[df['season'] != 2025]
###############################################################################
# Rider Performance and Career Trajectory

# How has a rider's performance evolved across different classes (Moto3, Moto2, MotoGP) over their career?
###############################################################################
# Riders wins over seasons

motogp_df=df[(df['class'] == 'MotoGP') & (df['season'] != 2025)]

motogp_champions = motogp_df[motogp_df['world_championships'] == 1]['rider_name'].unique()

_2024df = df[df['season'] != 2025]

data=[]

shapes = ['square','circle','triangle-up','diamond','cross']

i=0
for rider in motogp_champions:
    rider_df = _2024df[_2024df['rider_name'] == rider]
    trace = go.Scatter(x = rider_df['season'],
                       y = rider_df['wins'],
                       mode = 'lines+markers',
                       name = rider,
                       marker_symbol=shapes[i],
                       marker_size=15,
                       hovertemplate="<b>Class: </b>" + rider_df['class'] +
                       "<br><b>Season : </b>" + "%{x}" +
                       "<br><b>Wins : </b>" + "%{y}")
    i+=1
    data.append(trace)

plotly.offline.plot({
    "data": data,
    "layout": go.Layout(title="Riders experiencing a drop in wins after going superior class",
                        xaxis_title='Season',
                        yaxis_title='Wins',
                        template="plotly_dark",
                        hovermode="x unified",
                        legend_title='Riders')})


# ###############################################################################
# Riders points over seasons

motogp_df=df[(df['class'] == 'MotoGP') & (df['season'] != 2025)]

motogp_champions = motogp_df[motogp_df['world_championships'] == 1]['rider_name'].unique()

_2024df = df[df['season'] != 2025]

data=[]

shapes = ['square','circle','triangle-up','diamond','cross']

i=0
for rider in motogp_champions:
    rider_df = _2024df[_2024df['rider_name'] == rider]
    trace = go.Scatter(x = rider_df['season'],
                       y = rider_df['points'],
                       mode = 'lines+markers',
                       name = rider,
                       marker_symbol=shapes[i],
                       marker_size=15,
                       hovertemplate="<b>Class: </b>" + rider_df['class'] +
                       "<br><b>Season : </b>" + "%{x}" +
                       "<br><b>Points : </b>" + "%{y}")
    i+=1
    data.append(trace)

plotly.offline.plot({
    "data": data,
    "layout": go.Layout(title="Riders experiencing a drop in points after going superior class",
                        xaxis_title='Season',
                        yaxis_title='Points',
                        template="plotly_dark",
                        hovermode="x unified",
                        legend_title='Riders')})

###############################################################################
# Riders rank over seasons

motogp_df=df[(df['class'] == 'MotoGP') & (df['season'] != 2025)]

motogp_champions = motogp_df[motogp_df['world_championships'] == 1]['rider_name'].unique()

_2024df = df[df['season'] != 2025]

data=[]

shapes = ['square','circle','triangle-up','diamond','cross']

i=0
for rider in motogp_champions:
    rider_df = _2024df[_2024df['rider_name'] == rider]
    trace = go.Scatter(x = rider_df['season'],
                       y = rider_df['placed'],
                       mode = 'lines+markers',
                       name = rider,
                       marker_symbol=shapes[i],
                       marker_size=15,
                       hovertemplate="<b>Class: </b>" + rider_df['class'] +
                       "<br><b>Season : </b>" + "%{x}" +
                       "<br><b>Rank : </b>" + "%{y}")
    i+=1
    data.append(trace)

plotly.offline.plot({
    "data": data,
    "layout": go.Layout(title="Riders experiencing a drop in rank after going superior class",
                        xaxis_title='Season',
                        yaxis_title='Rank',
                        yaxis_autorange = 'reversed',
                        template="plotly_dark",
                        hovermode="x unified",
                        legend_title='Riders')})


###############################################################################
###############################################################################
# What is the distribution of podium finishes for each rider in MotoGP?
plt.style.use('seaborn-v0_8-talk')

ax1 = sns.barplot(data=df,y='rider_name',x='podium',estimator='sum',ci=None)
ax1.bar_label(ax1.containers[0], fontsize=8)

ax2 = sns.barplot(data=df,y='rider_name',x='podium',estimator='mean',ci=None)
ax2.bar_label(ax2.containers[1], fontsize=8,color='white')
plt.title("Marquez with most number and mean number of podiums",fontweight='bold')
plt.xlabel('Number of podiums')
plt.ylabel('Rider')
plt.legend(["Count of podiums", "Mean of podiums"], loc="upper right")
plt.show()

##############################################################################
##############################################################################
# What is the average points scored by each rider per season in MotoGP?
plt.style.use('seaborn-v0_8-talk')


riders_mean_points = df.groupby('rider_name')['points'].mean().reset_index().sort_values('points',ascending=False)

ax = sns.barplot(x='points',y='rider_name', data=riders_mean_points)
ax.bar_label(ax.containers[0], fontsize=15)
plt.title("Marquez and Acosta with highest average points per Season",fontweight='bold')
plt.xlabel('Average points per Season')
plt.ylabel('Rider')
plt.legend(["Count", "Mean"], loc="upper right")
plt.show()


##############################################################################
##############################################################################
# How consistent is each rider's performance over the years in terms of finishing position (placed)?

motogp_df = motogp_df[motogp_df['placed'] !=0]

plt.style.use('seaborn-v0_8-talk')

sns.boxplot(data=motogp_df, x='placed',y='rider_name',hue='home_country')
plt.xticks(range(1,50,5))
plt.title("Marquez median rank at champion of MotoGP",fontweight='bold')
plt.xlabel('Final season ranks')
plt.ylabel('Rider')
plt.legend(["Count", "Mean"], loc="upper right")
plt.show()