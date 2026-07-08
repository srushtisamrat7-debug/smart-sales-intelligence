import plotly.express as px


def monthly_sales_chart(df):
    monthly_sales = (
        df.groupby(df["Order Date"].dt.to_period("M"))["Sales"]
        .sum()
        .reset_index()
    )
    monthly_sales["Order Date"] = monthly_sales["Order Date"].astype(str)

    fig = px.line(
        monthly_sales,
        x="Order Date",
        y="Sales",
        markers=True,
        title="Monthly Sales Trend",
        color_discrete_sequence=["#2563EB"]
    )
    fig.update_layout(
     template="plotly_white",
     paper_bgcolor="white",
     plot_bgcolor="white",
     font=dict(size=14),
     title_font_size=20,
     title_x=0.02,
     margin=dict(l=20, r=20, t=60, b=20)
    )
    return fig


def category_sales_chart(df):
    category_sales = (
        df.groupby("Category")["Sales"]
        .sum()
        .reset_index()
        .sort_values(by="Sales", ascending=False)
    )

    fig = px.bar(
        category_sales,
        x="Category",
        y="Sales",
        title="Sales by Category",
        text_auto=True,
        color="Category",
        color_discrete_map={
        "Technology": "#6366F1",
        "Furniture": "#F97316",
        "Office Supplies": "#10B981"
    }
    )
    fig.update_layout(
     template="plotly_white",
     paper_bgcolor="white",
     plot_bgcolor="white",
     font=dict(size=14),
     title_font_size=20,
     title_x=0.02,
    margin=dict(l=20, r=20, t=60, b=20)
    )
    return fig


def region_sales_chart(df):
    region_sales = (
        df.groupby("Region")["Sales"]
        .sum()
        .reset_index()
        .sort_values(by="Sales", ascending=False)
    )

    fig = px.pie(
        region_sales,
        names="Region",
        values="Sales",
        title="Sales by Region",
        hole=0.4,
        color_discrete_sequence=px.colors.qualitative.Set2
    )
    
    fig.update_layout(
     template="plotly_white",
     paper_bgcolor="white",
     plot_bgcolor="white",
     font=dict(size=14),
     title_font_size=20,
     title_x=0.02,
     legend=dict(
        orientation="h",
        y=-0.2,
        x=0.1
    ),
     margin=dict(l=20, r=20, t=60, b=20)
    )
    
    return fig


def top_products_chart(df):
    top_products = (
        df.groupby("Product Name")["Sales"]
        .sum()
        .reset_index()
        .sort_values(by="Sales", ascending=False)
        .head(10)
    )   
    top_products["Product Name"] = top_products["Product Name"].apply(
        lambda x: x[:32] + "..." if len(x) > 32 else x
    )

    fig = px.bar(
        top_products,
        x="Sales",
        y="Product Name",
        orientation="h",
        title="Top 10 Products by Sales",
        text_auto=False,
        color_discrete_sequence=["#2563EB"]
    )

    fig.update_layout(yaxis={"categoryorder": "total ascending"})
    fig.update_layout(
     template="plotly_white",
     paper_bgcolor="white",
     plot_bgcolor="white",
     font=dict(size=14),
     title_font_size=20,
     title_x=0.02,
     height=650,
     margin=dict(l=220, r=30, t=60, b=30)
    )
    return fig


def top_customers_chart(df):
    top_customers = (
        df.groupby("Customer Name")["Sales"]
        .sum()
        .reset_index()
        .sort_values(by="Sales", ascending=False)
        .head(10)
    )

    fig = px.bar(
        top_customers,
        x="Sales",
        y="Customer Name",
        orientation="h",
        title="Top 10 Customers by Revenue",
        text_auto=False,
        color_discrete_sequence=["#16A34A"]
    )

    fig.update_layout(yaxis={"categoryorder": "total ascending"})
    fig.update_layout(
     template="plotly_white",
     paper_bgcolor="white",
     plot_bgcolor="white",
     font=dict(size=14),
     title_font_size=20,
     title_x=0.02,
     height=650,
     margin=dict(l=20, r=20, t=60, b=20)
    )
    return fig


