def answer_question(df, question):
    q = question.lower().strip()

    def money(x):
        if x >= 10000000:
            return f"₹{x / 10000000:.2f} Cr"
        elif x >= 100000:
            return f"₹{x / 100000:.2f} L"
        else:
            return f"₹{x:,.0f}"

    def top_list(series, n=5):
        text = ""
        for name, value in series.head(n).items():
            text += f"- {name}: {money(value)}\n"
        return text

    # ---------- TOTAL KPIs ----------
    if "total revenue" in q or "total sales" in q or "overall sales" in q:
        return f"💰 Total revenue is {money(df['Sales'].sum())}."

    elif "total profit" in q or "overall profit" in q:
        return f"📈 Total profit is {money(df['Profit'].sum())}."

    elif "total orders" in q or "number of orders" in q:
        return f"📦 Total orders are {df['Order ID'].nunique():,}."

    elif "total customers" in q or "number of customers" in q:
        return f"👥 Total customers are {df['Customer ID'].nunique():,}."

    elif "average order value" in q or "avg order" in q or "aov" in q:
        sales = df["Sales"].sum()
        orders = df["Order ID"].nunique()
        aov = sales / orders if orders else 0
        return f"🛒 Average order value is {money(aov)}."

    elif "profit margin" in q or "margin" in q:
        sales = df["Sales"].sum()
        profit = df["Profit"].sum()
        margin = (profit / sales) * 100 if sales else 0
        return f"💹 Profit margin is {margin:.2f}%."

    # ---------- REGION ----------
    elif "highest sales region" in q or "best region" in q or ("region" in q and "highest sales" in q):
        s = df.groupby("Region")["Sales"].sum()
        return f"🌍 Highest sales region is {s.idxmax()} with {money(s.max())}."

    elif "lowest sales region" in q or "worst region" in q or ("region" in q and "lowest sales" in q):
        s = df.groupby("Region")["Sales"].sum()
        return f"⚠️ Lowest sales region is {s.idxmin()} with {money(s.min())}."

    elif "most profitable region" in q or ("region" in q and "highest profit" in q):
        s = df.groupby("Region")["Profit"].sum()
        return f"💰 Most profitable region is {s.idxmax()} with {money(s.max())}."

    elif "least profitable region" in q or ("region" in q and "lowest profit" in q):
        s = df.groupby("Region")["Profit"].sum()
        return f"⚠️ Least profitable region is {s.idxmin()} with {money(s.min())}."

    elif "sales by region" in q or "region wise sales" in q:
        s = df.groupby("Region")["Sales"].sum().sort_values(ascending=False)
        return "🌍 Sales by region:\n\n" + top_list(s, len(s))

    elif "profit by region" in q or "region wise profit" in q:
        s = df.groupby("Region")["Profit"].sum().sort_values(ascending=False)
        return "💰 Profit by region:\n\n" + top_list(s, len(s))

    # ---------- CATEGORY ----------
    elif "highest sales category" in q or "best category" in q or ("category" in q and "highest sales" in q):
        s = df.groupby("Category")["Sales"].sum()
        return f"📦 Highest sales category is {s.idxmax()} with {money(s.max())}."

    elif "lowest sales category" in q or "worst category" in q or ("category" in q and "lowest sales" in q):
        s = df.groupby("Category")["Sales"].sum()
        return f"⚠️ Lowest sales category is {s.idxmin()} with {money(s.min())}."

    elif "most profitable category" in q or ("category" in q and "highest profit" in q):
        s = df.groupby("Category")["Profit"].sum()
        return f"💰 Most profitable category is {s.idxmax()} with {money(s.max())}."

    elif "least profitable category" in q or ("category" in q and "lowest profit" in q):
        s = df.groupby("Category")["Profit"].sum()
        return f"⚠️ Least profitable category is {s.idxmin()} with {money(s.min())}."

    elif "sales by category" in q or "category wise sales" in q:
        s = df.groupby("Category")["Sales"].sum().sort_values(ascending=False)
        return "📦 Sales by category:\n\n" + top_list(s, len(s))

    elif "profit by category" in q or "category wise profit" in q:
        s = df.groupby("Category")["Profit"].sum().sort_values(ascending=False)
        return "💰 Profit by category:\n\n" + top_list(s, len(s))

    # ---------- SUB-CATEGORY ----------
    elif "top sub category" in q or "best sub category" in q:
        s = df.groupby("Sub-Category")["Sales"].sum().sort_values(ascending=False)
        return "🏆 Top sub-categories by sales:\n\n" + top_list(s)

    elif "worst sub category" in q or "lowest sub category" in q:
        s = df.groupby("Sub-Category")["Sales"].sum().sort_values()
        return "⚠️ Lowest sub-categories by sales:\n\n" + top_list(s)

    elif "most profitable sub category" in q:
        s = df.groupby("Sub-Category")["Profit"].sum().sort_values(ascending=False)
        return "💰 Most profitable sub-categories:\n\n" + top_list(s)

    elif "least profitable sub category" in q:
        s = df.groupby("Sub-Category")["Profit"].sum().sort_values()
        return "⚠️ Least profitable sub-categories:\n\n" + top_list(s)

    # ---------- PRODUCTS ----------
    elif "top 5 product" in q or "top products" in q or "best selling product" in q:
        s = df.groupby("Product Name")["Sales"].sum().sort_values(ascending=False)
        return "🏆 Top 5 products by sales:\n\n" + top_list(s)

    elif "bottom 5 product" in q or "least selling product" in q or "worst product" in q:
        s = df.groupby("Product Name")["Sales"].sum().sort_values()
        return "⚠️ Bottom 5 products by sales:\n\n" + top_list(s)

    elif "most profitable product" in q:
        s = df.groupby("Product Name")["Profit"].sum().sort_values(ascending=False)
        return "💰 Top profitable products:\n\n" + top_list(s)

    elif "least profitable product" in q or "loss making product" in q:
        s = df.groupby("Product Name")["Profit"].sum().sort_values()
        return "⚠️ Least profitable products:\n\n" + top_list(s)

    elif "highest quantity product" in q or "most sold product by quantity" in q:
        s = df.groupby("Product Name")["Quantity"].sum().sort_values(ascending=False)
        text = "📦 Products with highest quantity sold:\n\n"
        for name, value in s.head(5).items():
            text += f"- {name}: {value:,.0f} units\n"
        return text

    # ---------- CUSTOMERS ----------
    elif "top 5 customer" in q or "top customers" in q or "best customers" in q:
        s = df.groupby("Customer Name")["Sales"].sum().sort_values(ascending=False)
        return "👑 Top 5 customers by revenue:\n\n" + top_list(s)

    elif "top customer" in q or "biggest customer" in q or "who buys the most" in q:
        s = df.groupby("Customer Name")["Sales"].sum()
        return f"👤 Top customer is {s.idxmax()} with {money(s.max())} in revenue."

    elif "lowest customer" in q or "least spending customer" in q:
        s = df.groupby("Customer Name")["Sales"].sum().sort_values()
        return "⚠️ Lowest spending customers:\n\n" + top_list(s)

    elif "repeat customers" in q:
        customer_orders = df.groupby("Customer ID")["Order ID"].nunique()
        repeat_count = (customer_orders > 1).sum()
        return f"🔁 There are {repeat_count:,} repeat customers."

    elif "new customers" in q:
        customer_orders = df.groupby("Customer ID")["Order ID"].nunique()
        new_count = (customer_orders == 1).sum()
        return f"🆕 There are {new_count:,} new customers."

    elif "customer lifetime value" in q or "clv" in q:
        clv = df.groupby("Customer ID")["Sales"].sum().mean()
        return f"💎 Average customer lifetime value is {money(clv)}."

    # ---------- SEGMENT ----------
    elif "best segment" in q or "highest sales segment" in q:
        s = df.groupby("Segment")["Sales"].sum()
        return f"👥 Best customer segment is {s.idxmax()} with {money(s.max())} in sales."

    elif "lowest performing segment" in q or "worst segment" in q:
        s = df.groupby("Segment")["Sales"].sum()
        return f"⚠️ Lowest performing segment is {s.idxmin()} with {money(s.min())} in sales."

    elif "most profitable segment" in q:
        s = df.groupby("Segment")["Profit"].sum()
        return f"💰 Most profitable segment is {s.idxmax()} with {money(s.max())}."

    elif "segment wise sales" in q or "sales by segment" in q:
        s = df.groupby("Segment")["Sales"].sum().sort_values(ascending=False)
        return "👥 Sales by segment:\n\n" + top_list(s, len(s))

    # ---------- STATE / CITY ----------
    elif "top states" in q or "best states" in q or "highest sales state" in q:
        s = df.groupby("State")["Sales"].sum().sort_values(ascending=False)
        return "🌎 Top states by sales:\n\n" + top_list(s)

    elif "lowest sales state" in q or "worst state" in q:
        s = df.groupby("State")["Sales"].sum().sort_values()
        return "⚠️ Lowest sales states:\n\n" + top_list(s)

    elif "most profitable state" in q:
        s = df.groupby("State")["Profit"].sum().sort_values(ascending=False)
        return "💰 Most profitable states:\n\n" + top_list(s)

    elif "least profitable state" in q:
        s = df.groupby("State")["Profit"].sum().sort_values()
        return "⚠️ Least profitable states:\n\n" + top_list(s)

    elif "top cities" in q or "best cities" in q or "highest sales city" in q:
        s = df.groupby("City")["Sales"].sum().sort_values(ascending=False)
        return "🏙️ Top cities by sales:\n\n" + top_list(s)

    elif "lowest sales city" in q or "worst city" in q:
        s = df.groupby("City")["Sales"].sum().sort_values()
        return "⚠️ Lowest sales cities:\n\n" + top_list(s)

    # ---------- TIME ANALYSIS ----------
    elif "monthly sales trend" in q or "sales trend" in q:
        monthly_sales = df.groupby(df["Order Date"].dt.to_period("M"))["Sales"].sum()
        best_month = monthly_sales.idxmax()
        best_sales = monthly_sales.max()
        return f"📈 Monthly sales trend is available in the dashboard. Best month was {best_month} with {money(best_sales)}."

    elif "best month" in q or "highest sales month" in q:
        s = df.groupby(df["Order Date"].dt.to_period("M"))["Sales"].sum()
        return f"📅 Best sales month was {s.idxmax()} with {money(s.max())}."

    elif "worst month" in q or "lowest sales month" in q:
        s = df.groupby(df["Order Date"].dt.to_period("M"))["Sales"].sum()
        return f"📅 Lowest sales month was {s.idxmin()} with {money(s.min())}."

    elif "quarterly sales" in q or "sales by quarter" in q:
        s = df.groupby(df["Order Date"].dt.to_period("Q"))["Sales"].sum().sort_index()
        text = "📊 Quarterly sales:\n\n"
        for period, value in s.items():
            text += f"- {period}: {money(value)}\n"
        return text

    elif "yearly sales" in q or "sales by year" in q:
        s = df.groupby(df["Order Date"].dt.year)["Sales"].sum().sort_index()
        text = "📆 Yearly sales:\n\n"
        for year, value in s.items():
            text += f"- {year}: {money(value)}\n"
        return text

    # ---------- DISCOUNT ----------
    elif "average discount" in q or "avg discount" in q:
        return f"🏷️ Average discount is {df['Discount'].mean() * 100:.2f}%."

    elif "highest discount" in q:
        max_discount = df["Discount"].max() * 100
        return f"🏷️ Highest discount given is {max_discount:.2f}%."

    elif "discount impact" in q or "discount vs profit" in q:
        corr = df["Discount"].corr(df["Profit"])
        return f"📉 Discount and profit correlation is {corr:.2f}. Negative value means higher discounts may reduce profit."

    # ---------- QUANTITY ----------
    elif "total quantity" in q or "units sold" in q:
        return f"📦 Total quantity sold is {df['Quantity'].sum():,} units."

    elif "average quantity" in q:
        return f"📦 Average quantity per order line is {df['Quantity'].mean():.2f}."

    # ---------- SHIPPING ----------
    elif "ship mode" in q or "shipping mode" in q:
        s = df.groupby("Ship Mode")["Sales"].sum().sort_values(ascending=False)
        return "🚚 Sales by ship mode:\n\n" + top_list(s, len(s))

    elif "most used shipping" in q or "popular shipping" in q:
        s = df["Ship Mode"].value_counts()
        return f"🚚 Most used shipping mode is {s.idxmax()} with {s.max():,} orders."

    # ---------- LOSS / RISK ----------
    elif "loss" in q or "negative profit" in q:
        loss_df = df[df["Profit"] < 0]
        return f"⚠️ There are {len(loss_df):,} loss-making rows with total loss of {money(abs(loss_df['Profit'].sum()))}."

    elif "profitable orders" in q:
        profit_df = df[df["Profit"] > 0]
        return f"✅ There are {len(profit_df):,} profitable rows."

    elif "recommendation" in q or "suggest" in q:
        profit_by_cat = df.groupby("Category")["Profit"].sum()
        sales_by_region = df.groupby("Region")["Sales"].sum()
        return (
            f"💡 Recommendation:\n\n"
            f"- Focus more on {profit_by_cat.idxmax()} because it gives the highest profit.\n"
            f"- Improve performance in {sales_by_region.idxmin()} because it has the lowest sales.\n"
            f"- Review high-discount products because discounts may reduce profitability."
        )

    # ---------- DATASET ----------
    elif "rows" in q or "how many records" in q:
        return f"📄 Dataset contains {df.shape[0]:,} rows."

    elif "columns" in q:
        return f"📋 Dataset contains {df.shape[1]:,} columns."

    elif "missing values" in q:
        missing = df.isnull().sum().sum()
        return f"🧹 Dataset contains {missing:,} missing values."

    elif "dataset summary" in q or "summary" in q:
        return (
            f"📊 Dataset Summary:\n\n"
            f"- Rows: {df.shape[0]:,}\n"
            f"- Columns: {df.shape[1]:,}\n"
            f"- Revenue: {money(df['Sales'].sum())}\n"
            f"- Profit: {money(df['Profit'].sum())}\n"
            f"- Orders: {df['Order ID'].nunique():,}\n"
            f"- Customers: {df['Customer ID'].nunique():,}"
        )

    else:
        return (
            "❓ I can answer questions about revenue, profit, orders, customers, products, "
            "regions, states, cities, categories, segments, discounts, shipping, quantity, trends, and dataset summary."
        )