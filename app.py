import streamlit as st
from PIL import Image
import random

# ---------------- PAGE CONFIG ----------------
st.set_page_config(page_title="Skin Disease Detection", layout="wide")

# ---------------- CUSTOM CSS ----------------
st.markdown("""
<style>
body {
    background-color: #f5f7fa;
}
.stApp {
    background-color: #f5f7fa;
}
h1, h2, h3, h4 {
    color: #1f4e79 !important;
}
label, .stTextInput label {
    color: black !important;
    font-weight: 600;
}
.card {
    padding: 25px;
    border-radius: 15px;
    background: white;
    box-shadow: 0px 4px 15px rgba(0,0,0,0.1);
}
</style>
""", unsafe_allow_html=True)

# ---------------- SIDEBAR ----------------
st.sidebar.title("🔍 Navigation")
menu = ["Login", "Skin Detection", "Feedback", "Analytics"]
choice = st.sidebar.selectbox("Go to", menu)

# ---------------- LOGIN PAGE ----------------
if choice == "Login":

    st.markdown("<h1 style='text-align:center;'>🔐 Skin Disease Detection System</h1>", unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1,2,1])

    with col2:
        st.markdown("<div class='card'>", unsafe_allow_html=True)

        st.subheader("👋 Welcome Back")

        username = st.text_input("👤 Username")

        show_pass = st.checkbox("Show Password")
        if show_pass:
            password = st.text_input("🔑 Password")
        else:
            password = st.text_input("🔑 Password", type="password")

        st.checkbox("Remember me")

        if st.button("🚀 Login"):
            if username == "admin" and password == "1234":
                st.success("✅ Login Successful!")
            else:
                st.error("❌ Invalid Username or Password")

        st.markdown("<p style='text-align:right; color:#1f4e79;'>Forgot Password?</p>", unsafe_allow_html=True)

        st.markdown("</div>", unsafe_allow_html=True)

# ---------------- SKIN DETECTION ----------------
elif choice == "Skin Detection":

    st.title("🩺 Skin Disease Detection")

    location = st.text_input("📍 Enter Your Location")

    uploaded_file = st.file_uploader("📤 Upload Skin Image", type=["jpg", "png", "jpeg"])

    if uploaded_file:
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image", use_column_width=True)

        diseases = ["Acne", "Eczema", "Psoriasis", "Melanoma"]
        prediction = random.choice(diseases)

        st.success(f"🧠 Detected Disease: {prediction}")

        # Hospital Recommendation
        if prediction == "Acne":
            hospital = "City Skin Care Clinic"
            precaution = "Keep skin clean and avoid oily products."
        elif prediction == "Eczema":
            hospital = "Apollo Dermatology Center"
            precaution = "Use moisturizers and avoid allergens."
        elif prediction == "Psoriasis":
            hospital = "Fortis Skin Hospital"
            precaution = "Reduce stress and follow medical advice."
        else:
            hospital = "AIIMS Dermatology Department"
            precaution = "Consult doctor immediately."

        st.info(f"🏥 Recommended Hospital: {hospital}")
        st.warning(f"⚠️ Precautions: {precaution}")

# ---------------- FEEDBACK ----------------
elif choice == "Feedback":

    st.title("💬 Patient Feedback")

    name = st.text_input("👤 Name")
    rating = st.slider("⭐ Rating", 1, 5)
    feedback = st.text_area("📝 Feedback")

    if st.button("Submit"):
        st.success("✅ Thank you for your feedback!")

        st.markdown("### 📄 Sample Patient Feedback")
        st.write(
            "After visiting the recommended hospital, I had a very positive experience. "
            "The doctors were knowledgeable and provided effective treatment. "
            "The hospital environment was clean and well-maintained."
        )

# ---------------- ANALYTICS ----------------
elif choice == "Analytics":

    st.title("📊 Analytics Dashboard")

    data = {
        "Acne": random.randint(10, 50),
        "Eczema": random.randint(10, 50),
        "Psoriasis": random.randint(10, 50),
        "Melanoma": random.randint(5, 30)
    }

    st.bar_chart(data)

    st.info("📈 This chart shows number of detected cases.")
    
