import pandas as pd
import plotly.figure_factory as ff
import csv

df=pd.read_csv("brands.csv")
print(df)
df_list=df["Avg Rating"].tolist()
print(df_list)
fig=ff.create_distplot([df_list],["Avg Rating"],show_hist=False)
fig.show()