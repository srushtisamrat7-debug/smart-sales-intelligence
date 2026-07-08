import streamlit as st
import pandas as pd
import plotly.express as px

from utils.ask_data import answer_question
from utils.cleaning import clean_data
from utils.calculations import calculate_kpis
from utils.charts import (
    monthly_sales_chart,
    category_sales_chart,
    region_sales_chart,
    top_products_chart,
    top_customers_chart,
    category_profit_chart,
    discount_profit_chart,
    repeat_customer_chart,
    customer_segment_chart,
    state_sales_chart,
    city_sales_chart
)
from utils.insights import generate_insights
from utils.recommendations import generate_recommendations
from utils.forecasting import forecast_sales
from utils.report import generate_pdf_report
from utils.formatting import format_currency
from utils.formatting import format_currency


def load_css(file_path):
    with open(file_path) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
def login_page():
    col1, col2, col3 = st.columns([2, 1, 2])

    with col2:
        st.image("assets/logo.png", width=120)
    st.markdown("""
    <div style="
    max-width:450px;
    margin:80px auto;
    background:rgba(255,255,255,0.18);
    padding:35px;
    border-radius:28px;
    text-align:center;
    box-shadow:0 20px 50px rgba(0,0,0,0.25);
    backdrop-filter:blur(18px);
    border:1px solid rgba(255,255,255,0.35);
    ">
    <h1 style="color:white;">
    Welcome Back 👋
    </h1>

    <div style="font-size:18px;color:#d9f3ff;margin-top:15px;">
    Sign in to Smart Sales Intelligence
    </div>

    <div style="color:#e0f2fe;margin-top:8px;">
    Smart Sales Intelligence System
    </div>
    </div>
    """, unsafe_allow_html=True)

    email = st.text_input(
        "📧 Email",
        placeholder="demo@smartsales.com"
    )
    password = st.text_input(
        "🔒 Password",
        type="password",
        placeholder="Enter password"
    )
    remember = st.checkbox("Remember me")

    if st.button("🚀 Sign In", use_container_width=True):

        email_clean = email.strip()
        password_clean = password.strip()

        if email_clean == "demo@smartsales.com" and password_clean == "SmartSales@2026":
            st.session_state["logged_in"] = True
            st.session_state["user_email"] = email_clean
            st.rerun()
        else:
            st.error("Invalid Email or Password")

    st.markdown(
        "<center><a href='#'>Forgot Password?</a></center>",
        unsafe_allow_html=True
    )
        
    st.info("""
    ### Demo Login

    Email:
    demo@smartsales.com

    Password:
    SmartSales@2026
    """)

def logout_button():
    if st.sidebar.button("🚪 Logout"):
        st.session_state["logged_in"] = False
        st.session_state["user_email"] = ""
        st.rerun()

st.set_page_config(
    page_title="Smart Sales Intelligence",
    page_icon="assets/logo.png",
    layout="wide",
    initial_sidebar_state="expanded"
)

load_css("assets/style.css")
if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False

if "user_email" not in st.session_state:
    st.session_state["user_email"] = ""

if not st.session_state["logged_in"]:
    login_page()
    st.stop()
st.markdown("""
<div style="
    background: linear-gradient(135deg,#2563eb 0%,#7c3aed 55%,#db2777 100%);
    padding:40px;
    border-radius:28px;
    margin-bottom:30px;
">

<h1 style="color:white !important;font-size:48px;margin:0;">
📊 Smart Sales Intelligence System
</h1>

<p style="color:#eef2ff !important;font-size:20px;margin-top:15px;">
Upload e-commerce data, generate dashboards, forecasts, insights and executive reports automatically.
</p>

</div>
""", unsafe_allow_html=True)

uploaded_file = st.file_uploader("📂 Upload Dataset", type=["csv", "xlsx"])
st.sidebar.markdown("---")

st.sidebar.markdown("---")

st.sidebar.markdown("## 📊 Smart Sales Intelligence")

st.sidebar.info(
    "Upload sales data to generate dashboards, forecasts, reports and business insights."
)

st.sidebar.markdown("### 🚀 Features")
st.sidebar.markdown("""
- 📈 Interactive Dashboard
- 📊 Sales Analytics
- 🤖 AI Business Assistant
- 🔮 30-Day Forecasting
- 📄 Executive PDF Report
""")

st.sidebar.markdown("---")

st.sidebar.markdown("### 👨‍💻 Developed By")
st.sidebar.write("Srushti Samrat")

