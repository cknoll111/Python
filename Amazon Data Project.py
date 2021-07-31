import pandas as pd
#amazon data analysis program
#takes in CSV data from amazon.com and displays useful information as well as plotting a graph

df = pd.read_csv('amazonorders.csv')
df = df.fillna(0)
df["Item Total"] = df["Item Total"].str.replace('$','').astype(float)
df["Item Subtotal Tax"] = df["Item Subtotal Tax"].str.replace('$','').astype(float)
df['Order Date'] = pd.to_datetime(df['Order Date'])


sum = df["Item Total"].sum()
mean = df["Item Total"].mean()
median = df["Item Total"].median()
max = df["Item Total"].max()
min = df["Item Total"].min()
sumTax = df["Item Subtotal Tax"].sum()


print(f"The total amount spent in 2020 was: ${sum}")
print(f"The average amount spent in 2020 was: ${mean}")
print(f"The the median amount spent in 2020 was: ${median}")
print(f"The most spent in one transaction in 2020 was: ${max}")
print(f"The least spent in one transaction in 2020 was: ${min}")

print(f"The total amount spent in sales tax in 2020 was: ${sumTax}")

daily_orders = df.groupby('Order Date').sum()["Item Total"]

%matplotlib inline
daily_orders.plot.bar(figsize=(20,10))
