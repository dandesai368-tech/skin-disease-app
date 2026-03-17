import streamlit as st
from PIL import Image
import pandas as pd
import os
import matplotlib.pyplot as plt

st.set_page_config(page_title="Skin Disease App", layout="wide")

# Sidebar Menu
menu = ["Login", "Detection", "Patient Feedback", "Analytics"]
choice = st.sidebar.selectbox("Navigation", menu)

# ---------------- LOGIN ----------------
if choice == "Login":
    st.title("🔐 Login Page")

    user = st.text_input("Username")
    pwd = st.text_input("Password", type="password")

    if st.button("Login"):
        if user == "admin" and pwd == "1234":
            st.success("Login successful ✅")
        else:
            st.error("Invalid credentials ❌")

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

        # 🔍 Search
        st.subheader("🔍 Search Patient")
        search_name = st.text_input("Enter patient name")

        if search_name:
            result = df[df["Name"].str.contains(search_name, case=False)]
            if not result.empty:
                st.dataframe(result)
            else:
                st.warning("No patient found")

        # 📊 Bar Charts
        st.subheader("⭐ Rating Distribution")
        st.bar_chart(df["Rating"].value_counts())

        st.subheader("Disease Count")
        st.bar_chart(df["Disease"].value_counts())

        # 🥧 Pie Chart
        st.subheader("📊 Rating Pie Chart")
        fig, ax = plt.subplots()
        df["Rating"].value_counts().plot.pie(autopct='%1.1f%%', ax=ax)
        ax.set_ylabel("")
        st.pyplot(fig)

        # 📥 Download
        st.download_button(
            label="📥 Download Feedback Data",
            data=df.to_csv(index=False),
            file_name="patient_feedback.csv",
            mime="text/csv"
        )

        # 🧾 Report
        st.subheader("🧾 Generate Report")

        if st.button("Generate Summary Report"):
            total = len(df)
            avg_rating = round(df["Rating"].mean(), 2)

            st.write("### 📌 Report Summary")
            st.write(f"Total Patients: {total}")
            st.write(f"Average Rating: {avg_rating}")
            st.write("Most Common Disease:")
            st.write(df["Disease"].value_counts().idxmax())

    else:
        st.warning("No feedback data available yet")
