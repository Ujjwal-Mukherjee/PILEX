import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
marks = pd.read_csv("marks_clean.csv")
columns = ["study_hours", "sleep_hours", "score"]
marks["group"] = KMeans(n_clusters=3, random_state=42, n_init=10).fit_predict(StandardScaler().fit_transform(marks[columns]))
print(marks.groupby("group")[columns].mean())
plt.scatter(marks["study_hours"], marks["score"], c=marks["group"])
plt.xlabel("study_hours")
plt.ylabel("score")
plt.show()
