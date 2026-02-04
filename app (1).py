import streamlit as st
import pandas as pd
import pickle
import plotly.graph_objects as go

# =====================================================
# PAGE CONFIG
# =====================================================
st.set_page_config(
    page_title="Bank Term Deposit Dashboard",
    page_icon="🏦",
    layout="wide"
)

# =====================================================
# LOAD MODEL (LOGIC TETAP)
# =====================================================
@st.cache_resource
def load_model():
    with open("pipeline.pkl", "rb") as f:
        model = pickle.load(f)
    return model

model = load_model()

# =====================================================
# HEADER
# =====================================================
st.markdown("""
<h1 style='margin-bottom:0'>🏦 Bank Term Deposit Prediction Dashboard</h1>
<p style='color:gray; margin-top:5px'>
Decision Support System for Telemarketing Campaign Optimization
</p>
""", unsafe_allow_html=True)

st.markdown("---")

# =====================================================
# EXECUTIVE INFO BAR
# =====================================================
kpi_a, kpi_b, kpi_c = st.columns(3)

with kpi_a:
    st.markdown("### 🎯 Business Objective")
    st.caption(
        "Optimize telemarketing campaign efficiency by identifying "
        "high-potential customers before contact is made."
    )

with kpi_b:
    st.markdown("### 📊 Model Focus")
    st.caption(
        "Prediction model optimized for **precision**, "
        "prioritizing quality of leads over call volume."
    )

with kpi_c:
    st.markdown("### ⚠️ Important Note")
    st.caption(
        "Call duration is excluded to prevent data leakage "
        "and ensure fair real-world inference."
    )

st.markdown("---")

# =====================================================
# SIDEBAR — INPUT NASABAH
# =====================================================
with st.sidebar:
    st.markdown("## 📋 Customer Input")

    age = st.number_input("Age", 18, 100, 35)

    job = st.selectbox(
        "Job",
        ["admin.", "blue-collar", "entrepreneur", "housemaid",
         "management", "retired", "self-employed", "services",
         "student", "technician", "unemployed", "unknown"]
    )

    marital = st.selectbox("Marital Status", ["married", "single", "divorced"])

    education = st.selectbox(
        "Education",
        ["primary", "secondary", "tertiary", "unknown"]
    )

    balance = st.number_input(
        "Average Yearly Balance (€)",
        min_value=-10000,
        max_value=150000,
        step=500,
        value=1000
    )

    default = st.selectbox("Credit in Default?", ["yes", "no"])
    housing = st.selectbox("Housing Loan", ["yes", "no"])
    loan = st.selectbox("Personal Loan", ["yes", "no"])

    contact = st.selectbox(
        "Contact Type",
        ["cellular", "telephone", "unknown"]
    )

    month = st.selectbox(
        "Last Contact Month",
        ["jan", "feb", "mar", "apr", "may", "jun",
         "jul", "aug", "sep", "oct", "nov", "dec"]
    )

    campaign = st.number_input(
        "Number of Contacts (Current Campaign)",
        min_value=1,
        value=1
    )

    pdays = st.number_input(
        "Days Since Last Contact",
        value=-1,
        help="-1 means customer has not been contacted before"
    )

    previous = st.number_input("Number of Previous Contacts", value=0)

    poutcome = st.selectbox(
        "Previous Campaign Outcome",
        ["success", "failure", "other", "unknown"]
    )

    predict_btn = st.button("🔍 Predict Potential", use_container_width=True)

# =====================================================
# MAIN CONTENT — TABS
# =====================================================
tab1, tab2, tab3 = st.tabs(
    ["📈 Prediction Result", "📊 Business Interpretation", "ℹ️ Model Info"]
)

# =====================================================
# TAB 1 — PREDICTION RESULT
# =====================================================
with tab1:
    if predict_btn:
        input_df = pd.DataFrame([{
            "age": age,
            "job": job,
            "marital": marital,
            "education": education,
            "default": default,
            "balance": balance,
            "housing": housing,
            "loan": loan,
            "contact": contact,
            "month": month,
            "campaign": campaign,
            "pdays": pdays,
            "previous": previous,
            "poutcome": poutcome
        }])

        prob = model.predict_proba(input_df)[0][1]
        st.session_state["prob"] = prob

        kpi1, kpi2 = st.columns(2)
        kpi1.metric("📞 Campaign Contacts", campaign)
        kpi2.metric("📆 Days Since Last Contact", pdays)

        st.markdown("---")

        col1, col2 = st.columns([1.2, 1])

        with col1:
            st.markdown("### 🧾 Customer Profile")
            st.dataframe(input_df, use_container_width=True)

        with col2:
            st.markdown("### 🎯 Prediction Output")
            st.metric("Subscription Probability", f"{prob:.2%}")

            fig = go.Figure(go.Indicator(
                mode="gauge+number",
                value=prob * 100,
                number={"suffix": "%"},
                gauge={
                    "axis": {"range": [0, 100]},
                    "bar": {"color": "#1f77b4"},
                    "steps": [
                        {"range": [0, 35], "color": "#f8d7da"},
                        {"range": [35, 60], "color": "#fff3cd"},
                        {"range": [60, 100], "color": "#d4edda"}
                    ],
                },
                title={"text": "Conversion Probability"}
            ))

            st.plotly_chart(fig, use_container_width=True)

    else:
        st.info("👈 Please input customer data and click **Predict Potential**.")

