import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
marks = pd.read_csv("marks_clean.csv")
inputs = ["study_hours", "sleep_hours", "attendance"]
X_train, X_test, y_train, y_test = train_test_split(marks[inputs], marks["result"], test_size=0.2, random_state=42)
model = DecisionTreeClassifier(random_state=0).fit(X_train, y_train)
pred = model.predict(X_test)
print(accuracy_score(y_test, pred))
print(classification_report(y_test, pred))
print(confusion_matrix(y_test, pred))
