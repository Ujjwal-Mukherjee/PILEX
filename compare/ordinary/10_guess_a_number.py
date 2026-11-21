import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, r2_score
marks = pd.read_csv("marks_clean.csv")
inputs = ["study_hours", "sleep_hours"]
X_train, X_test, y_train, y_test = train_test_split(marks[inputs], marks["score"], test_size=0.2, random_state=42)
model = LinearRegression().fit(X_train, y_train)
pred = model.predict(X_test)
print(mean_absolute_error(y_test, pred), r2_score(y_test, pred))
print(model.predict(pd.DataFrame([[6, 7]], columns=inputs)))