def category_profit_chart(df):
    category_profit = (
        df.groupby("Category")["Profit"]
        .sum()
        .reset_index()
        .sort_values(by="Profit", ascending=False)
    )

    fig = px.bar(
        category_profit,
        x="Category",
        y="Profit",
        title="Profit by Category",
        text_auto=True,
        color="Category",
        color_discrete_map={
        "Technology": "#6366F1",
        "Furniture": "#F97316",
        "Office Supplies": "#10B981"
    }
    )
    fig.update_layout(
     template="plotly_white",
     paper_bgcolor="white",
     plot_bgcolor="white",
     font=dict(size=14),
     title_font_size=20,
     title_x=0.02,
     margin=dict(l=20, r=20, t=60, b=20)
    )
    return fig


def discount_profit_chart(df):
    fig = px.scatter(
        df,
        x="Discount",
        y="Profit",
        size="Sales",
        color="Category",
        title="Discount vs Profit",
        hover_data=["Product Name", "Region"],
        color_discrete_map={
        "Technology": "#6366F1",
        "Furniture": "#F97316",
        "Office Supplies": "#10B981"
    }
    )
    return fig
def repeat_customer_chart(df):
    customer_orders = (
        df.groupby("Customer ID")["Order ID"]
        .nunique()
        .reset_index()
    )

    customer_orders["Customer Type"] = customer_orders["Order ID"].apply(
        lambda x: "Repeat Customer" if x > 1 else "New Customer"
    )

    customer_type_count = (
        customer_orders["Customer Type"]
        .value_counts()
        .reset_index()
    )

    customer_type_count.columns = ["Customer Type", "Count"]

    fig = px.pie(
        customer_type_count,
        names="Customer Type",
        values="Count",
        title="Repeat vs New Customers",
        hole=0.4,
         color="Customer Type",
         color_discrete_map={
        "Repeat Customer": "#2563EB",   # Blue
        "New Customer": "#10B981"       # Green
    }
    )
    fig.update_layout(
     template="plotly_white",
     paper_bgcolor="white",
     plot_bgcolor="white",
     font=dict(size=14),
     title_font_size=20,
     title_x=0.02,
     margin=dict(l=20, r=20, t=60, b=20)
    )

    return fig


def customer_segment_chart(df):
    segment_sales = (
        df.groupby("Segment")["Sales"]
        .sum()
        .reset_index()
        .sort_values(by="Sales", ascending=False)
    )

    fig = px.bar(
        segment_sales,
        x="Segment",
        y="Sales",
        title="Sales by Customer Segment",
        text_auto=True,
         color="Segment",
         color_discrete_map={
        "Consumer": "#2563EB",      # Blue
        "Corporate": "#F59E0B",     # Orange
        "Home Office": "#10B981"    # Green
    }
    )
    fig.update_layout(
     template="plotly_white",
     paper_bgcolor="white",
     plot_bgcolor="white",
     font=dict(size=14),
     title_font_size=20,
     title_x=0.02,
     margin=dict(l=20, r=20, t=60, b=20)
)

    return fig
def state_sales_chart(df):
    state_sales = (
        df.groupby("State")["Sales"]
        .sum()
        .reset_index()
        .sort_values(by="Sales", ascending=False)
        .head(10)
    )

    fig = px.bar(
        state_sales,
        x="Sales",
        y="State",
        orientation="h",
        title="Top 10 States by Sales",
        text_auto=True,
        color_discrete_sequence=["#2563EB"]
    )

    fig.update_layout(yaxis={"categoryorder": "total ascending"})
    fig.update_layout(
     template="plotly_white",
     paper_bgcolor="white",
     plot_bgcolor="white",
     font=dict(size=14),
     title_font_size=20,
     title_x=0.02,
     margin=dict(l=20, r=20, t=60, b=20)
    )
    return fig


def city_sales_chart(df):
    city_sales = (
        df.groupby("City")["Sales"]
        .sum()
        .reset_index()
        .sort_values(by="Sales", ascending=False)
        .head(10)
    )

    fig = px.bar(
        city_sales,
        x="Sales",
        y="City",
        orientation="h",
        title="Top 10 Cities by Sales",
        text_auto=True,
        color_discrete_sequence=["#7C3AED"]
    )

    fig.update_layout(yaxis={"categoryorder": "total ascending"})
    fig.update_layout(
     template="plotly_white",
     paper_bgcolor="white",
     plot_bgcolor="white",
     font=dict(size=14),
     title_font_size=20,
     title_x=0.02,
     margin=dict(l=20, r=20, t=60, b=20)
    )
    return fig