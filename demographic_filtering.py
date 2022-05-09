import pandas as pd
import numpy as np 
import csv

df = pd.read_csv("articles.csv")

#print(df.head()) 

df = df.sort_values('total_events' , ascending = True)
data_top = df.head(20)

#print("\nAfter sorting:")
#print(df)

