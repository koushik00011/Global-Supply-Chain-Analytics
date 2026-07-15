# ==========================================================
# 🚀 IMPORT LIBRARIES
# ==========================================================

import streamlit as st
import pandas as pd
import numpy as np
import joblib
from pathlib import Path

# Optional (used later for charts)
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go

# Suppress warnings
import warnings
warnings.filterwarnings("ignore")


# ==========================================================
# ⚙️ PAGE CONFIGURATION
# ==========================================================

st.set_page_config(
    page_title="Supply Chain Late Delivery Prediction",
    page_icon="🚚",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ==========================================================
# 🤖 LOAD MACHINE LEARNING MODEL
# ==========================================================

# Project Directory
BASE_DIR = Path(__file__).resolve().parent

# Model Path
MODEL_PATH = BASE_DIR / "model" / "rf_pipeline.pkl"


@st.cache_resource
def load_model():
    """
    Loads the trained Random Forest Pipeline.
    The model is cached so it is loaded only once.
    """
    model = joblib.load(MODEL_PATH)
    return model


# Load Model
model = load_model()


# ==========================================================
# 📂 LOAD DATASET
# ==========================================================

DATA_PATH_1 = BASE_DIR / "data" / "supply_cleaned_data.csv"
DATA_PATH_2 = BASE_DIR / "supply_cleaned_data.csv"


@st.cache_data
def load_dataset():
    """
    Loads the cleaned supply chain dataset.
    It first checks the data folder.
    If not found, it checks the project root.
    """

    if DATA_PATH_1.exists():
        df = pd.read_csv(DATA_PATH_1)

    elif DATA_PATH_2.exists():
        df = pd.read_csv(DATA_PATH_2)

    else:
        st.error("❌ Dataset not found.")
        st.stop()

    return df


# Load Dataset
df = load_dataset()
# ==========================================================
# 📋 SIDEBAR
# ==========================================================

with st.sidebar:

    st.image(
        "https://img.icons8.com/fluency/96/delivery.png",
        width=80
    )

    st.title("Supply Chain AI")

    st.markdown("---")

    st.subheader("🤖 Model")

    st.info("""
Random Forest Classifier

Version : 1.0
""")

    st.subheader("📈 Performance")

    st.metric("Accuracy","74.32%")

    st.metric("Precision","82.79%")

    st.metric("Recall","67.12%")

    st.metric("ROC AUC","0.75")

    st.markdown("---")

    st.subheader("📊 Dataset")

    st.write(f"**Records :** {len(df):,}")

    st.write(f"**Features :** {df.shape[1]}")

    st.markdown("---")

    st.subheader("👨‍💻 Developer")

    st.write("Koushik Naidu")

    st.markdown("---")

    st.caption(
        "AI Powered Supply Chain Late Delivery Prediction System"
    )
# ==========================================================
# 🚚 HERO SECTION
# ==========================================================

st.markdown(f"""
<div class="hero">

<h1>🚚 AI Supply Chain Intelligence</h1>

<p>
Predict shipment delays before dispatch using Machine Learning.
</p>

<span class="badge">🤖 Random Forest</span>
<span class="badge">📦 180,519 Orders</span>
<span class="badge">📈 Accuracy 74.32%</span>
<span class="badge">🚚 Risk Prediction</span>

</div>
""", unsafe_allow_html=True)
# ==========================================================
# ℹ️ ABOUT APPLICATION
# ==========================================================

st.markdown('<div class="section-title">📌 About This Application</div>',
            unsafe_allow_html=True)

st.markdown("""
<div class="card">

<h3 style="color:#2563EB;">
Why this application?
</h3>

<p class="description">

Late deliveries directly impact customer satisfaction,
increase operational costs, and reduce overall supply chain efficiency.

This application leverages a trained <b>Random Forest Machine Learning model</b>
to predict whether a shipment is likely to be delivered late before dispatch.

Rather than reacting after delays occur, logistics teams can proactively identify
high-risk shipments and take preventive actions.

</p>

<hr>

<h3 style="color:#2563EB;">
🚀 What this application provides
</h3>

<ul class="description">

<li>Predict shipment delay risk using Machine Learning.</li>

<li>Estimate the probability of late delivery.</li>

<li>Provide an AI-generated explanation for every prediction.</li>

<li>Recommend actionable business strategies to reduce delivery risk.</li>

<li>Highlight the most influential features affecting the prediction.</li>

</ul>

<hr>

<h3 style="color:#2563EB;">
💼 Business Value
</h3>

<ul class="description">

<li>Improve logistics planning.</li>

<li>Reduce delivery delays.</li>

<li>Increase customer satisfaction.</li>

<li>Support data-driven operational decisions.</li>

<li>Minimize financial losses caused by delayed shipments.</li>

</ul>

</div>
""", unsafe_allow_html=True)
# ==========================================================
# 📊 MODEL INFORMATION
# ==========================================================

st.markdown('<div class="section-title">🤖 Machine Learning Model</div>',
            unsafe_allow_html=True)

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown("""
    <div class="card" style="text-align:center;">
        <h4>Algorithm</h4>
        <h2 style="color:#2563EB;">Random Forest</h2>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="card" style="text-align:center;">
        <h4>Accuracy</h4>
        <h2 style="color:#16A34A;">74.32%</h2>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="card" style="text-align:center;">
        <h4>ROC-AUC</h4>
        <h2 style="color:#F59E0B;">0.75</h2>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown(f"""
    <div class="card" style="text-align:center;">
        <h4>Dataset Size</h4>
        <h2 style="color:#DC2626;">{len(df):,}</h2>
    </div>
    """, unsafe_allow_html=True)
# ==========================================================
# 📝 SHIPMENT INPUT FORM
# ==========================================================

st.markdown(
    '<div class="section-title">📦 Shipment Details</div>',
    unsafe_allow_html=True
)

st.markdown("""
<div class="card">
<p class="description">
Enter the shipment details below. The AI model will analyze the information
and predict whether the shipment is likely to be delivered late.
</p>
</div>
""", unsafe_allow_html=True)

# ==========================================================
# 👤 CUSTOMER INFORMATION | 📦 PRODUCT INFORMATION
# ==========================================================

customer_col, product_col = st.columns(2)

with customer_col:

    st.markdown("### 👤 Customer Information")

    customer_segment = st.selectbox(
        "Customer Segment",
        sorted(df["customer_segment"].dropna().unique())
    )

    customer_country = st.selectbox(
        "Customer Country",
        sorted(df["customer_country"].dropna().unique())
    )

    customer_state = st.selectbox(
        "Customer State",
        sorted(df["customer_state"].dropna().unique())
    )

    customer_zipcode = st.number_input(
        "Customer Zip Code",
        min_value=0,
        value=10001
    )

with product_col:

    st.markdown("### 📦 Product Information")

    department_name = st.selectbox(
        "Department",
        sorted(df["department_name"].dropna().unique())
    )

    category_name = st.selectbox(
        "Category",
        sorted(df["category_name"].dropna().unique())
    )

    product_name = st.selectbox(
        "Product",
        sorted(df["product_name"].dropna().unique())
    )

    product_price = st.number_input(
        "Product Price",
        min_value=0.0,
        value=100.0,
        step=1.0
    )

# ==========================================================
# 🚚 SHIPPING INFORMATION | 💰 FINANCIAL INFORMATION
# ==========================================================

shipping_col, finance_col = st.columns(2)

with shipping_col:

    st.markdown("### 🚚 Shipping Information")

    shipping_mode = st.selectbox(
        "Shipping Mode",
        sorted(df["shipping_mode"].dropna().unique())
    )

    market = st.selectbox(
        "Market",
        sorted(df["market"].dropna().unique())
    )

    order_region = st.selectbox(
        "Order Region",
        sorted(df["order_region"].dropna().unique())
    )

    order_country = st.selectbox(
        "Order Country",
        sorted(df["order_country"].dropna().unique())
    )

    order_status = st.selectbox(
        "Order Status",
        sorted(df["order_status"].dropna().unique())
    )

    order_type = st.selectbox(
        "Order Type",
        sorted(df["type"].dropna().unique())
    )

    scheduled_shipping_days = st.slider(
        "Scheduled Shipping Days",
        1,
        7,
        3
    )

with finance_col:

    st.markdown("### 💰 Financial Information")

    sales = st.number_input(
        "Sales",
        min_value=0.0,
        value=500.0
    )

    sales_per_customer = st.number_input(
        "Sales Per Customer",
        min_value=0.0,
        value=500.0
    )

    benefit_per_order = st.number_input(
        "Benefit Per Order",
        value=25.0
    )

    order_profit_per_order = st.number_input(
        "Order Profit Per Order",
        value=30.0
    )

    order_item_discount = st.number_input(
        "Order Item Discount",
        value=10.0
    )

    order_item_discount_rate = st.slider(
        "Discount Rate",
        0.00,
        1.00,
        0.10
    )

    order_item_quantity = st.number_input(
        "Order Quantity",
        min_value=1,
        value=1
    )

# ==========================================================
# 📍 LOCATION INFORMATION
# ==========================================================

st.markdown("### 📍 Location Information")

loc1, loc2 = st.columns(2)

with loc1:

    latitude = st.number_input(
        "Latitude",
        value=0.0,
        format="%.6f"
    )

with loc2:

    longitude = st.number_input(
        "Longitude",
        value=0.0,
        format="%.6f"
    )
# ==========================================================
# 📦 CREATE INPUT DATAFRAME
# ==========================================================

# Automatically derive model features
category_id = (
    df.loc[df["category_name"] == category_name, "category_id"]
      .mode()
      .iloc[0]
)

department_id = (
    df.loc[df["department_name"] == department_name, "department_id"]
      .mode()
      .iloc[0]
)

order_item_product_price = product_price

order_item_total = (
    product_price * order_item_quantity
) - order_item_discount

order_item_profit_ratio = (
    order_profit_per_order / sales
    if sales != 0 else 0
)

# Create dataframe exactly as model expects

input_df = pd.DataFrame({

    "type":[order_type],

    "scheduled_shipping_days":[scheduled_shipping_days],

    "benefit_per_order":[benefit_per_order],

    "sales_per_customer":[sales_per_customer],

    "category_id":[category_id],

    "category_name":[category_name],

    "customer_country":[customer_country],

    "customer_segment":[customer_segment],

    "customer_state":[customer_state],

    "customer_zipcode":[customer_zipcode],

    "department_id":[department_id],

    "department_name":[department_name],

    "latitude":[latitude],

    "longitude":[longitude],

    "market":[market],

    "order_country":[order_country],

    "order_item_discount":[order_item_discount],

    "order_item_discount_rate":[order_item_discount_rate],

    "order_item_product_price":[order_item_product_price],

    "order_item_profit_ratio":[order_item_profit_ratio],

    "order_item_quantity":[order_item_quantity],

    "sales":[sales],

    "order_item_total":[order_item_total],

    "order_profit_per_order":[order_profit_per_order],

    "order_region":[order_region],

    "order_status":[order_status],

    "product_name":[product_name],

    "product_price":[product_price],

    "shipping_mode":[shipping_mode]

})
# ==========================================================
# 🚀 PREDICTION BUTTON
# ==========================================================

st.markdown("<br>", unsafe_allow_html=True)

predict = st.button(
    "🚚 Predict Shipment Risk",
    use_container_width=True,
    type="primary"
)
# ==========================================================
# 🤖 MACHINE LEARNING PREDICTION
# ==========================================================

if predict:

    st.write("### Input DataFrame")
    st.dataframe(input_df)

    st.write("### Column Names")
    st.write(input_df.columns.tolist())

    st.write("### Data Types")
    st.write(input_df.dtypes)

    try:
        prediction = model.predict(input_df)[0]
        probability = model.predict_proba(input_df)[0]

        late_probability = probability[1] * 100
        ontime_probability = probability[0] * 100

    except Exception as e:
        st.error(f"Prediction Error: {e}")
        st.stop()
# ==========================================================
# 🎯 PREDICTION RESULT
# ==========================================================

    st.markdown("---")

    st.markdown("## 🎯 Prediction Result")

    if prediction == 1:

        st.error("## 🔴 HIGH RISK OF LATE DELIVERY")

    else:

        st.success("## 🟢 LOW RISK OF LATE DELIVERY")
# ==========================================================
# 📈 PREDICTION PROBABILITY
# ==========================================================

    st.markdown("## 📈 Prediction Probability")

    if prediction == 1:

        st.progress(late_probability / 100)

        st.metric(
            "Late Delivery Probability",
            f"{late_probability:.2f}%"
        )

    else:

        st.progress(ontime_probability / 100)

        st.metric(
            "On-Time Delivery Probability",
            f"{ontime_probability:.2f}%"
        )
# ==========================================================
# 🚨 RISK LEVEL
# ==========================================================

    st.markdown("## 🚨 Risk Level")

    if late_probability >= 90:

        risk = "Very High"

    elif late_probability >= 75:

        risk = "High"

    elif late_probability >= 50:

        risk = "Medium"

    else:

        risk = "Low"

    st.info(f"### Risk Level : **{risk}**")
# ==========================================================
# 🧠 AI EXPLANATION
# ==========================================================

    st.markdown("## 🧠 AI Explanation")

    explanation = []

    if shipping_mode == "Standard Class":
        explanation.append(
            "• Standard Class shipping generally has longer transit times."
        )

    if scheduled_shipping_days <= 2:
        explanation.append(
            "• A short scheduled shipping window increases delivery risk."
        )

    if order_item_quantity >= 5:
        explanation.append(
            "• Higher order quantities can increase warehouse processing time."
        )

    if order_item_discount_rate >= 0.30:
        explanation.append(
            "• Large discounts often indicate promotional periods with higher order volumes."
        )

    if late_probability >= 80:
        explanation.append(
            "• The model predicts a very high likelihood of shipment delay based on the overall feature combination."
        )

    if not explanation:
        explanation.append(
            "• The shipment characteristics indicate a relatively low delivery risk."
        )

    st.markdown("### Why did the model make this prediction?")

    for item in explanation:

        st.write(item)
# ==========================================================
# 💡 BUSINESS RECOMMENDATIONS
# ==========================================================

    st.markdown("## 💡 Business Recommendations")

    recommendations = []

    if prediction == 1:

        recommendations.extend([

            "🚚 Upgrade to a faster shipping method.",

            "📦 Prioritize warehouse processing.",

            "📞 Notify the customer about possible delivery delays.",

            "📍 Increase shipment tracking frequency.",

            "⚠️ Assign the shipment to logistics monitoring."

        ])

    else:

        recommendations.extend([

            "✅ Shipment is expected to arrive on time.",

            "📦 Continue with the current shipping plan.",

            "📈 Monitor shipment using standard tracking procedures."

        ])

    for rec in recommendations:

        st.success(rec)