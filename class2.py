import plotly.figure_factory as ff
import pandas as pd
import csv

df = pd.read_csv("data1.csv")
graph = ff.create_distplot([df["Avg Rating"].tolist()],["Avg Rating"],show_hist = False)

graph.show()