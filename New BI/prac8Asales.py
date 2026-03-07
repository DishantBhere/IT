#Data Visualization using Python on Sales Data

import pandas as pd
import matplotlib.pyplot as plt
import sys

# CSV file path
fname = "sales_data.csv"

try:
    df = pd.read_csv(fname)
except FileNotFoundError:
    sys.exit("Please check the CSV file path")

MONTH_ORDER = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]


def bar_total_sales_by_product(dataframe):
    sales = dataframe.groupby("Product", as_index=False)["Total_Sales"].sum()

    plt.figure(figsize=(8,5))
    plt.bar(sales["Product"], sales["Total_Sales"])
    plt.title("Total Sales by Product")
    plt.xlabel("Product")
    plt.ylabel("Total Sales")
    plt.grid(axis="y", linestyle="--", alpha=0.5)
    plt.tight_layout()
    plt.show()


def pie_sales_contribution(dataframe):
    sales = dataframe.groupby("Product", as_index=False)["Total_Sales"].sum()

    plt.figure(figsize=(6,6))
    plt.pie(
        sales["Total_Sales"],
        labels=sales["Product"],
        autopct="%1.1f%%",
        startangle=90
    )
    plt.title("Sales Contribution by Product")
    plt.axis("equal")
    plt.tight_layout()
    plt.show()


def line_monthly_sales_trend(dataframe):
    monthly = dataframe.groupby("Month", as_index=False)["Total_Sales"].sum()

    monthly["Month"] = pd.Categorical(
        monthly["Month"],
        categories=MONTH_ORDER,
        ordered=True
    )

    monthly = monthly.sort_values("Month")

    plt.figure(figsize=(10,5))
    plt.plot(monthly["Month"].astype(str), monthly["Total_Sales"], marker="o")
    plt.title("Monthly Sales Trend")
    plt.xlabel("Month")
    plt.ylabel("Total Sales")
    plt.grid(True)
    plt.tight_layout()
    plt.show()


while True:

    print("\n1 Bar Chart - Total Sales by Product")
    print("2 Pie Chart - Sales Contribution by Product")
    print("3 Line Chart - Monthly Sales Trend")
    print("0 Exit")

    choice = input("Enter your choice (0-3): ")

    if choice == "0":
        print("Bye bye")
        break

    elif choice == "1":
        bar_total_sales_by_product(df)

    elif choice == "2":
        pie_sales_contribution(df)

    elif choice == "3":
        line_monthly_sales_trend(df)

    else:
        print("Invalid choice")
