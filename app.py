import streamlit as st
from PIL import Image
import random
import pandas as pd

# ---------------- PAGE CONFIG ----------------
st.set_page_config(page_title="Skin Disease Detection", layout="wide")

# ---------------- CUSTOM CSS ----------------
st.markdown("""
<style>

/* Background */
.stApp {
    background: linear-gradient(to right, #e3f2fd, #ffffff);
}

/* Headings */
h1 {
    color: #0b3c5d !important;
    font-size: 48px !important;
    text-align: center;
}
h2 {
    color: #1565c0 !important;
    font-size: 32px !important;
}
h3 {
    color: #1976d2 !important;
    font-size: 24px !important;
}

/* Text */
label, p {
    font-size: 18px !important;
    color: black !important;
}

/* Card */
.card {
    padding: 35px;
    border-radius: 20px;
    background: white;
    box-shadow: 0px 10px 30px rgba(0,0,0,0.15);
}

/* Buttons */
.stButton>button {
    background-color: #1976d2;
    color: white;
    font-size: 18px;
    border-radius: 10px;
    padding: 10px 20px;
}

/* Navigation buttons */
.nav-btn {
    text-align:center;
    margin-bottom:20px;
}
</style>
""", unsafe_allow_html=True)

# ---------------- NAVIGATION (TOP MENU) ----------------
st.markdown("<h1>🩺 Skin Disease Detection System</h1>", unsafe_allow_html=True)

col1, col2, col3, col4 = st.columns(4)

if "page" not in st.session_state:
    st.session_state.page = "Login"

if col1.button("🔐 Login"):
    st.session_state.page = "Login"
if col2.button("🩺 Detection"):
    st.session_state.page = "Detection"
if col3.button("💬 Feedback"):
    st.session_state.page = "Feedback"
if col4.button("📊 Analytics"):
    st.session_state.page = "Analytics"

page = st.session_state.page

# ---------------- LOGIN ----------------
if page == "Login":

    col1, col2, col3 = st.columns([1,2,1])

    with col2:
        st.markdown("<div class='card'>", unsafe_allow_html=True)

        st.markdown("<h2>👋 Welcome Back</h2>", unsafe_allow_html=True)

        username = st.text_input("👤 Username")

        show_pass = st.checkbox("Show Password")
        password = st.text_input("🔑 Password", type="default" if show_pass else "password")

        st.checkbox("Remember me")

        if st.button("🚀 Login"):
            if username == "admin" and password == "1234":
                st.success("✅ Login Successful! Go to Detection page")
            else:
                st.error("❌ Invalid Username or Password")

        st.markdown("<p style='text-align:right;color:#1565c0;'>Forgot Password?</p>", unsafe_allow_html=True)

        st.markdown("</div>", unsafe_allow_html=True)

# ---------------- DETECTION ----------------
elif page == "Detection":

    st.markdown("<h2>🩺 Skin Disease Detection</h2>", unsafe_allow_html=True)

    location = st.text_input("📍 Enter Location (lat, lon)", "17.3850, 78.4867")

    uploaded_file = st.file_uploader("📤 Upload Skin Image", type=["jpg","png","jpeg"])

    if uploaded_file:
        image = Image.open(uploaded_file)

        st.image(image, width=250)

        diseases = ["Acne", "Eczema", "Psoriasis", "Melanoma"]
        prediction = random.choice(diseases)

        st.success(f"🧠 Detected Disease: {prediction}")

        if prediction == "Acne":
            hospital = "City Skin Care Clinic"
            precaution = "Wash face and avoid oily creams."
        elif prediction == "Eczema":
            hospital = "Apollo Dermatology Center"
            precaution = "Use moisturizer regularly."
        elif prediction == "Psoriasis":
            hospital = "Fortis Skin Hospital"
            precaution = "Reduce stress and follow treatment."
        else:
            hospital = "AIIMS Dermatology Department"
            precaution = "Consult doctor immediately."

        st.info(f"🏥 Hospital: {hospital}")
        st.warning(f"⚠️ Precautions: {precaution}")

        # Map
        try:
            lat, lon = map(float, location.split(","))
            map_data = pd.DataFrame({"lat":[lat], "lon":[lon]})
            st.map(map_data)
        except:
            st.error("Enter correct format: 17.3850, 78.4867")

# ---------------- FEEDBACK ----------------
elif page == "Feedback":

    st.markdown("<h2>💬 Patient Feedback</h2>", unsafe_allow_html=True)

    name = st.text_input("👤 Name")
    rating = st.slider("⭐ Rating", 1, 5)
    feedback = st.text_area("📝 Feedback")

    if st.button("Submit Feedback"):
        df = pd.DataFrame([[name, rating, feedback]],
                          columns=["Name","Rating","Feedback"])
        df.to_csv("feedback.csv", mode="a", header=False, index=False)

        st.success("✅ Feedback Saved!")

        st.write(
            "I visited the hospital and received excellent care. "
            "Doctors were professional and treatment was effective."
        )

# ---------------- ANALYTICS ----------------
elif page == "Analytics":

    st.markdown("<h2>📊 Analytics Dashboard</h2>", unsafe_allow_html=True)

    data = {
        "Acne": random.randint(10,50),
        "Eczema": random.randint(10,50),
        "Psoriasis": random.randint(10,50),
        "Melanoma": random.randint(5,30)
    }

    st.subheader("🧠 Disease Cases")
    st.bar_chart(data)

    try:
        df = pd.read_csv("feedback.csv")
        st.subheader("⭐ Ratings")
        st.bar_chart(df["Rating"].value_counts())
    except:
        st.info("No feedback yet.")
