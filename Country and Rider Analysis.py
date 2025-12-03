#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  3 07:43:16 2025

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
###############################################################################
# Country and Rider Analysis:
    
# ###############################################################################    
# Which country produces the most successful MotoGP riders (based on wins or championships)?
sns.set_palette('muted')
plt.style.use('seaborn-v0_8-talk')


ax1 = sns.barplot(data=df,y='home_country',x='wins',estimator='sum',ci=None)
ax1.bar_label(ax1.containers[0], fontsize=12)

ax2 = sns.barplot(data=df,y='home_country',x='wins',estimator='mean',ci=None)
ax2.bar_label(ax2.containers[1], fontsize=12,color='white')
plt.title("Spain with the most riders in all classes",fontweight='bold')
plt.xlabel('Wins')
plt.ylabel('Home Countries')
plt.legend(["Count", "Mean"], loc="lower right")
plt.show()

ax1 = sns.barplot(data=df,y='home_country',x='world_championships',estimator='sum',ci=None)
ax1.bar_label(ax1.containers[0], fontsize=12)

ax2 = sns.barplot(data=df,y='home_country',x='world_championships',estimator='mean',ci=None)
ax2.bar_label(ax2.containers[1], fontsize=12,color='white')
plt.title("Spain with the most champions in all classes",fontweight='bold')
plt.xlabel('Number of champions')
plt.ylabel('Home Countries')
plt.legend(["Count", "Mean"], loc="lower right")
plt.show()

ax1 = sns.barplot(data=motogp_df,y='home_country',x='wins',estimator='sum',ci=None)
ax1.bar_label(ax1.containers[0], fontsize=12)

ax2 = sns.barplot(data=motogp_df,y='home_country',x='wins',estimator='mean',ci=None)
ax2.bar_label(ax2.containers[1], fontsize=12,color='white')
plt.title("Spain with the most riders in MotoGP",fontweight='bold')
plt.xlabel('Wins')
plt.ylabel('Home Countries')
plt.legend(["Count", "Mean"], loc="lower right")
plt.show()

ax1 = sns.barplot(data=motogp_df,y='home_country',x='world_championships',estimator='sum',ci=None)
ax1.bar_label(ax1.containers[0], fontsize=12)

ax2 = sns.barplot(data=motogp_df,y='home_country',x='world_championships',estimator='mean',ci=None)
ax2.bar_label(ax2.containers[1], fontsize=12,color='white')
plt.title("Spain with the most Champions in MotoGP",fontweight='bold')
plt.xlabel('Number of champions')
plt.ylabel('Home Countries')
plt.legend(["Count", "Mean"], loc="lower right")
plt.show()

country_group = df.groupby('home_country')['rider_name'].count()

data = go.Scattermap(
        lat=['40.416775','48.864716','41.893333',
             '-25.745928','13.752494',' -35.297591',
             '35.67686','38.707751'],
        lon=['-3.703790','2.349014','12.482778',
             '28.18791','100.493509','149.101268',
             '139.763895','-9.136592'],
        mode='markers',
        marker=go.scattermap.Marker(
            size=15
        ),
        text=[f"Spain rider presence: {country_group['Spain']}",
              f"France rider presence: {country_group['France']}",
              f"Italy rider presence: {country_group['Italy']}",
              f"South Africa rider presence: {country_group['South Africa']}",
              f"Thailand rider presence: {country_group['Thailand']}",
              f"Australia rider presence: {country_group['Australia']}",
              f"Japan rider presence: {country_group['Japan']}",
              f"Portugal rider presence: {country_group['Portugal']}"],
        hovertemplate=""
    )

plotly.offline.plot({
    "data": data,
    "layout": go.Layout(title="Spain breaking records of presence in all classes",
                        xaxis_title='Season',
                        autosize=True,
                        hovermode='closest',
                        showlegend=False,
                        map=dict(bearing=0,
                                 center=dict(
                                     lat=15,
                                     lon=55),
                                 pitch=0,
                                 zoom=1.5,
                                 style='dark'
                                 ))})




rider_country_list = []
for rider in df['rider_name'].unique():
    rider_country = [rider,df[df['rider_name'] == rider]['home_country'].iloc[0]]
    rider_country_list.append(rider_country)
    
rider_country_df = pd.DataFrame(rider_country_list,columns=['rider_name','home_country'])

rider_country_group = rider_country_df.groupby('home_country')['rider_name'].count()

data = go.Scattermap(
        lat=['40.416775','48.864716','41.893333',
             '-25.745928','13.752494',' -35.297591',
             '35.67686','38.707751'],
        lon=['-3.703790','2.349014','12.482778',
             '28.18791','100.493509','149.101268',
             '139.763895','-9.136592'],
        mode='markers',
        marker=go.scattermap.Marker(
            size=15
        ),
        text=[f"Spain rider count: {rider_country_group['Spain']}",
              f"France rider count: {rider_country_group['France']}",
              f"Italy rider count: {rider_country_group['Italy']}",
              f"South Africa rider count: {rider_country_group['South Africa']}",
              f"Thailand rider count: {rider_country_group['Thailand']}",
              f"Australia rider count: {rider_country_group['Australia']}",
              f"Japan rider count: {rider_country_group['Japan']}",
              f"Portugal rider count: {rider_country_group['Portugal']}"],
        hovertemplate=""
    )

plotly.offline.plot({
    "data": data,
    "layout": go.Layout(title="European Countries providing most riders",
                        xaxis_title='Season',
                        autosize=True,
                        hovermode='closest',
                        showlegend=False,
                        map=dict(bearing=0,
                                 center=dict(
                                     lat=15,
                                     lon=55),
                                 pitch=0,
                                 zoom=1.5,
                                 style='dark'
                                 ))})

###############################################################################
###############################################################################
# Is there a correlation between the rider's home country and their performance (podiums)?
sns.set_palette('muted')
plt.style.use('seaborn-v0_8-talk')

ax1 = sns.barplot(data=df,y='home_country',x='podium',estimator='sum',ci=None)
ax1.bar_label(ax1.containers[0], fontsize=12)

ax2 = sns.barplot(data=df,y='home_country',x='podium',estimator='mean',ci=None)
ax2.bar_label(ax2.containers[1], fontsize=12,color='white')
plt.title("Spain with the most podium in all classes",fontweight='bold')
plt.xlabel('podium')
plt.ylabel('Home Countries')
plt.legend(["Count", "Mean"], loc="lower right")
plt.show()

ax1 = sns.barplot(data=motogp_df,y='home_country',x='podium',estimator='sum',ci=None)
ax1.bar_label(ax1.containers[0], fontsize=12)

ax2 = sns.barplot(data=motogp_df,y='home_country',x='podium',estimator='mean',ci=None)
ax2.bar_label(ax2.containers[1], fontsize=12,color='white')
plt.title("Spain with the most podium in MotoGP",fontweight='bold')
plt.xlabel('podium')
plt.ylabel('Home Countries')
plt.legend(["Count", "Mean"], loc="lower right")
plt.show()