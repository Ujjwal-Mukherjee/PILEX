import pandas as pd
from sklearn.ensemble import RandomForestRegressor
marks = pd.read_csv("marks_clean.csv")
inputs = ["study_hours", "sleep_hours", "attendance"]
forest = RandomForestRegressor(random_state=42).fit(marks[inputs], marks["score"])
print(pd.Series(forest.feature_importances_, index=inputs).sort_values(ascending=False))
