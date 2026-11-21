import pandas as pd
marks = pd.read_csv("marks.csv")
marks["study_hours"] = marks["study_hours"].fillna(marks["study_hours"].mean())
q1, q3 = marks["score"].quantile([0.25, 0.75])
iqr = q3 - q1
marks = marks[marks["score"].between(q1 - 1.5 * iqr, q3 + 1.5 * iqr)]
marks = marks.loc[:, marks.isna().mean() <= 0.5]
marks = marks.loc[:, marks.nunique(dropna=False) > 1]
marks = marks.drop_duplicates()
marks.to_csv("marks_clean.csv", index=False)
