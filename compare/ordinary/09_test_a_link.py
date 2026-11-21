import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
marks = pd.read_csv("marks_clean.csv")
plt.scatter(marks["study_hours"], marks["score"])
slope, intercept = np.polyfit(marks["study_hours"], marks["score"], 1)
plt.plot(marks["study_hours"], slope * marks["study_hours"] + intercept)
plt.title("Study and marks")
plt.show()
print(marks["study_hours"].corr(marks["score"]))
