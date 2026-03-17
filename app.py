import streamlit as st
from PIL import Image
import random
import pandas as pd

# ---------------- PAGE CONFIG ----------------
st.set_page_config(page_title="Skin Disease Detection", layout="wide")

# ---------------- PREMIUM CSS ----------------
st.markdown("""
<style>

/* Background with image */
.stApp {
    background: url("https://images.unsplash.com/photo-1588776814546-1ffcf47267a5") no-repeat center center fixed;
    background-size: cover;
}

/* Glass effect card */
.glass {
    backdrop-filter: blur(15px);
    background: rgba(255,255,255,0.85);
    padding: 40px;
    border-radius: 20px;
    box-shadow: 0px 10px 30px rgba(0,0,0,0.2);
    animation: fadeIn 1s ease-in-out;
}

/* Animation */
@keyframes fadeIn {
    from {opacity:0; transform:translateY(20px);}
    to {opacity:1; transform:translateY(0);}
}

/* Headings */
h1 {
    text-align:center;
    color:white !important;
    font-size:50px !important;
    font-weight:bold;
}

h2 {
    color:#4a148c !important;
    font-size:30px !important;
}

/* Labels */
label {
    color:black !important;
    font-size:16px !important;
}

/* Buttons */
.stButton>button {
    background: linear-gradient(to right, #7b1fa2, #512da8);
    color:white;
    border-radius:10px;
    font-size:18px;
    padding:10px;
    width:100%;
}

/* Navigation buttons */
.nav button {
    background-color:#ffffff;
    color:black;
    border-radius:8px;
    padding:8px;
    font-weight:600;
}

</style>
""", unsafe_allow_html=True)

# ---------------- NAVIGATION ----------------
st.markdown("<h1>🩺 Skin Disease Detection</h1>", unsafe_allow_html=True)

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

# ---------------- LOGIN PAGE ----------------
if page == "Login":

    col1, col2, col3 = st.columns([1,2,1])

    with col2:
        st.markdown("<div class='glass'>", unsafe_allow_html=True)

        st.markdown("<h2>Welcome back</h2>", unsafe_allow_html=True)

        email = st.text_input("📧 Enter your email")

        show_pass = st.checkbox("Show Password")
        password = st.text_input("🔑 Password", type="default" if show_pass else "password")

        st.checkbox("Remember for 30 days")

        if st.button("Sign In"):
            if email == "admin@gmail.com" and password == "1234":
                st.success("✅ Login Successful!")
            else:
                st.error("❌ Invalid credentials")

        st.markdown("<p style='text-align:right;color:#7b1fa2;'>Forgot password?</p>", unsafe_allow_html=True)

        st.markdown("</div>", unsafe_allow_html=True)

# ---------------- DETECTION ----------------
elif page == "Detection":

    st.markdown("<h2>🩺 Skin Disease Detection</h2>", unsafe_allow_html=True)

    location = st.text_input("📍 Enter Location (lat, lon)", "17.3850, 78.4867")

    uploaded_file = st.file_uploader("📤 Upload Image", type=["jpg","png","jpeg"])

    if uploaded_file:
        image = Image.open(uploaded_file)
        st.image(image, width=250)

        diseases = ["Acne", "Eczema", "Psoriasis", "Melanoma"]
        prediction = random.choice(diseases)

        st.success(f"🧠 Detected: {prediction}")

        if prediction == "Acne":
            hospital = "City Skin Care Clinic"
            precaution = "Avoid oily skin products."
        elif prediction == "Eczema":
            hospital = "Apollo Dermatology Center"
            precaution = "Use moisturizer."
        elif prediction == "Psoriasis":
            hospital = "Fortis Skin Hospital"
            precaution = "Reduce stress."
        else:
            hospital = "AIIMS Dermatology Department"
            precaution = "Consult doctor immediately."

        st.info(f"🏥 Hospital: {hospital}")
        st.warning(f"⚠️ Precautions: {precaution}")

        try:
            lat, lon = map(float, location.split(","))
            map_data = pd.DataFrame({"lat":[lat], "lon":[lon]})
            st.map(map_data)
        except:
            st.error("Enter correct format")

# ---------------- FEEDBACK ----------------
elif page == "Feedback":

    st.markdown("<h2>💬 Patient Feedback</h2>", unsafe_allow_html=True)

    name = st.text_input("👤 Name")
    rating = st.slider("⭐ Rating", 1, 5)
    feedback = st.text_area("📝 Feedback")

    if st.button("Submit"):
        df = pd.DataFrame([[name, rating, feedback]],
                          columns=["Name","Rating","Feedback"])
        df.to_csv("feedback.csv", mode="a", header=False, index=False)

        st.success("✅ Feedback saved!")

# ---------------- ANALYTICS ----------------
elif page == "Analytics":

    st.markdown("<h2>📊 Analytics</h2>", unsafe_allow_html=True)

    data = {
        "Acne": random.randint(10,50),
        "Eczema": random.randint(10,50),
        "Psoriasis": random.randint(10,50),
        "Melanoma": random.randint(5,30)
    }

    st.bar_chart(data)

    try:
        df = pd.read_csv("feedback.csv")
        st.bar_chart(df["Rating"].value_counts())
    except:
        st.info("No data yet.")
