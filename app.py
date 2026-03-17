import streamlit as st
from PIL import Image
import random

# Page config
st.set_page_config(page_title="Skin Disease Detection", layout="wide")

# White Background Style
st.markdown("""
    <style>
    body {
        background-color: #ffffff;
    }
    .stApp {
        background-color: #ffffff;
    }
    </style>
""", unsafe_allow_html=True)

# Sidebar Navigation
st.sidebar.title("Navigation")
menu = ["Login", "Skin Detection", "Feedback"]
choice = st.sidebar.selectbox("Go to", menu)

# ------------------ LOGIN PAGE ------------------
if choice == "Login":

    st.markdown("<h1 style='text-align:center;'>🔐 Skin Disease Detection System</h1>", unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1,2,1])

    with col2:
        st.markdown("""
        <div style='padding:30px; border-radius:15px;
        background:white; box-shadow:0px 5px 20px rgba(0,0,0,0.1);'>
        """, unsafe_allow_html=True)

        st.subheader("👋 Welcome Back")

        username = st.text_input("👤 Username")

        show_pass = st.checkbox("Show Password")
        if show_pass:
            password = st.text_input("🔑 Password")
        else:
            password = st.text_input("🔑 Password", type="password")

        st.checkbox("Remember me")

        if st.button("Login"):
            if username == "admin" and password == "1234":
                st.success("✅ Login Successful!")
            else:
                st.error("❌ Invalid Username or Password")

        st.markdown("<p style='text-align:right; color:gray;'>Forgot Password?</p>", unsafe_allow_html=True)

        st.markdown("</div>", unsafe_allow_html=True)

# ------------------ SKIN DETECTION ------------------
elif choice == "Skin Detection":

    st.title("🩺 Skin Disease Detection")

    uploaded_file = st.file_uploader("Upload Skin Image", type=["jpg", "png", "jpeg"])

    if uploaded_file:
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image", use_column_width=True)

        # Dummy Prediction (replace with model later)
        diseases = ["Acne", "Eczema", "Psoriasis", "Melanoma"]
        prediction = random.choice(diseases)

        st.success(f"🧠 Detected Disease: {prediction}")

        # Hospital Recommendation
        if prediction == "Acne":
            hospital = "City Skin Care Clinic"
        elif prediction == "Eczema":
            hospital = "Apollo Dermatology Center"
        elif prediction == "Psoriasis":
            hospital = "Fortis Skin Hospital"
        else:
            hospital = "AIIMS Dermatology Department"

        st.info(f"🏥 Recommended Hospital: {hospital}")

# ------------------ FEEDBACK ------------------
elif choice == "Feedback":

    st.title("💬 Patient Feedback Form")

    name = st.text_input("👤 Your Name")
    rating = st.slider("⭐ Rate your experience", 1, 5)
    feedback = st.text_area("📝 Your Feedback")

    if st.button("Submit Feedback"):
        st.success("✅ Thank you for your feedback!")

        st.write("📄 Sample Feedback:")
        st.write(
            "I visited the hospital after using this system, and the experience was very good. "
            "The doctors were professional, and the treatment was effective. "
            "I am satisfied with the service provided."
        )
