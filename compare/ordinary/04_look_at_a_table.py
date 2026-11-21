import pandas as pd
marks = pd.read_csv("marks.csv")
print(marks.head(5))
print(marks.describe(include="all"))
