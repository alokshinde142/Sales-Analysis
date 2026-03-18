import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("sales_data.csv")
df["Date"] = pd.to_datetime(df["Date"])

total_revenue = df["Revenue"].sum()
avg_order_value = df["Revenue"].mean()

top_products = df.groupby("Product")["Revenue"].sum()
plt.figure()
top_products.plot(kind="bar")
plt.savefig("top_products.png")

region_sales = df.groupby("Region")["Revenue"].sum()
plt.figure()
region_sales.plot(kind="bar")
plt.savefig("region_sales.png")

monthly = df.resample("M", on="Date")["Revenue"].sum()
plt.figure()
monthly.plot()
plt.savefig("monthly_trend.png")

with open("summary.txt","w") as f:
    f.write(f"Total Revenue: {total_revenue}\nAverage Order Value: {avg_order_value}")
