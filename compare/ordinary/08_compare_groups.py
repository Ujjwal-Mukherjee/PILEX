import pandas as pd
import matplotlib.pyplot as plt
marks = pd.read_csv("marks_clean.csv")
print(marks.groupby("class")["score"].mean())
marks.boxplot(column="score", by="class")
plt.title("Marks by class")
plt.show()
