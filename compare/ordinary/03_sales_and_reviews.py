import pandas as pd
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline
sales = pd.read_csv("sales.csv")
sales["date"] = pd.to_datetime(sales["date"], format="%d/%m/%Y")
months = sales.groupby(sales["date"].dt.to_period("M"))["amount"].sum().reset_index()
months.columns = ["month", "total"]
plt.plot(months["month"].astype(str), months["total"])
plt.title("Sales by month")
plt.show()
months.to_csv("months.csv", index=False)
reviews = pd.read_csv("reviews.csv")
counter = CountVectorizer(stop_words="english")
counts = counter.fit_transform(reviews["text"]).sum(axis=0).A1
print(sorted(zip(counter.get_feature_names_out(), counts), key=lambda t: -t[1])[:5])
X_train, X_test, y_train, y_test = train_test_split(reviews["text"], reviews["label"], test_size=0.2, random_state=42)
model = make_pipeline(CountVectorizer(), MultinomialNB()).fit(X_train, y_train)
print(classification_report(y_test, model.predict(X_test)))
print(model.predict(["Cold food and rude staff"]))
