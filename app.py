import seaborn as sns
import requests
import seaborn as sns
import pandas as pd
from io import StringIO
import matplotlib.pyplot as plt
import streamlit as st

sns.set_theme(style="whitegrid")

# Load the example planets dataset
url = 'https://raw.githubusercontent.com/mwaskom/seaborn-data/master/planets.csv'
response = requests.get(url)
planets = pd.read_csv(StringIO(response.text))

sns.set_theme(style="whitegrid")

cmap = sns.cubehelix_palette(rot=-.2, as_cmap=True)
g = sns.relplot(
    data=planets,
    x="distance", y="orbital_period",
    hue="year", size="mass",
    palette=cmap, sizes=(10, 200),
)
g.set(xscale="log", yscale="log")
g.ax.xaxis.grid(True, "minor", linewidth=.25)
g.ax.yaxis.grid(True, "minor", linewidth=.25)
g.despine(left=True, bottom=True)
st.pyplot(g.fig)