import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

# Page Config - Full Width & Professional Theme
st.set_page_config(
    page_title="IT Company Financial Dashboard (80k)",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom Styling
st.markdown("""
    <style>
    .main { background-color: #0E1117; }
    .stMetric {
        background-color: #1E232A;
        padding: 15px;
        border-radius: 10px;
        border: 1px solid #2D3748;
    }
    div[data-testid="stMetricValue"] {
        font-size: 24px;
        font-weight: bold;
        color: #6366F1;
    }
    h1, h2, h3 { color: #F3F4F6; }
    </style>
""", unsafe_allow_html=True)

@st.cache_data
def generate_or_load_data():
    file_path = "IT_Company_Financial_Performance_80k.xlsx"
    try:
        df = pd.read_excel(file_path)
    except Exception:
        # Fallback generation if file not found in deployment environment
        np.random.seed(42)
        n_rows = 80000
        client_names = [
            "Acme Corp", "TechGlobe Inc", "FinTech Solutions", "Apex Healthcare", 
            "Omni Retail", "CloudScale Systems", "Nexus Logistics", "CyberGuard",
            "DataDynamics", "Vanguard Media", "Innovate Bio", "Quantum Analytics",
            "Global Telco", "Starlight Energy", "Alpha Investments"
        ]
        client_regions = ["North America", "Europe", "Asia-Pacific", "Latin America", "Middle East"]
        employee_roles = [
            "Software Engineer", "Senior Software Engineer", "DevOps Engineer", 
            "Data Scientist", "UI/UX Designer", "QA Automation Engineer", 
            "Cloud Architect", "Project Manager", "Business Analyst", "Tech Lead"
        ]
        departments = ["Engineering", "Cloud & Infra", "Data & AI", "Product & Design", "Quality Assurance"]

        clients = np.random.choice(client_names, size=n_rows)
        regions = np.random.choice(client_regions, size=n_rows)
        emp_ids = [f"EMP-{100000 + i}" for i in range(n_rows)]
        roles = np.random.choice(employee_roles, size=n_rows)
        depts = np.random.choice(departments, size=n_rows)
        base_salaries = np.random.randint(55000, 155000, size=n_rows)
        revenue_multipliers = np.random.uniform(1.8, 3.2, size=n_rows)
        client_revenues = np.round(base_salaries * revenue_multipliers, 2)
        overhead_rates = np.random.uniform(0.20, 0.35, size=n_rows)
        total_costs = np.round(base_salaries * (1 + overhead_rates), 2)
        profits = np.round(client_revenues - total_costs, 2)
        profit_margins = np.round((profits / client_revenues) * 100, 2)

        df = pd.DataFrame({
            "Employee ID": emp_ids,
            "Department": depts,
            "Role": roles,
            "Client Name": clients,
            "Client Region": regions,
            "Annual Salary ($)": base_salaries,
            "Total Overhead Cost ($)": np.round(base_salaries * overhead_rates, 2),
            "Total Direct Cost ($)": total_costs,
            "Client Revenue Generated ($)": client_revenues,
            "Net Profit ($)": profits,
            "Profit Margin (%)": profit_margins
        })
    return df

df = generate_or_load_data()

# Header Section
st.title("💼 Enterprise Financial & Resource Dashboard")
st.caption("Real-time executive analytics for 80,000 IT employee assignments, revenues, costs, and profit margins.")
st.markdown("---")

# Sidebar Filters
st.sidebar.header("🔍 Executive Filters")
selected_regions = st.sidebar.multiselect("Select Client Region", options=df["Client Region"].unique(), default=df["Client Region"].unique())
selected_depts = st.sidebar.multiselect("Select Department", options=df["Department"].unique(), default=df["Department"].unique())
selected_clients = st.sidebar.multiselect("Select Top Clients", options=df["Client Name"].unique(), default=df["Client Name"].unique()[:5])

filtered_df = df[
    (df["Client Region"].isin(selected_regions)) &
    (df["Department"].isin(selected_depts)) &
    (df["Client Name"].isin(selected_clients))
]

# Top KPI Summary Cards
col1, col2, col3, col4, col5 = st.columns(5)
total_rev = filtered_df["Client Revenue Generated ($)"].sum()
total_cost = filtered_df["Total Direct Cost ($)"].sum()
total_profit = filtered_df["Net Profit ($)"].sum()
avg_margin = filtered_df["Profit Margin (%)"].mean()
total_emps = len(filtered_df)

col1.metric("Total Revenue", f"${total_rev/1e6:.2f}M")
col2.metric("Total Cost", f"${total_cost/1e6:.2f}M")
col3.metric("Net Profit", f"${total_profit/1e6:.2f}M")
col4.metric("Avg Profit Margin", f"{avg_margin:.1f}%")
col5.metric("Resources Billed", f"{total_emps:,}")

st.markdown("---")

# Visualizations Row 1
c1, c2 = st.columns(2)

with c1:
    st.subheader("🏢 Revenue & Profit by Client")
    client_summary = filtered_df.groupby("Client Name")[["Client Revenue Generated ($)", "Net Profit ($)"]].sum().reset_index()
    fig1 = px.bar(
        client_summary, x="Client Name", y=["Client Revenue Generated ($)", "Net Profit ($)"],
        barmode="group", color_discrete_sequence=["#6366F1", "#10B981"],
        labels={"value": "Amount ($)", "variable": "Metric"}
    )
    fig1.update_layout(template="plotly_dark", height=400)
    st.plotly_chart(fig1, use_container_width=True)

with c2:
    st.subheader("🌐 Financial Breakdown by Region")
    region_summary = filtered_df.groupby("Client Region")[["Client Revenue Generated ($)", "Net Profit ($)"]].sum().reset_index()
    fig2 = px.pie(
        region_summary, values="Client Revenue Generated ($)", names="Client Region",
        hole=0.4, color_discrete_sequence=px.colors.qualitative.Dark24
    )
    fig2.update_layout(template="plotly_dark", height=400)
    st.plotly_chart(fig2, use_container_width=True)

# Visualizations Row 2
c3, c4 = st.columns(2)

with c3:
    st.subheader("🛠️ Cost vs Revenue by Department")
    dept_summary = filtered_df.groupby("Department")[["Total Direct Cost ($)", "Client Revenue Generated ($)"]].sum().reset_index()
    fig3 = px.scatter(
        dept_summary, x="Total Direct Cost ($)", y="Client Revenue Generated ($)",
        size="Client Revenue Generated ($)", color="Department",
        hover_name="Department", text="Department"
    )
    fig3.update_layout(template="plotly_dark", height=400)
    st.plotly_chart(fig3, use_container_width=True)

with c4:
    st.subheader("👨‍💻 Salary Distribution Across Roles")
    fig4 = px.box(
        filtered_df, x="Role", y="Annual Salary ($)", color="Role"
    )
    fig4.update_layout(template="plotly_dark", height=400, showlegend=False)
    fig4.update_xaxes(tickangle=45)
    st.plotly_chart(fig4, use_container_width=True)

# Data Table View
st.markdown("---")
st.subheader("📄 Interactive Data Explorer (Filtered Records)")
st.dataframe(filtered_df.head(1000), use_container_width=True)
