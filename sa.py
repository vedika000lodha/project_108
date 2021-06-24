import pandas as pd 
import plotly.figure_factory as ff 
import csv

df = pd.read_csv("dataproject.csv")
fig = ff.create_distplot([df["Avg"].tolist()],["Avg"], show_hist = False)
fig.show()