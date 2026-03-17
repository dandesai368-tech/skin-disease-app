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
    font-size: 38px;
    font-weight: 800;
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

/* Buttons */
.stButton>button {
    background: linear-gradient(to right, #6366f1, #8b5cf6);
    color: white;
    font-size: 18px;
    border-radius: 10px;
}

/* Section headings */
.section-title {
    font-size: 34px;
    font-weight: 800;
    color: #1e3a8a;
    margin-top: 20px;
}

/* Animation */
@keyframes fadeIn {
    from {opacity: 0; transform: translateY(20px);}
    to {opacity: 1; transform: translateY(0);}
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

        # Visible Cards
        st.markdown(f"""
        <div style="background:#d1fae5;padding:18px;border-radius:12px;
        margin-top:15px;font-size:20px;font-weight:700;color:#065f46;">
        🧠 Disease: {pred}
        </div>
        """, unsafe_allow_html=True)

        st.markdown(f"""
        <div style="background:#dbeafe;padding:18px;border-radius:12px;
        margin-top:10px;font-size:20px;font-weight:700;color:#1e3a8a;">
        🏥 Hospital: {hospital}
        </div>
        """, unsafe_allow_html=True)

        st.markdown(f"""
        <div style="background:#fef3c7;padding:18px;border-radius:12px;
        margin-top:10px;font-size:20px;font-weight:700;color:#92400e;">
        ⚠️ Precaution: {precaution}
        </div>
        """, unsafe_allow_html=True)

        try:
            lat, lon = map(float, location.split(","))
            df = pd.DataFrame({"lat":[lat],"lon":[lon]})
            st.map(df)
        except:
            st.error("Enter correct format like 17.3850, 78.4867")

# ---------------- FEEDBACK ----------------
elif page == "Feedback":

    st.markdown("<div class='section-title'>💬 Patient Feedback</div>", unsafe_allow_html=True)

    name = st.text_input("👤 Name")
    age = st.number_input("🎂 Age", min_value=1, max_value=100, step=1)
    gender = st.selectbox("⚧ Gender", ["Male", "Female", "Other"])
    location = st.text_input("📍 Location")

    disease = st.selectbox("🧠 Disease", ["Acne", "Eczema", "Psoriasis", "Melanoma"])

    rating = st.slider("⭐ Rating", 1, 5)
    fb = st.text_area("💬 Feedback")

    if st.button("Submit Feedback"):

        df = pd.DataFrame([[name, age, gender, location, disease, rating, fb]],
                          columns=["Name", "Age", "Gender", "Location", "Disease", "Rating", "Feedback"])

        df.to_csv("feedback.csv", mode="a", header=False, index=False)

        st.success("✅ Feedback Saved Successfully!")

# ---------------- ANALYTICS ----------------
elif page == "Analytics":

    st.markdown("<div class='section-title'>📊 Analytics</div>", unsafe_allow_html=True)

    try:
        df = pd.read_csv("feedback.csv")

        st.subheader("⭐ Ratings Distribution")
        st.bar_chart(df["Rating"].value_counts())

        st.subheader("🧠 Disease Cases")
        st.bar_chart(df["Disease"].value_counts())

        st.subheader("⚧ Gender Distribution")
        st.bar_chart(df["Gender"].value_counts())

    except:
        st.info("No data available yet")
  
