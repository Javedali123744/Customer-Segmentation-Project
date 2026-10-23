
import streamlit as st
import pandas as pd
import joblib

st.set_page_config(
    page_title="Customer Segmentation",
    page_icon="📊",
    layout="wide"
)

# Load the saved model and dataset
kmeans = joblib.load("kmeans_model.pkl")
df = pd.read_csv("customer_segments.csv")

st.title("Customer Segmentation Dashboard")
st.write(
    "Explore customer groups using K-Means clustering "
    "based on annual income and spending score."
)

# Sidebar inputs
st.sidebar.header("Enter Customer Details")

income = st.sidebar.slider(
    "Annual Income (k$)",
    min_value=15,
    max_value=140,
    value=50
)

spending = st.sidebar.slider(
    "Spending Score (1-100)",
    min_value=1,
    max_value=100,
    value=50
)

# Predict customer cluster
if st.sidebar.button("Identify Customer Segment"):
    customer = pd.DataFrame(
        [[income, spending]],
        columns=["Annual Income (k$)", "Spending Score (1-100)"]
    )

    cluster = int(kmeans.predict(customer)[0])

    st.subheader("Prediction Result")
    st.metric("Assigned Cluster", f"Cluster {cluster}")

    st.info(
        "This customer belongs to Cluster "
        f"{cluster}. Compare its income and spending "
        "characteristics with the cluster summary below."
    )

# Customer distribution
st.subheader("Customer Segment Summary")

summary = df.groupby("Cluster").agg(
    Customer_Count=("CustomerID", "count"),
    Average_Age=("Age", "mean"),
    Average_Income=("Annual Income (k$)", "mean"),
    Average_Spending_Score=("Spending Score (1-100)", "mean")
).round(2)

st.dataframe(summary, use_container_width=True)

# Visualize customer segments
st.subheader("Customer Segmentation Chart")

st.scatter_chart(
    df,
    x="Annual Income (k$)",
    y="Spending Score (1-100)",
    color="Cluster"
)

st.caption(
    "Educational demonstration using the Mall Customers dataset."
)
