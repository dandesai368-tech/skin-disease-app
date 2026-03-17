import streamlit as st
from PIL import Image
import pandas as pd
import os
import matplotlib.pyplot as plt

# -------- PAGE CONFIG --------
st.set_page_config(page_title="Skin Disease App", layout="wide")

# -------- BEAUTIFUL LIGHT UI --------
st.markdown("""
<style>

/* BACKGROUND */
.stApp {
    background: linear-gradient(to right, #e3f2fd, #ffffff);
}

/* HEADINGS */
h1, h2, h3 {
    color: #1a237e !important;
    font-weight: bold;
}

/* LABELS */
label {
    color: #000000 !important;
    font-weight: bold;
}

/* INPUT BOX */
input {
    background-color: #ffffff !important;
    color: #000000 !important;
    border: 1px solid #ccc !important;
    border-radius: 8px !important;
}

/* REMOVE DARK FIELDS */
div[data-baseweb="input"] {
    background-color: white !important;
}

/* BUTTON */
button {
    background-color: #1976d2 !important;
    color: white !important;
    border-radius: 8px !important;
}

/* LOGIN CARD */
.login-box {
    width: 400px;
    margin: 80px auto;
    padding: 30px;
    background: #ffffff;
    border-radius: 15px;
    box-shadow: 0px 5px 20px rgba(0,0,0,0.1);
    text-align: center;
}

/* TITLE */
.title {
    text-align: center;
    font-size: 34px;
    font-weight: bold;
    color: #0d47a1;
}

</style>
""", unsafe_allow_html=True)

# -------- SIDEBAR --------
menu = ["Login", "Detection", "Patient Feedback", "Analytics"]
choice = st.sidebar.selectbox("Navigation", menu)

# -------- LOGIN --------
if choice == "Login":
    st.markdown('<p class="title">🔐 Skin Disease Detection System</p>', unsafe_allow_html=True)

    st.markdown('<div class="login-box">', unsafe_allow_html=True)

    username = st.text_input("👤 Username")
    password = st.text_input("🔑 Password", type="password")

    if st.button("Login"):
        if username == "admin" and password == "1234":
            st.success("✅ Login Successful!")
        else:
            st.error("❌ Invalid Username or Password")

    st.markdown('</div>', unsafe_allow_html=True)

# -------- DETECTION --------
elif choice == "Detection":
    st.markdown("<h1>🩺 Skin Disease Detection</h1>", unsafe_allow_html=True)

    file = st.file_uploader("📤 Upload Skin Image", type=["jpg","png","jpeg"])

    if file:
        img = Image.open(file)

        col1, col2 = st.columns(2)

        with col1:
            st.image(img, caption="Uploaded Image", use_column_width=True)

        with col2:
            st.success("Detected Disease: Acne")

            st.subheader("🏥 Recommended Hospitals")
            st.write("• Apollo Hospital")
            st.write("• AIIMS")
            st.write("• Fortis Hospital")

# -------- FEEDBACK --------
elif choice == "Patient Feedback":
    st.markdown("<h1>📝 Patient Feedback Form</h1>", unsafe_allow_html=True)

    name = st.text_input("Patient Name")
    age = st.number_input("Age", 1, 100)
    gender = st.selectbox("Gender", ["Male", "Female", "Other"])
    disease = st.selectbox("Disease", ["Acne", "Eczema", "Psoriasis"])
    rating = st.slider("⭐ Rating", 1, 5)
    comments = st.text_area("Comments")

    if st.button("Submit Feedback"):
        if name and comments:
            data = {
                "Name": name,
                "Age": age,
                "Gender": gender,
                "Disease": disease,
                "Rating": rating,
                "Comments": comments
            }

            df = pd.DataFrame([data])

            if os.path.exists("feedback.csv"):
                df.to_csv("feedback.csv", mode='a', header=False, index=False)
            else:
                df.to_csv("feedback.csv", index=False)

            st.success("✅ Feedback Submitted Successfully!")
        else:
            st.warning("⚠️ Please fill all fields")

# -------- ANALYTICS --------
elif choice == "Analytics":
    st.markdown("<h1>📊 Feedback Analytics</h1>", unsafe_allow_html=True)

    if os.path.exists("feedback.csv"):
        df = pd.read_csv("feedback.csv")

        st.subheader("📋 All Data")
        st.dataframe(df)

        st.subheader("⭐ Rating Distribution")
        st.bar_chart(df["Rating"].value_counts())

        st.subheader("🦠 Disease Count")
        st.bar_chart(df["Disease"].value_counts())

        st.subheader("📊 Rating Pie Chart")
        fig, ax = plt.subplots()
        df["Rating"].value_counts().plot.pie(autopct='%1.1f%%', ax=ax)
        ax.set_ylabel("")
        st.pyplot(fig)

        st.download_button("📥 Download CSV", df.to_csv(index=False), "feedback.csv")

    else:
        st.warning("No data available")
