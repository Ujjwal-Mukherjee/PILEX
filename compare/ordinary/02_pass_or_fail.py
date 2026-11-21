import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
marks = pd.read_csv("marks.csv")
marks["study_hours"] = marks["study_hours"].fillna(marks["study_hours"].mean())
q1, q3 = marks["score"].quantile([0.25, 0.75])
iqr = q3 - q1
marks = marks[marks["score"].between(q1 - 1.5 * iqr, q3 + 1.5 * iqr)]
marks = marks.loc[:, marks.isna().mean() <= 0.5]
marks = marks.loc[:, marks.nunique(dropna=False) > 1]
marks = marks.drop_duplicates()
inputs = ["study_hours", "sleep_hours", "attendance"]
forest = RandomForestRegressor(random_state=42).fit(marks[inputs], marks["score"])
print(pd.Series(forest.feature_importances_, index=inputs).sort_values(ascending=False))
X_train, X_test, y_train, y_test = train_test_split(marks[inputs], marks["result"], test_size=0.2, random_state=42)
model = RandomForestClassifier(random_state=42).fit(X_train, y_train)
pred = model.predict(X_test)
print(classification_report(y_test, pred))
print(confusion_matrix(y_test, pred))
print(model.predict(pd.DataFrame([[7, 6, 90]], columns=inputs)))
marks.boxplot(column="score", by="class")
plt.title("Marks by class")
plt.show()
columns = ["study_hours", "sleep_hours", "score"]
marks["group"] = KMeans(n_clusters=3, random_state=42, n_init=10).fit_predict(StandardScaler().fit_transform(marks[columns]))
print(marks.groupby("group")[columns].mean())
plt.scatter(marks["study_hours"], marks["score"], c=marks["group"])
plt.xlabel("study_hours")
plt.ylabel("score")
plt.show()
