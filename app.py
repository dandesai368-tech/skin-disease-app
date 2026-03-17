import streamlit as st
from PIL import Image
import pandas as pd
import os
import matplotlib.pyplot as plt

st.set_page_config(page_title="Skin Disease App", layout="wide")

# ---------------- CUSTOM CSS ----------------
st.markdown("""
<style>
body {
    background: linear-gradient(to right, #e3f2fd, #ffffff);
}

.login-box {
    width: 350px;
    margin: auto;
    padding: 30px;
    background: white;
    border-radius: 15px;
    box-shadow: 0px 0px 15px rgba(0,0,0,0.2);
    text-align: center;
}

.title {
    text-align: center;
    font-size: 32px;
    font-weight: bold;
    color: #2c3e50;
}

</style>
""", unsafe_allow_html=True)

# Sidebar
menu = ["Login", "Detection", "Patient Feedback", "Analytics"]
choice = st.sidebar.selectbox("Navigation", menu)

# ---------------- LOGIN ----------------
if choice == "Login":
    st.markdown('<p class="title">🔐 Skin Disease Detection System</p>', unsafe_allow_html=True)

    st.markdown('<div class="login-box">', unsafe_allow_html=True)

    username = st.text_input("👤 Username")
    password = st.text_input("🔑 Password", type="password")

    if st.button("Login"):
        if username == "admin" and password == "1234":
            st.success("✅ Login successful!")
        else:
            st.error("❌ Invalid credentials")

    st.markdown('</div>', unsafe_allow_html=True)

# ---------------- DETECTION ----------------
elif choice == "Detection":
    st.title("🩺 Skin Disease Detection")

    def predict():
        return "Acne"

    file = st.file_uploader("Upload Skin Image", type=["jpg","png","jpeg"])

    if file:
        img = Image.open(file)

        col1, col2 = st.columns(2)
        with col1:
            st.image(img, caption="Uploaded Image")

        with col2:
            st.success("Detected Disease: " + predict())

            st.subheader("🏥 Recommended Hospitals")
            st.write("• Apollo Hospital")
            st.write("• AIIMS")
            st.write("• Fortis Hospital")

# ---------------- PATIENT FEEDBACK ----------------
elif choice == "Patient Feedback":
    st.title("📝 Patient Feedback Form")

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
            file_path = "feedback.csv"

            if os.path.exists(file_path):
                df.to_csv(file_path, mode='a', header=False, index=False)
            else:
                df.to_csv(file_path, index=False)

            st.success("✅ Feedback saved!")

        else:
            st.warning("⚠️ Fill all fields")

# ---------------- ANALYTICS ----------------
elif choice == "Analytics":
    st.title("📊 Feedback Analytics")

    if os.path.exists("feedback.csv"):
        df = pd.read_csv("feedback.csv")

        st.subheader("📋 All Feedback Data")
        st.dataframe(df)

        # Search
        st.subheader("🔍 Search Patient")
        search = st.text_input("Enter name")

        if search:
            result = df[df["Name"].str.contains(search, case=False)]
            if not result.empty:
                st.dataframe(result)
            else:
                st.warning("No result found")

        # Charts
        st.subheader("⭐ Rating Distribution")
        st.bar_chart(df["Rating"].value_counts())

        st.subheader("Disease Count")
        st.bar_chart(df["Disease"].value_counts())

        # Pie Chart
        st.subheader("📊 Rating Pie Chart")
        fig, ax = plt.subplots()
        df["Rating"].value_counts().plot.pie(autopct='%1.1f%%', ax=ax)
        ax.set_ylabel("")
        st.pyplot(fig)

        # Download
        st.download_button(
            "📥 Download Data",
            df.to_csv(index=False),
            "feedback.csv"
        )

        # Report
        st.subheader("🧾 Report")

        if st.button("Generate Report"):
            st.write("Total Patients:", len(df))
            st.write("Average Rating:", round(df["Rating"].mean(), 2))
            st.write("Most Common Disease:", df["Disease"].value_counts().idxmax())

    else:
        st.warning("No data available")
