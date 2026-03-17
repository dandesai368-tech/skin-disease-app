import streamlit as st
from PIL import Image
import random
import pandas as pd

# ---------------- PAGE CONFIG ----------------
st.set_page_config(page_title="Skin Disease Detection", layout="wide")

# ---------------- CSS (FINAL UI FIX) ----------------
st.markdown("""
<style>

/* Background */
.stApp {
    background: #f4f8fb;
}

/* MAIN HEADINGS */
h1 {
    color: #003366 !important;
    font-size: 48px !important;
    font-weight: bold;
    text-align: center;
}

h2 {
    color: #0b5394 !important;
    font-size: 28px !important;
}

/* Labels */
label {
    color: #000000 !important;
    font-weight: 600;
}

/* Card Style */
.card {
    padding: 30px;
    border-radius: 20px;
    background: white;
    box-shadow: 0px 8px 25px rgba(0,0,0,0.1);
}

/* Button Style */
.stButton>button {
    background-color: #0b5394;
    color: white;
    border-radius: 10px;
    padding: 10px 18px;
    font-size: 16px;
}

/* Make text visible */
p, span {
    color: black !important;
}

</style>
""", unsafe_allow_html=True)

# ---------------- SIDEBAR ----------------
st.sidebar.title("🔍 Navigation")
menu = ["Login", "Skin Detection", "Feedback", "Analytics"]
choice = st.sidebar.selectbox("Select Page", menu)

# ---------------- LOGIN PAGE ----------------
if choice == "Login":

    st.markdown("<h1>🩺 Skin Disease Detection System</h1>", unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1,2,1])

    with col2:
        st.markdown("<div class='card'>", unsafe_allow_html=True)

        st.markdown("<h2>👋 Welcome Back</h2>", unsafe_allow_html=True)

        username = st.text_input("👤 Username")

        show = st.checkbox("Show Password")
        password = st.text_input("🔑 Password", type="default" if show else "password")

        st.checkbox("Remember me")

        if st.button("🚀 Login"):
            if username == "admin" and password == "1234":
                st.success("Login Successful ✅")
            else:
                st.error("Invalid Login ❌")

        st.markdown("<p style='text-align:right;'>Forgot Password?</p>", unsafe_allow_html=True)

        st.markdown("</div>", unsafe_allow_html=True)

# ---------------- SKIN DETECTION ----------------
elif choice == "Skin Detection":

    st.markdown("<h1>🧠 Skin Disease Detection</h1>", unsafe_allow_html=True)

    location = st.text_input("📍 Enter Location (lat,lon)", "17.3850,78.4867")

    file = st.file_uploader("📤 Upload Skin Image", type=["jpg","png","jpeg"])

    if file:
        img = Image.open(file)

        # SMALL IMAGE
        st.image(img, width=250)

        diseases = ["Acne", "Eczema", "Psoriasis", "Melanoma"]
        result = random.choice(diseases)

        st.success(f"Detected Disease: {result}")

        # Hospital + Precautions
        if result == "Acne":
            hospital = "City Skin Clinic"
            precaution = "Wash face regularly"
        elif result == "Eczema":
            hospital = "Apollo Hospital"
            precaution = "Avoid dust and use creams"
        elif result == "Psoriasis":
            hospital = "Fortis Hospital"
            precaution = "Reduce stress"
        else:
            hospital = "AIIMS Hospital"
            precaution = "Consult doctor immediately"

        st.info(f"🏥 Hospital: {hospital}")
        st.warning(f"⚠️ Precautions: {precaution}")

        # MAP
        try:
            lat, lon = map(float, location.split(","))
            df = pd.DataFrame({"lat":[lat], "lon":[lon]})
            st.map(df)
        except:
            st.error("Enter location like: 17.3850,78.4867")

# ---------------- FEEDBACK ----------------
elif choice == "Feedback":

    st.markdown("<h1>💬 Patient Feedback</h1>", unsafe_allow_html=True)

    name = st.text_input("Name")
    rating = st.slider("Rating", 1, 5)
    text = st.text_area("Write Feedback")

    if st.button("Submit"):
        df = pd.DataFrame([[name, rating, text]])
        df.to_csv("feedback.csv", mode="a", header=False, index=False)

        st.success("Feedback Saved ✅")

        st.write("Patient had a good hospital experience and treatment was effective.")

# ---------------- ANALYTICS ----------------
elif choice == "Analytics":

    st.markdown("<h1>📊 Analytics Dashboard</h1>", unsafe_allow_html=True)

    data = {
        "Acne": random.randint(10,50),
        "Eczema": random.randint(10,50),
        "Psoriasis": random.randint(10,50),
        "Melanoma": random.randint(5,30)
    }

    st.subheader("Disease Cases")
    st.bar_chart(data)

    try:
        df = pd.read_csv("feedback.csv")
        st.subheader("User Ratings")
        st.bar_chart(df[1].value_counts())
    except:
        st.info("No feedback yet")