# =====================================================
# TAB 2 — EXECUTIVE BUSINESS INTERPRETATION (UPGRADED)
# =====================================================
with tab2:
    if "prob" not in st.session_state:
        st.info("📌 Run prediction first to unlock executive insights.")
    else:
        prob = st.session_state["prob"]

        st.markdown("## 🧭 Executive Decision & Business Insight")

        # =====================================================
        # SEGMENTATION INTERPRETATION
        # =====================================================
        if prob >= 0.60:
            st.success("""
### 🟢 HIGH PRIORITY SEGMENT — **Revenue Acceleration Zone**

**Key Insight**
- Nasabah menunjukkan **pola historis yang sangat mirip** dengan pelanggan yang berhasil membuka deposito.
- Model memiliki tingkat keyakinan tinggi terhadap potensi konversi.

**Business Implication**
- Setiap panggilan pada segmen ini memiliki **expected value positif**.
- Risiko pemborosan biaya telemarketing **rendah**.
- Kontribusi langsung terhadap peningkatan **conversion rate dan ROI campaign**.

**Recommended Executive Action**
- Jadikan **prioritas utama** dalam campaign berjalan.
- Alokasikan **telemarketer terbaik** dan jam kontak premium.
- Cocok untuk campaign dengan **target revenue agresif**.
""")

        elif prob >= 0.35:
            st.warning("""
### 🟡 MEDIUM PRIORITY SEGMENT — **Optimization & Selective Growth Zone**

**Key Insight**
- Nasabah memiliki potensi konversi, namun sinyalnya **belum cukup kuat**.
- Outcome sangat dipengaruhi oleh **pendekatan komunikasi dan timing**.

**Business Implication**
- Risiko false positive **moderat**.
- Efektif jika digunakan untuk mengisi kapasitas idle telemarketing.
- Cocok untuk campaign **eksperimental atau retensi**.

**Recommended Executive Action**
- Hubungi secara **selektif dan terjadwal**.
- Gunakan skrip komunikasi yang lebih personal.
- Monitor performa secara ketat untuk evaluasi threshold di masa depan.
""")

        else:
            st.error("""
### 🔴 LOW PRIORITY SEGMENT — **Cost Avoidance & Risk Control Zone**

**Key Insight**
- Pola historis menunjukkan tingkat keberhasilan konversi yang rendah.
- Tidak terdapat indikator kuat bahwa kontak langsung akan efektif.

**Business Implication**
- Telemarketing pada segmen ini cenderung menghasilkan **negative ROI**.
- Risiko **over-contacting** dan penurunan customer experience meningkat.

**Recommended Executive Action**
- **Hindari telemarketing langsung**.
- Alihkan ke channel biaya rendah (email, SMS, digital nurturing).
- Simpan untuk campaign jangka panjang atau edukasi produk.
""")

        st.markdown("---")

        # =====================================================
        # DECISION THRESHOLD VISUALIZATION
        # =====================================================
        st.markdown("### 📊 Decision Threshold & Risk Visualization")

        fig = go.Figure()

        fig.add_bar(
            y=[35],
            name="Low Priority Zone",
            marker_color="#dc3545"
        )

        fig.add_bar(
            y=[25],
            base=[35],
            name="Medium Priority Zone",
            marker_color="#ffc107"
        )

        fig.add_bar(
            y=[40],
            base=[60],
            name="High Priority Zone",
            marker_color="#28a745"
        )

        fig.add_shape(
            type="line",
            x0=-0.5, x1=0.5,
            y0=prob * 100, y1=prob * 100,
            line=dict(color="black", width=3, dash="dash")
        )

        fig.add_annotation(
            x=0,
            y=prob * 100 + 2,
            text=f"Customer Probability: {prob:.2%}",
            showarrow=False,
            font=dict(size=12)
        )

        fig.update_layout(
            barmode="overlay",
            yaxis=dict(
                title="Probability (%)",
                range=[0, 100]
            ),
            xaxis=dict(showticklabels=False),
            title="Customer Position Relative to Business Decision Threshold",
            legend=dict(orientation="h", y=-0.25),
            height=420
        )

        st.plotly_chart(fig, use_container_width=True)

        st.markdown("---")

        # =====================================================
        # EXECUTIVE SUMMARY BOX
        # =====================================================
        st.info("""
### 🎯 Executive Takeaway

Aplikasi ini berfungsi sebagai **Decision Support System** untuk manajemen dengan tujuan:

- Mengidentifikasi **nasabah prioritas tinggi sebelum campaign dimulai**
- Mengoptimalkan **alokasi resource telemarketing**
- Meningkatkan **conversion rate** tanpa menaikkan biaya operasional
- Mengurangi risiko **false positive dan customer fatigue**

Model difokuskan pada **precision**, sehingga setiap panggilan yang dilakukan
memiliki probabilitas keberhasilan yang lebih tinggi.
""")

# =====================================================
# TAB 3 — MODEL INFO
# =====================================================
with tab3:
    st.markdown("""
    ### 🧠 Model Overview

    - End-to-end ML pipeline
    - One-Hot Encoding + StandardScaler
    - Logistic Regression
    - Precision-oriented optimization

    **Disclaimer**  
    This tool supports decision-making, not replaces it.
    """)

# =====================================================
# FOOTER
# =====================================================
st.markdown("---")
st.caption("📊 Final Project – Bank Marketing Prediction | Brian Naufal & Fahrezy Maulana Haz")

