import pandas as pd
import matplotlib.pyplot as plt
sales = pd.read_csv("sales.csv")
sales["date"] = pd.to_datetime(sales["date"], format="%d/%m/%Y")
months = sales.groupby(sales["date"].dt.to_period("M"))["amount"].sum().reset_index()
months.columns = ["month", "total"]
plt.plot(months["month"].astype(str), months["total"])
plt.title("Sales by month")
plt.show()
