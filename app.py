import streamlit as st

st.set_page_config(page_title="Skin Disease App", layout="centered")

# ---------- CUSTOM CSS ----------
st.markdown("""
<style>
body {
    background-color: #eef2f7;
}

/* Center card */
.main-box {
    background: white;
    padding: 30px;
    border-radius: 15px;
    box-shadow: 0px 6px 20px rgba(0,0,0,0.15);
}

/* Headings */
.title {
    text-align: center;
    font-size: 34px;
    font-weight: bold;
    color: #2c3e50;
}

.subtitle {
    text-align: center;
    font-size: 18px;
    color: #555;
    margin-bottom: 20px;
}

/* Input labels */
.label {
    font-size: 18px;
    font-weight: bold;
    color: #333;
}

/* Button */
.stButton>button {
    background: linear-gradient(90deg, #6a5acd, #00bcd4);
    color: white;
    font-size: 18px;
    border-radius: 10px;
    padding: 10px;
    width: 100%;
}

/* Success box */
.success-box {
    background: linear-gradient(90deg, #00c853, #69f0ae);
    padding: 18px;
    border-radius: 12px;
    text-align: center;
    color: black;
    font-size: 20px;
    font-weight: bold;
    box-shadow: 0px 4px 10px rgba(0,0,0,0.2);
    animation: fadeIn 1s ease-in-out;
}

/* Animation */
@keyframes fadeIn {
    from {opacity: 0;}
    to {opacity: 1;}
}
</style>
""", unsafe_allow_html=True)

# ---------- LOGIN PAGE ----------
st.markdown('<div class="main-box">', unsafe_allow_html=True)

st.markdown('<div class="title">🔥 Welcome Back</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Please enter your details</div>', unsafe_allow_html=True)

st.markdown('<div class="label">👤 Username</div>', unsafe_allow_html=True)
username = st.text_input("", placeholder="Enter your username")

st.markdown('<div class="label">🔑 Password</div>', unsafe_allow_html=True)
password = st.text_input("", type="password", placeholder="Enter your password")

login = st.button("Login")

st.markdown('</div>', unsafe_allow_html=True)

# ---------- AFTER LOGIN ----------
if login:
    if username == "admin" and password == "1234":
        
        st.markdown("""
        <div class="success-box">
        ✅ Login Successful!
        </div>
        """, unsafe_allow_html=True)

        st.write("")

        # ---------- SKIN DETECTION ----------
        st.markdown("<h2 style='color:#1976d2;'>🧠 Skin Disease Detection</h2>", unsafe_allow_html=True)

        image = st.file_uploader("📸 Upload Skin Image", type=["jpg", "png"])

        if image:
            st.image(image, width=250)

            st.markdown("""
            <div style="background:#c8e6c9; padding:15px; border-radius:10px; font-size:18px;">
            🧠 Disease: <b>Psoriasis</b>
            </div>
            """, unsafe_allow_html=True)

            st.markdown("""
            <div style="background:#bbdefb; padding:15px; border-radius:10px; font-size:18px;">
            🏥 Hospital: <b>Fortis Hospital</b>
            </div>
            """, unsafe_allow_html=True)

            st.markdown("""
            <div style="background:#fff9c4; padding:15px; border-radius:10px; font-size:18px;">
            ⚠ Precaution: <b>Reduce stress</b>
            </div>
            """, unsafe_allow_html=True)

        # ---------- FEEDBACK ----------
        st.markdown("<h2 style='color:#6a5acd;'>💬 Patient Feedback</h2>", unsafe_allow_html=True)

        st.markdown('<div class="label">👤 Name</div>', unsafe_allow_html=True)
        name = st.text_input(" ")

        st.markdown('<div class="label">🎂 Age</div>', unsafe_allow_html=True)
        age = st.number_input(" ", min_value=1, max_value=100)

        st.markdown('<div class="label">⚧ Gender</div>', unsafe_allow_html=True)
        gender = st.selectbox(" ", ["Male", "Female", "Other"])

        st.markdown('<div class="label">📍 Location</div>', unsafe_allow_html=True)
        location = st.text_input("  ")

        st.markdown("""
        <h3 style='color:#ff9800;'>⭐ Rating</h3>
        """, unsafe_allow_html=True)
        rating = st.slider("", 1, 5)

        st.markdown("""
        <h3 style='color:#6a5acd;'>💬 Feedback</h3>
        """, unsafe_allow_html=True)
        feedback = st.text_area("")

        if st.button("Submit Feedback"):
            st.markdown("""
            <div class="success-box">
            ✅ Feedback Saved Successfully!
            </div>
            """, unsafe_allow_html=True)

    else:
        st.error("❌ Invalid Username or Password")
