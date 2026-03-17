import streamlit as st
from PIL import Image
import random
import pandas as pd

# ---------------- PAGE CONFIG ----------------
st.set_page_config(page_title="Skin Disease Detection", layout="wide")

# ---------------- CSS ----------------
st.markdown("""
<style>
.stApp {
    background: linear-gradient(to right, #eef2f7, #ffffff);
}

h1 {
    color: #0b3c5d !important;
    font-size: 42px !important;
}
h2 {
    color: #1f4e79 !important;
}

label {
    color: black !important;
    font-weight: 600;
}

.card {
    padding: 30px;
    border-radius: 20px;
    background: white;
    box-shadow: 0px 8px 25px rgba(0,0,0,0.15);
}

.stButton>button {
    background-color: #1f77b4;
    color: white;
    border-radius: 10px;
}
</style>
""", unsafe_allow_html=True)

# ---------------- SIDEBAR ----------------
st.sidebar.title("🔍 Navigation")
menu = ["Login", "Skin Detection", "Feedback", "Analytics"]
choice = st.sidebar.selectbox("Go to", menu)

# ---------------- LOGIN ----------------
if choice == "Login":

    st.markdown("<h1 style='text-align:center;'>🩺 Skin Disease Detection System</h1>", unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1,2,1])

    with col2:
        st.markdown("<div class='card'>", unsafe_allow_html=True)

        st.markdown("<h2 style='text-align:center;'>👋 Welcome Back</h2>", unsafe_allow_html=True)

        username = st.text_input("👤 Username")

        show_pass = st.checkbox("Show Password")
        password = st.text_input("🔑 Password", type="default" if show_pass else "password")

        st.checkbox("Remember me")

        if st.button("🚀 Login"):
            if username == "admin" and password == "1234":
                st.success("✅ Login Successful!")
            else:
                st.error("❌ Invalid Username")

        st.markdown("<p style='text-align:right; color:#1f4e79;'>Forgot Password?</p>", unsafe_allow_html=True)

        st.markdown("</div>", unsafe_allow_html=True)

# ---------------- SKIN DETECTION ----------------
elif choice == "Skin Detection":

    st.markdown("<h1>🩺 Skin Disease Detection</h1>", unsafe_allow_html=True)

    location = st.text_input("📍 Enter Your Location (lat, lon)", "17.3850, 78.4867")

    uploaded_file = st.file_uploader("📤 Upload Skin Image", type=["jpg", "png", "jpeg"])

    if uploaded_file:
        image = Image.open(uploaded_file)

        # Smaller Image
        st.image(image, width=300)

        diseases = ["Acne", "Eczema", "Psoriasis", "Melanoma"]
        prediction = random.choice(diseases)

        st.success(f"🧠 Detected Disease: {prediction}")

        # Hospital + Precautions
        if prediction == "Acne":
            hospital = "City Skin Care Clinic"
            precaution = "Wash face and avoid oily products."
        elif prediction == "Eczema":
            hospital = "Apollo Dermatology Center"
            precaution = "Use moisturizer and avoid allergens."
        elif prediction == "Psoriasis":
            hospital = "Fortis Skin Hospital"
            precaution = "Reduce stress and follow treatment."
        else:
            hospital = "AIIMS Dermatology Department"
            precaution = "Consult doctor immediately."

        st.info(f"🏥 Recommended Hospital: {hospital}")
        st.warning(f"⚠️ Precautions: {precaution}")

        # MAP
        try:
            lat, lon = map(float, location.split(","))
            map_data = pd.DataFrame({"lat":[lat], "lon":[lon]})
            st.map(map_data)
        except:
            st.error("Enter location like: 17.3850, 78.4867")

# ---------------- FEEDBACK ----------------
elif choice == "Feedback":

    st.markdown("<h1>💬 Patient Feedback</h1>", unsafe_allow_html=True)

    name = st.text_input("👤 Name")
    rating = st.slider("⭐ Rating", 1, 5)
    feedback = st.text_area("📝 Feedback")

    if st.button("Submit Feedback"):

        # Save feedback
        df = pd.DataFrame([[name, rating, feedback]],
                          columns=["Name","Rating","Feedback"])
        df.to_csv("feedback.csv", mode="a", header=False, index=False)

        st.success("✅ Feedback saved!")

        st.write(
            "I visited the recommended hospital and received excellent care. "
            "Doctors were professional and treatment was effective."
        )

# ---------------- ANALYTICS ----------------
elif choice == "Analytics":

    st.markdown("<h1>📊 Analytics Dashboard</h1>", unsafe_allow_html=True)

    # Disease Data
    data = {
        "Acne": random.randint(10, 50),
        "Eczema": random.randint(10, 50),
        "Psoriasis": random.randint(10, 50),
        "Melanoma": random.randint(5, 30)
    }

    st.subheader("🧠 Disease Cases")
    st.bar_chart(data)

    # Feedback Data
    try:
        df = pd.read_csv("feedback.csv")
        st.subheader("⭐ User Ratings")
        st.bar_chart(df["Rating"].value_counts())
    except:
        st.info("No feedback data yet.")