st.sidebar.markdown("### 🛠 Tech Stack")
st.sidebar.markdown("""
- Python
- Streamlit
- Pandas
- Plotly
- Prophet
- ReportLab
""")

st.sidebar.markdown("---")
st.sidebar.caption("Version 1.0")
page = st.sidebar.radio(
    "📌 Navigation",
    [
        "🏠 Dashboard",
        "📈 Forecast",
        "🤖 AI Assistant",
        "📄 Reports",
        "ℹ About Project"
    ]
)
st.sidebar.markdown("---")
st.sidebar.success(f"Logged in as: {st.session_state.user_email}")
logout_button()
if uploaded_file is not None:

    if uploaded_file.name.endswith(".csv"):
        try:
            df = pd.read_csv(uploaded_file, encoding="utf-8")
        except UnicodeDecodeError:
            uploaded_file.seek(0)
            df = pd.read_csv(uploaded_file, encoding="latin1")
    else:
        df = pd.read_excel(uploaded_file)

    df = clean_data(df)
    USD_TO_INR = 86

    df["Sales"] = df["Sales"] * USD_TO_INR
    df["Profit"] = df["Profit"] * USD_TO_INR
    if page == "ℹ About Project":
        st.markdown("## ℹ About Project")

        st.markdown("""
    ### 🎯 Objective
    Smart Sales Intelligence System helps users upload sales data and automatically generate business dashboards, forecasts, insights, and reports.

    ### 📦 Dataset
    The project uses sales data with fields such as order date, region, category, product, customer, sales, profit, discount, and quantity.

    ### 🛠 Tech Stack
    - Python
    - Streamlit
    - Pandas
    - Plotly
    - Prophet
    - ReportLab

    ### 🔄 Workflow
    1. Upload CSV or Excel file  
    2. Clean and prepare the dataset  
    3. Apply filters  
    4. Generate KPIs and visual dashboards  
    5. Produce business insights and recommendations  
    6. Forecast future sales  
    7. Download executive PDF report  

    ### ⭐ Key Features
    - Interactive KPI dashboard
    - Region, product, customer, and profit analysis
    - 30-day sales forecasting
    - AI-style business Q&A
    - Executive PDF report
    - Glassmorphism UI theme
    """)
    st.sidebar.header("🔎 Filters")

    date_range = st.sidebar.date_input(
        "📅 Select Date Range",
        [df["Order Date"].min(), df["Order Date"].max()]
    )

    regions = st.sidebar.multiselect(
        "🌎 Select Region",
        options=df["Region"].unique(),
        default=df["Region"].unique()
    )

    categories = st.sidebar.multiselect(
        "📦 Select Category",
        options=df["Category"].unique(),
        default=df["Category"].unique()
    )

    segments = st.sidebar.multiselect(
        "👥 Select Segment",
        options=df["Segment"].unique(),
        default=df["Segment"].unique()
    )

    filtered_df = df[
        (df["Region"].isin(regions)) &
        (df["Category"].isin(categories)) &
        (df["Segment"].isin(segments))
    ]

    if len(date_range) == 2:
        start_date, end_date = date_range
        filtered_df = filtered_df[
            (filtered_df["Order Date"].dt.date >= start_date) &
            (filtered_df["Order Date"].dt.date <= end_date)
        ]
    if filtered_df.empty:
        st.warning("⚠️ No data found for the selected filters. Please change the date range or filters.")
        st.stop()

    total_sales, total_profit, total_orders, total_customers, avg_order_value, profit_margin, monthly_growth = calculate_kpis(filtered_df)
    insights = generate_insights(filtered_df)
    recommendations = generate_recommendations(filtered_df)

    if page == "🏠 Dashboard":
    
            # ---------------- ACTIVE FILTER SUMMARY ----------------
        st.markdown("## 🎯 Current Filters")

        selected_start = start_date.strftime("%b %d, %Y")
        selected_end = end_date.strftime("%b %d, %Y")

        filter_col1, filter_col2, filter_col3, filter_col4 = st.columns(4)

        filter_col1.info(f"📅 {selected_start} - {selected_end}")
        filter_col2.info(f"🌍 {', '.join(regions)}")
        filter_col3.info(f"📦 {', '.join(categories)}")
        filter_col4.info(f"👥 {', '.join(segments)}")

        st.success("File uploaded successfully!")
        st.markdown("## 📄 Dataset Summary")

        rows = filtered_df.shape[0]
        cols = filtered_df.shape[1]
        missing_values = filtered_df.isnull().sum().sum()

        d1, d2, d3 = st.columns(3)

        d1.metric("Rows", f"{rows:,}")
        d2.metric("Columns", f"{cols:,}")
        d3.metric("Missing Values", f"{missing_values:,}")

        st.divider()
        st.markdown("## 📊 Sales Overview")

        col1, col2, col3, col4 = st.columns(4)
        col1.metric("💰 Revenue", format_currency(total_sales))
        col2.metric("📈 Profit", format_currency(total_profit))
        col3.metric("📦 Orders", f"{total_orders:,}")
        col4.metric("👥 Customers", f"{total_customers:,}")

        col5, col6, col7 = st.columns(3)
        col5.metric("🛒 Avg Order", format_currency(avg_order_value))
        col6.metric("💹 Margin", f"{profit_margin:.1f}%")
        col7.metric("📊 Growth", f"{monthly_growth:.1f}%")

        st.divider()

        st.markdown("## 📈 Monthly Sales Trend")
        fig_monthly = monthly_sales_chart(filtered_df)
        st.plotly_chart(fig_monthly, use_container_width=True)

        left_col, right_col = st.columns(2)

        with left_col:
            fig_category = category_sales_chart(filtered_df)
            st.plotly_chart(fig_category, use_container_width=True)

        with right_col:
            fig_region = region_sales_chart(filtered_df)
            st.plotly_chart(fig_region, use_container_width=True)

        left_col, right_col = st.columns(2)

        with left_col:
            fig_products = top_products_chart(filtered_df)
            st.plotly_chart(fig_products, use_container_width=True)

        with right_col:
            fig_customers = top_customers_chart(filtered_df)
            st.plotly_chart(fig_customers, use_container_width=True)

        st.markdown("## 💵 Profit Analysis")

        left_col, right_col = st.columns(2)

        with left_col:
            fig_profit_category = category_profit_chart(filtered_df)
            st.plotly_chart(fig_profit_category, use_container_width=True)

        with right_col:
            fig_discount_profit = discount_profit_chart(filtered_df)
            st.plotly_chart(fig_discount_profit, use_container_width=True)

        st.markdown("## 👥 Customer Analysis")

        left_col, right_col = st.columns(2)

        with left_col:
            fig_repeat_customer = repeat_customer_chart(filtered_df)
            st.plotly_chart(fig_repeat_customer, use_container_width=True)

        with right_col:
            fig_customer_segment = customer_segment_chart(filtered_df)
            st.plotly_chart(fig_customer_segment, use_container_width=True)

        st.divider()

        st.markdown("## 🌍 Regional Analysis")

        left_col, right_col = st.columns(2)

        with left_col:
            fig_state_sales = state_sales_chart(filtered_df)
            st.plotly_chart(fig_state_sales, use_container_width=True)

        with right_col:
            fig_city_sales = city_sales_chart(filtered_df)
            st.plotly_chart(fig_city_sales, use_container_width=True)

        st.divider()

        st.markdown("## 🤖 Business Intelligence")

        for item in insights:
            st.info(item)

        st.markdown("## 💡 Smart Recommendations")

        for item in recommendations:
            st.success(item)

        pdf_report = generate_pdf_report(
            total_sales,
            total_profit,
            total_orders,
            total_customers,
            avg_order_value,
            insights,
            recommendations
        )

        st.download_button(
            label="📄 Download Executive PDF Report",
            data=pdf_report,
            file_name="sales_intelligence_report.pdf",
            mime="application/pdf"
        )

        st.divider()

        st.markdown("## 🔮 30-Day Sales Forecast")

        if st.button("Generate Forecast"):

            with st.spinner("🔮 Generating 30-Day Forecast..."):
                forecast = forecast_sales(filtered_df, periods=30)

            forecast_display = forecast[["ds", "yhat", "yhat_lower", "yhat_upper"]].tail(30)
            expected_sales = forecast_display["yhat"].sum()
            avg_daily_sales = forecast_display["yhat"].mean()
            best_day = forecast_display.loc[forecast_display["yhat"].idxmax(), "ds"]

            fcol1, fcol2, fcol3 = st.columns(3)
            fcol1.metric("📈 Expected 30-Day Sales", format_currency(expected_sales))
            fcol2.metric("🗓️ Avg Daily Sales", format_currency(avg_daily_sales))
            fcol3.metric("⭐ Peak Forecast Day", best_day.strftime("%b %d, %Y"))
            st.dataframe(forecast_display, use_container_width=True)

            forecast_chart = forecast[["ds", "yhat", "yhat_lower", "yhat_upper"]]

            fig_forecast = px.line(
                forecast_chart,
                x="ds",
                y=["yhat", "yhat_lower", "yhat_upper"],
                title="30-Day Sales Forecast",
                labels={
                    "ds": "Date",
                    "value": "Sales Forecast",
                    "variable": "Forecast Type"
                }
            )

            fig_forecast.update_layout(
                template="plotly_white",
                paper_bgcolor="white",
                plot_bgcolor="white",
                font=dict(size=14),
                title_font_size=20,
                title_x=0.02,
                margin=dict(l=20, r=20, t=60, b=20)
            )

            st.plotly_chart(fig_forecast, use_container_width=True)
        st.markdown("🤖 AI Business Assistant")

        user_question = st.text_input(
            "Ask a business question about your uploaded data",
            placeholder="Example: Which region has highest sales?"
        )

        if user_question:
            answer = answer_question(filtered_df, user_question)
            st.info(answer)
        csv = filtered_df.to_csv(index=False).encode("utf-8")

        st.download_button(
            "📥 Download Filtered Data CSV",
            csv,
            "filtered_sales_data.csv",
            "text/csv"
        )

        with st.expander("📄 View Data Preview"):
            st.dataframe(filtered_df.head(20), use_container_width=True)

        with st.expander("🧾 View Column Names"):
            st.write(list(filtered_df.columns))
    elif page == "📈 Forecast":

        st.header("🔮 30-Day Sales Forecast")

        if st.button("Generate Forecast"):

            with st.spinner("Generating forecast..."):

                forecast = forecast_sales(filtered_df, periods=30)

                forecast_display = forecast[["ds","yhat","yhat_lower","yhat_upper"]].tail(30)

                st.dataframe(forecast_display, use_container_width=True)

                fig = px.line(
                    forecast_display,
                    x="ds",
                    y=["yhat","yhat_lower","yhat_upper"],
                    title="30-Day Sales Forecast"
                )

                st.plotly_chart(fig, use_container_width=True)
    elif page == "🤖 AI Assistant":

        st.header("🤖 AI Business Assistant")
        st.caption("💡 Example questions you can ask:")

        st.markdown("""
        - Which region has highest sales?
        - Top 5 customers
        - Average order value
        - Most profitable state
        - Dataset summary
        - Lowest performing segment
        - Show monthly sales trend
        """)

        question = st.text_input(
            "Ask any question about your data"
    )

        if question:

            answer = answer_question(filtered_df, question)

            st.success(answer)

        with st.expander("📄 Preview Data"):
            st.dataframe(filtered_df.head(20))

        with st.expander("📋 Column Names"):
            st.write(filtered_df.columns.tolist())
            
    elif page == "📄 Reports":

        st.header("📄 Executive Report")

        pdf_report = generate_pdf_report(
            total_sales,
            total_profit,
            total_orders,

            total_customers,
            avg_order_value,
            insights,
            recommendations
        )

        st.download_button(
            "📄 Download Executive PDF",
            pdf_report,
            file_name="Sales_Report.pdf",
            mime="application/pdf"
        )

else:
    st.markdown("""
## 👋 Welcome!

Upload a **CSV or Excel sales dataset** to unlock:

### 📊 Interactive KPI Dashboard

### 📈 Sales Analytics

### 🔮 30-Day Sales Forecast

### 🤖 AI Business Assistant

### 📄 Executive PDF Report

---

**Supported Files:** CSV, XLSX
""")
st.markdown("---")

st.markdown("""
<div style="
background:rgba(255,255,255,0.12);
padding:25px;
border-radius:20px;
text-align:center;
color:white;
margin-top:30px;
margin-bottom:20px;
box-shadow:0 10px 30px rgba(0,0,0,.2);
">

<h2>📊 Smart Sales Intelligence System</h2>

<p style="font-size:18px;">
Version 1.0
</p>

<p style="color:#d9f3ff;">
Built with ❤️ using Python • Streamlit • Plotly • Prophet • Pandas
</p>

<p style="
font-size:14px;
color:white;
font-weight:500;
margin-top:18px;
">
© 2026 | Designed by Srushti Samrat
</p>

</div>
""", unsafe_allow_html=True)