import streamlit as st
from PIL import Image
import random
import pandas as pd

# ---------------- PAGE CONFIG ----------------
st.set_page_config(page_title="Skin Disease Detection", layout="wide")

# ---------------- CSS ----------------
st.markdown("""
<style>

/* Background */
.stApp {
    background: linear-gradient(135deg, #dbeafe, #f8fafc);
}

/* Main Title */
.main-title {
    text-align: center;
    font-size: 50px;
    font-weight: 800;
    color: #0f172a;
}

/* Login Heading */
.login-title {
    font-size: 36px;
    font-weight: 700;
    color: #111827;
    text-align:center;
}

/* Subtitle */
.login-sub {
    font-size: 18px;
    color: #374151;
    text-align:center;
    margin-bottom: 20px;
}

/* Card */
.card {
    background: white;
    padding: 40px;
    border-radius: 20px;
    box-shadow: 0px 10px 30px rgba(0,0,0,0.15);
    animation: fadeIn 0.8s ease-in-out;
}

/* Inputs */
.stTextInput input {
    border-radius: 10px;
    padding: 10px;
}

/* Buttons */
.stButton>button {
    background: linear-gradient(to right, #6366f1, #8b5cf6);
    color: white;
    font-size: 18px;
    border-radius: 10px;
}

/* Animation */
@keyframes fadeIn {
    from {opacity: 0; transform: translateY(20px);}
    to {opacity: 1; transform: translateY(0);}
}

/* Section headings */
.section-title {
    font-size: 32px;
    font-weight: 700;
    color: #1e3a8a;
    margin-top: 20px;
}

</style>
""", unsafe_allow_html=True)

# ---------------- NAVIGATION ----------------
st.markdown("<div class='main-title'>🩺 Skin Disease Detection System</div>", unsafe_allow_html=True)

col1, col2, col3, col4 = st.columns(4)

if "page" not in st.session_state:
    st.session_state.page = "Login"

if col1.button("🔐 Login"):
    st.session_state.page = "Login"
if col2.button("🧪 Detection"):
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

        st.image("https://cdn-icons-png.flaticon.com/512/2966/2966488.png", width=70)

        st.markdown("<div class='login-title'>Welcome back 👋</div>", unsafe_allow_html=True)
        st.markdown("<div class='login-sub'>Please enter your details</div>", unsafe_allow_html=True)

        username = st.text_input("", placeholder="Enter your username")

        show = st.checkbox("Show Password")
        password = st.text_input("", type="default" if show else "password", placeholder="Enter password")

        st.checkbox("Remember for 30 days")

        if st.button("Sign In"):
            if username == "admin" and password == "1234":
                st.success("✅ Login Successful! Go to Detection")
            else:
                st.error("❌ Invalid Credentials")

        st.markdown("<p style='text-align:right;color:#6366f1;'>Forgot password?</p>", unsafe_allow_html=True)

        st.markdown("</div>", unsafe_allow_html=True)

# ---------------- DETECTION ----------------
elif page == "Detection":

    st.markdown("<div class='section-title'>🧪 Skin Detection</div>", unsafe_allow_html=True)

    location = st.text_input("📍 Location (lat, lon)", "17.3850, 78.4867")

    file = st.file_uploader("Upload Image", type=["jpg","png","jpeg"])

    if file:
        img = Image.open(file)
        st.image(img, width=250)

        diseases = ["Acne", "Eczema", "Psoriasis", "Melanoma"]
        pred = random.choice(diseases)

        st.success(f"🧠 Disease: {pred}")

        if pred == "Acne":
            hospital = "City Skin Clinic"
            precaution = "Avoid oily food"
        elif pred == "Eczema":
            hospital = "Apollo Center"
            precaution = "Use moisturizer"
        elif pred == "Psoriasis":
            hospital = "Fortis Hospital"
            precaution = "Reduce stress"
        else:
            hospital = "AIIMS"
            precaution = "Consult doctor immediately"

        st.info(f"🏥 Hospital: {hospital}")
        st.warning(f"⚠️ Precaution: {precaution}")

        try:
            lat, lon = map(float, location.split(","))
            df = pd.DataFrame({"lat":[lat],"lon":[lon]})
            st.map(df)
        except:
            st.error("Enter correct format like 17.3850, 78.4867")

# ---------------- FEEDBACK ----------------
elif page == "Feedback":

    st.markdown("<div class='section-title'>💬 Patient Feedback</div>", unsafe_allow_html=True)

    name = st.text_input("Name")
    rating = st.slider("Rating",1,5)
    fb = st.text_area("Feedback")

    if st.button("Submit"):
        df = pd.DataFrame([[name,rating,fb]], columns=["Name","Rating","Feedback"])
        df.to_csv("feedback.csv", mode="a", header=False, index=False)

        st.success("✅ Feedback Saved")

# ---------------- ANALYTICS ----------------
elif page == "Analytics":

    st.markdown("<div class='section-title'>📊 Analytics</div>", unsafe_allow_html=True)

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
        st.info("No feedback yet")
