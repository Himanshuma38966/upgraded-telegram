import pandas as pd 
import plotly.express as px
import plotly.figure_factory as ff

df=pd.read_csv("data108.csv")
fig=ff.create_distplot([df["Sr.No"].tolist()],["Avg Rating"],show_hist = False)
fig.show()