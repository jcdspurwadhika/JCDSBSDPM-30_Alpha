# bank-term-deposit-StreamlitApp
# 📊 Bank Marketing Campaign Analysis & Prediction

## Project Overview
Project ini bertujuan untuk menganalisis dan memprediksi **probabilitas nasabah berlangganan deposito berjangka (term deposit)** berdasarkan data hasil kampanye telemarketing bank.  
Analisis dilakukan menggunakan pendekatan **Exploratory Data Analysis (EDA)** dan **Machine Learning (Logistic Regression)** untuk mendukung pengambilan keputusan bisnis yang lebih efektif.

Dataset yang digunakan merupakan data historis kampanye pemasaran bank, yang banyak digunakan sebagai studi kasus di bidang data science dan analytics.

---

## Objectives
- Memahami karakteristik nasabah yang berpengaruh terhadap keputusan berlangganan deposito
- Mengidentifikasi faktor paling penting dalam keberhasilan kampanye telemarketing
- Membangun model prediksi probabilitas subscription
- Memberikan **insight bisnis** untuk optimalisasi strategi telemarketing

---

## Live Applications & Dashboards

### Streamlit Prediction App
Aplikasi interaktif untuk memprediksi probabilitas nasabah berlangganan deposito berdasarkan input karakteristik nasabah.

**Streamlit App**:  
https://bank-term-deposit-appapp-yjgtwqybxc9cwokvtqhqvr.streamlit.app/

---

### Tableau Executive Dashboard
Dashboard visualisasi untuk analisis performa kampanye dan distribusi nasabah secara strategis.

**Tableau Dashboard**:  
https://public.tableau.com/app/profile/fahrezy.maulana.haz/viz/Finpro2Dashboardd/Dashboard1?publish=yes

---

## Dataset Information
- **Source**: Bank Marketing Dataset
- **Target Variable**:
  - `y`  
    - `1` = Nasabah berlangganan deposito  
    - `0` = Nasabah tidak berlangganan deposito

### Contoh Fitur yang Digunakan:
- Demografi: `age`, `job`, `education`, `marital`
- Finansial: `balance`, `housing`, `loan`, `default`
- Campaign: `contact`, `month`, `campaign`, `pdays`, `previous`, `poutcome`

**Catatan penting**:  
Fitur `duration` sengaja **tidak digunakan** karena merupakan **data leakage** (informasi hanya diketahui setelah panggilan selesai).

---

## Exploratory Data Analysis (EDA)
Tahapan EDA meliputi:
- Analisis distribusi target (conversion rate)
- Analisis fitur demografis dan finansial terhadap target
- Analisis performa campaign berdasarkan waktu dan kanal kontak
- Visualisasi hubungan fitur terhadap probabilitas subscription

EDA difokuskan pada **insight bisnis**, bukan hanya statistik deskriptif.

---

## Data Preprocessing
Tahapan preprocessing yang dilakukan:
- Encoding fitur kategorikal menggunakan **One-Hot Encoding**
- Scaling fitur numerik
- Pemisahan data train dan test
- Pipeline preprocessing untuk menjaga konsistensi data

---

## Modeling
- Model: **Logistic Regression**
- Alasan pemilihan:
  - Interpretatif
  - Cocok untuk binary classification
  - Mendukung analisis feature importance berbasis koefisien

---

## Model Evaluation
Evaluasi model dilakukan menggunakan:
- Confusion Matrix
- Classification Report
- Probability-based interpretation (bukan hanya accuracy)

Model difokuskan untuk mendukung **prioritisasi nasabah**, bukan sekadar prediksi benar/salah.

---

## Feature Importance
Feature importance dianalisis menggunakan **koefisien Logistic Regression** setelah preprocessing.

Temuan utama:
- Riwayat campaign sebelumnya (`poutcome`) memiliki pengaruh paling kuat
- Waktu dan kanal kontak berpengaruh signifikan
- Faktor demografis berpengaruh, namun relatif lebih kecil dibanding faktor interaksi historis

Interpretasi dilakukan pada **fitur hasil transformasi**, bukan fitur mentah.

---

## Business Insights
- Nasabah dengan riwayat keberhasilan campaign sebelumnya memiliki probabilitas konversi paling tinggi
- Strategi telemarketing sebaiknya memprioritaskan:
  - Nasabah dengan histori positif
  - Timing campaign yang tepat
  - Kanal komunikasi yang efektif
- Pendekatan berbasis data dapat:
  - Mengurangi biaya kampanye
  - Meningkatkan conversion rate
  - Mengoptimalkan resource telemarketing

---

## Key Takeaways
- Tidak semua fitur demografis memiliki pengaruh besar terhadap keputusan nasabah
- Faktor interaksi dan histori kampanye jauh lebih menentukan
- Model mendukung pengambilan keputusan bisnis yang **lebih presisi dan efisien**

---

## Tools & Libraries
- Python
- Pandas, NumPy
- Matplotlib, Seaborn
- Scikit-learn
- Streamlit
- Tableau
- Jupyter Notebook / VS Code

---
## Project Structure
bank-term-deposit-analysis/
│
├── data/
│   └── bank-full.csv
│      # Dataset asli Bank Marketing
│
├── notebook/
│   └── FinalProject.ipynb
│      # Exploratory Data Analysis (EDA),
│      # Feature Engineering,
│      # Model Training & Evaluation
│
├── app/
│   ├── app.py
│   │   # Streamlit application for prediction
│   │
│   └── pipeline.pkl
│       # Trained machine learning pipeline
│
├── README.md
│   # Project documentation
│
└── requirements.txt
    # Python dependencies


---

## Author
**Brian Naufal & Fahrezy Maulana Haz**  
Data Analysis & Machine Learning Project

---



## 📁 Project Structure
