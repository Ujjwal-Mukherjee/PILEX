import pandas as pd
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score
from sklearn.model_selection import train_test_split

def tidy(table):
    table = table.fillna(table.mean(numeric_only=True))
    for column in table.select_dtypes("number"):
        q1, q3 = table[column].quantile([0.25, 0.75])
        table = table[table[column].between(q1 - 1.5 * (q3 - q1), q3 + 1.5 * (q3 - q1))]
    table = table.loc[:, table.isna().mean() <= 0.5]
    table = table.loc[:, table.nunique(dropna=False) > 1]
    return table.drop_duplicates()

marks = pd.read_csv("marks.csv")
print(marks.describe(include="all"))
numbers = tidy(marks).select_dtypes("number")
for column in numbers:
    plt.hist(numbers[column])
    plt.title(column)
    plt.show()
corr = numbers.corr()
plt.imshow(corr, cmap="coolwarm", vmin=-1, vmax=1)
plt.xticks(range(len(corr)), corr.columns, rotation=90)
plt.yticks(range(len(corr)), corr.columns)
plt.colorbar()
plt.title("Links between columns")
plt.show()
data = pd.get_dummies(tidy(marks), dtype=float)
inputs = data.drop(columns="score")
X_train, X_test, y_train, y_test = train_test_split(inputs, data["score"], test_size=0.2, random_state=42)
models = [LinearRegression(), RandomForestRegressor(random_state=42)]
for model in models:
    model.fit(X_train, y_train)
best = max(models, key=lambda m: r2_score(y_test, m.predict(X_test)))
pred = best.predict(X_test)
print(mean_absolute_error(y_test, pred), r2_score(y_test, pred))
print(pd.Series(getattr(best, "feature_importances_", abs(getattr(best, "coef_", 0))), index=inputs.columns).sort_values(ascending=False))
