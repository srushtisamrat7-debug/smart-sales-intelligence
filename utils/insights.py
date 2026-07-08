import pandas as pd

def generate_insights(df):

    insights = []

    total_sales = df["Sales"].sum()
    total_profit = df["Profit"].sum()

    profit_margin = (total_profit / total_sales) * 100

    # Top Category
    top_category = (
        df.groupby("Category")["Sales"]
        .sum()
        .idxmax()
    )

    # Top Region
    top_region = (
        df.groupby("Region")["Sales"]
        .sum()
        .idxmax()
    )

    # Top Product
    top_product = (
        df.groupby("Product Name")["Sales"]
        .sum()
        .idxmax()
    )

    # Top Customer
    top_customer = (
        df.groupby("Customer Name")["Sales"]
        .sum()
        .idxmax()
    )

    # Highest Discount Category
    high_discount = (
        df.groupby("Category")["Discount"]
        .mean()
        .idxmax()
    )

    insights.append(f"💰 Total Revenue: ${total_sales:,.0f}")

    insights.append(f"📈 Profit Margin: {profit_margin:.2f}%")

    insights.append(f"🏆 Highest Revenue Category: {top_category}")

    insights.append(f"🌎 Best Performing Region: {top_region}")

    insights.append(f"📦 Best Selling Product: {top_product}")

    insights.append(f"👑 Highest Value Customer: {top_customer}")

    insights.append(f"🏷 Highest Average Discount: {high_discount}")

    return insights