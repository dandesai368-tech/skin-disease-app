import streamlit as st
from PIL import Image
import pandas as pd
import os

st.set_page_config(page_title="Skin Disease App", layout="wide")

# ---------------- CUSTOM STYLE ----------------
st.markdown("""
<style>
.big-title {
    font-size:30px;
    font-weight:bold;
    color:#4CAF50;
}
</style>
""", unsafe_allow_html=True)

menu = ["Login", "Detection", "Patient Feedback", "Analytics"]
choice = st.sidebar.selectbox("Navigation", menu)

# ---------------- LOGIN ----------------
if choice == "Login":
    st.markdown('<p class="big-title">🔐 Login Page</p>', unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        user = st.text_input("Username")
    with col2:
        pwd = st.text_input("Password", type="password")

    if st.button("Login"):
        if user == "admin" and pwd == "1234":
            st.success("Login successful ✅")
        else:
            st.error("Invalid credentials ❌")

# ---------------- DETECTION ----------------
elif choice == "Detection":
    st.markdown('<p class="big-title">🩺 Skin Disease Detection</p>', unsafe_allow_html=True)

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
    st.markdown('<p class="big-title">📝 Patient Feedback Form</p>', unsafe_allow_html=True)

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
    st.markdown('<p class="big-title">📊 Feedback Analytics</p>', unsafe_allow_html=True)

    if os.path.exists("feedback.csv"):
        df = pd.read_csv("feedback.csv")

        st.subheader("All Feedback Data")
        st.dataframe(df)

        st.subheader("⭐ Rating Distribution")
        st.bar_chart(df["Rating"].value_counts())

        st.subheader("Disease Count")
        st.bar_chart(df["Disease"].value_counts())

    else:
        st.warning("No data available yet")
