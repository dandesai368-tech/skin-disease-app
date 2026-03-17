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
    font-weight: 900;
    color: #0f172a;
}

/* Section Title */
.section-title {
    font-size: 36px;
    font-weight: 900;
    color: #1e3a8a;
    margin-top: 20px;
}

/* Label Style */
.label {
    font-size: 22px;
    font-weight: 800;
    color: #000000;
    margin-top: 15px;
}

/* Card */
.card {
    background: white;
    padding: 40px;
    border-radius: 20px;
    box-shadow: 0px 10px 30px rgba(0,0,0,0.15);
}

/* Login */
.login-title {
    font-size: 38px;
    font-weight: 900;
    color: #000;
    text-align:center;
}

.login-sub {
    font-size: 18px;
    color: #374151;
    text-align:center;
}

/* Buttons */
.stButton>button {
    background: linear-gradient(to right, #6366f1, #8b5cf6);
    color: white;
    font-size: 18px;
    border-radius: 10px;
}

/* Dark Inputs */
.stTextInput input, .stNumberInput input {
    background-color: #1f2937;
    color: white;
    border-radius: 10px;
}

.stSelectbox div {
    background-color: #1f2937 !important;
    color: white !important;
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

        st.markdown("<div class='login-title'>Welcome back 👋</div>", unsafe_allow_html=True)
        st.markdown("<div class='login-sub'>Please enter your details</div>", unsafe_allow_html=True)

        st.markdown("<div class='label'>👤 Username</div>", unsafe_allow_html=True)
        username = st.text_input("")

        st.markdown("<div class='label'>🔑 Password</div>", unsafe_allow_html=True)
        password = st.text_input("", type="password")

        if st.button("Sign In"):
            if username == "admin" and password == "1234":
                st.success("✅ Login Successful!")
            else:
                st.error("❌ Invalid Credentials")

        st.markdown("</div>", unsafe_allow_html=True)

# ---------------- DETECTION ----------------
elif page == "Detection":

    st.markdown("<div class='section-title'>🧪 Skin Detection</div>", unsafe_allow_html=True)

    st.markdown("<div class='label'>📍 Location (lat, lon)</div>", unsafe_allow_html=True)
    location = st.text_input("", "17.3850, 78.4867")

    st.markdown("<div class='label'>📷 Upload Image</div>", unsafe_allow_html=True)
    file = st.file_uploader("", type=["jpg","png","jpeg"])

    if file:
        img = Image.open(file)
        st.image(img, width=250)

        diseases = ["Acne", "Eczema", "Psoriasis", "Melanoma"]
        pred = random.choice(diseases)

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

        # Result Cards
        st.markdown(f"""
        <div style="background:#d1fae5;padding:18px;border-radius:12px;
        margin-top:15px;font-size:20px;font-weight:800;color:#065f46;">
        🧠 Disease: {pred}
        </div>
        """, unsafe_allow_html=True)

        st.markdown(f"""
        <div style="background:#dbeafe;padding:18px;border-radius:12px;
        margin-top:10px;font-size:20px;font-weight:800;color:#1e3a8a;">
        🏥 Hospital: {hospital}
        </div>
        """, unsafe_allow_html=True)

        st.markdown(f"""
        <div style="background:#fef3c7;padding:18px;border-radius:12px;
        margin-top:10px;font-size:20px;font-weight:800;color:#92400e;">
        ⚠️ Precaution: {precaution}
        </div>
        """, unsafe_allow_html=True)

        # -------- MAP FIX --------
        try:
            lat, lon = location.split(",")
            lat = float(lat.strip())
            lon = float(lon.strip())

            df = pd.DataFrame({"lat":[lat], "lon":[lon]})

            st.markdown("<div class='section-title'>📍 Location Map</div>", unsafe_allow_html=True)
            st.map(df)

        except:
            st.error("❌ Enter location like: 17.3850, 78.4867")

# ---------------- FEEDBACK ----------------
elif page == "Feedback":

    st.markdown("<div class='section-title'>💬 Patient Feedback</div>", unsafe_allow_html=True)

    st.markdown("<div class='label'>👤 Name</div>", unsafe_allow_html=True)
    name = st.text_input("")

    st.markdown("<div class='label'>🎂 Age</div>", unsafe_allow_html=True)
    age = st.number_input("", 1, 100)

    st.markdown("<div class='label'>⚧ Gender</div>", unsafe_allow_html=True)
    gender = st.selectbox("", ["Male","Female","Other"])

    st.markdown("<div class='label'>📍 Location</div>", unsafe_allow_html=True)
    loc = st.text_input(" ")

    st.markdown("<div class='label'>🧠 Disease</div>", unsafe_allow_html=True)
    disease = st.selectbox(" ", ["Acne","Eczema","Psoriasis","Melanoma"])

    st.markdown("<div class='label'>⭐ Rating</div>", unsafe_allow_html=True)
    rating = st.slider("", 1, 5)

    st.markdown("<div class='label'>💬 Feedback</div>", unsafe_allow_html=True)
    fb = st.text_area("")

    if st.button("Submit Feedback"):
        df = pd.DataFrame([[name, age, gender, loc, disease, rating, fb]],
                          columns=["Name","Age","Gender","Location","Disease","Rating","Feedback"])
        df.to_csv("feedback.csv", mode="a", header=False, index=False)
        st.success("✅ Feedback Saved Successfully!")

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
