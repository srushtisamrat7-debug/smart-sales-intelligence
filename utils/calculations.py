def calculate_kpis(df):
    total_sales = df["Sales"].sum()
    total_profit = df["Profit"].sum()
    total_orders = df["Order ID"].nunique()
    total_customers = df["Customer ID"].nunique()

    avg_order_value = total_sales / total_orders if total_orders != 0 else 0
    profit_margin = (total_profit / total_sales) * 100 if total_sales != 0 else 0

    df = df.copy()
    df["Month"] = df["Order Date"].dt.to_period("M")

    monthly_sales = df.groupby("Month")["Sales"].sum().sort_index()

    if len(monthly_sales) >= 2:
        current_month_sales = monthly_sales.iloc[-1]
        previous_month_sales = monthly_sales.iloc[-2]
        monthly_growth = ((current_month_sales - previous_month_sales) / previous_month_sales) * 100
    else:
        monthly_growth = 0

    return total_sales, total_profit, total_orders, total_customers, avg_order_value, profit_margin, monthly_growth