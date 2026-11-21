import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score
from sklearn.model_selection import train_test_split
marks = pd.read_csv("marks.csv")
print(marks.head(3))
print(marks.describe(include="all"))
marks["study_hours"] = marks["study_hours"].fillna(marks["study_hours"].median())
q1, q3 = marks["score"].quantile([0.25, 0.75])
iqr = q3 - q1
marks = marks[marks["score"].between(q1 - 1.5 * iqr, q3 + 1.5 * iqr)]
marks = marks.loc[:, marks.isna().mean() <= 0.5]
marks = marks.loc[:, marks.nunique(dropna=False) > 1]
marks = marks.drop_duplicates()
plt.hist(marks["score"], bins=8)
plt.title("Class marks")
plt.show()
marks["result"].value_counts().plot.pie(autopct="%1.0f%%")
plt.title("Pass and fail")
plt.ylabel("")
plt.show()
corr = marks.select_dtypes("number").corr()
plt.imshow(corr, cmap="coolwarm", vmin=-1, vmax=1)
plt.xticks(range(len(corr)), corr.columns, rotation=90)
plt.yticks(range(len(corr)), corr.columns)
plt.colorbar()
plt.title("Links between columns")
plt.show()
plt.scatter(marks["study_hours"], marks["score"])
slope, intercept = np.polyfit(marks["study_hours"], marks["score"], 1)
plt.plot(marks["study_hours"], slope * marks["study_hours"] + intercept)
plt.title("Study and marks")
plt.show()
print(marks["study_hours"].corr(marks["score"]))
inputs = ["study_hours", "sleep_hours"]
X_train, X_test, y_train, y_test = train_test_split(marks[inputs], marks["score"], test_size=0.2, random_state=42)
model = LinearRegression().fit(X_train, y_train)
pred = model.predict(X_test)
print(mean_absolute_error(y_test, pred), r2_score(y_test, pred))
print(model.predict(pd.DataFrame([[6, 7]], columns=inputs)))
