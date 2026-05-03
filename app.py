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

/* Dashboard Cards */
.dashboard-card {
    background: white;
    padding: 25px;
    border-radius: 15px;
    text-align: center;
    box-shadow: 0px 5px 15px rgba(0,0,0,0.1);
}

.dashboard-title {
    font-size: 20px;
    font-weight: 700;
    color: #374151;
}

.dashboard-value {
    font-size: 30px;
    font-weight: 900;
    color: #111827;
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

        st.success(f"🧠 Disease: {pred}")
        st.info(f"🏥 Hospital: {hospital}")
        st.warning(f"⚠️ Precaution: {precaution}")

        try:
            lat, lon = location.split(",")
            df = pd.DataFrame({"lat":[float(lat)], "lon":[float(lon)]})
            st.map(df)
        except:
            st.error("Enter valid location")

# ---------------- FEEDBACK ----------------
elif page == "Feedback":

    st.markdown("<div class='section-title'>💬 Patient Feedback</div>", unsafe_allow_html=True)

    name = st.text_input("Name")
    age = st.number_input("Age", 1, 100)
    gender = st.selectbox("Gender", ["Male","Female","Other"])
    loc = st.text_input("Location")
    disease = st.selectbox("Disease", ["Acne","Eczema","Psoriasis","Melanoma"])
    rating = st.slider("Rating", 1, 5)
    fb = st.text_area("Feedback")

    if st.button("Submit Feedback"):
        df = pd.DataFrame([[name, age, gender, loc, disease, rating, fb]])
        df.to_csv("feedback.csv", mode="a", header=False, index=False)
        st.success("Saved!")

# ---------------- ANALYTICS (DASHBOARD) ----------------
elif page == "Analytics":

    st.markdown("<div class='section-title'>📊 Dashboard</div>", unsafe_allow_html=True)

    try:
        df = pd.read_csv("feedback.csv",
                         names=["Name","Age","Gender","Location","Disease","Rating","Feedback"])
    except:
        df = pd.DataFrame(columns=["Name","Age","Gender","Location","Disease","Rating","Feedback"])

    total = len(df)
    common = df["Disease"].value_counts().idxmax() if total > 0 else "N/A"
    avg = round(df["Rating"].mean(),2) if total > 0 else 0

    c1, c2, c3 = st.columns(3)

    with c1:
        st.markdown(f"<div class='dashboard-card'><div class='dashboard-title'>Total Patients</div><div class='dashboard-value'>{total}</div></div>", unsafe_allow_html=True)

    with c2:
        st.markdown(f"<div class='dashboard-card'><div class='dashboard-title'>Most Common Disease</div><div class='dashboard-value'>{common}</div></div>", unsafe_allow_html=True)

    with c3:
        st.markdown(f"<div class='dashboard-card'><div class='dashboard-title'>Avg Rating</div><div class='dashboard-value'>{avg}</div></div>", unsafe_allow_html=True)

    st.markdown("---")

    if total > 0:
        st.subheader("Disease Distribution")
        st.bar_chart(df["Disease"].value_counts())

        st.subheader("Ratings")
        st.bar_chart(df["Rating"].value_counts())

        st.subheader("Recent Feedback")
        st.dataframe(df.tail(5))
    else:
        st.info("No data yet")
