import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import requests

url = 'https://raw.githubusercontent.com/mwaskom/seaborn-data/master/datasets.txt'
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    print("Request successful!")
    print(response.text)  # Print the content of the response (list of dataset names)
else:
    print(f"Request failed with status code {response.status_code}")


st.title("DS basics")

st.title("Seaborn Visualization")

sns.set_theme(style="whitegrid")

#load data
planets = sns.load_dataset("planets")

planets.columns

cmap = sns. cubehelix_palette(rot=.2, as_cmap=True)
plot = sns.relplot(
    data=planets, x='distance', y='orbital_period', hue='year', size='mass', palette=cmap, sizes=(10,200)
)
plot.set(xscale='log', yscale='log')
g.ax.xaxis.grid(True, "minor", linewidth=.25)
g.ax.yaxis.grid(True, "minor", linewidth=.25)
g.despine(left=True, bottom=True)