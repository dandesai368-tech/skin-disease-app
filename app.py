import streamlit as st
from PIL import Image

# ------------------ PAGE CONFIG ------------------
st.set_page_config(page_title="Skin Disease Detector", layout="centered")

# ------------------ SIMPLE LOGIN ------------------
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

def login():
    st.title("🔐 Login Page")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if username == "admin" and password == "1234":
            st.session_state.logged_in = True
            st.success("Login Successful!")
        else:
            st.error("Invalid Username or Password")

# ------------------ PREDICT FUNCTION ------------------
def predict_disease():
    return "Acne"   # Dummy prediction

# ------------------ SKIN TIPS ------------------
def skin_tips(disease):
    if disease == "Acne":
        return [
            "Wash your face twice daily",
            "Avoid oily and junk food",
            "Do not touch your face frequently",
            "Drink plenty of water",
            "Use mild face wash"
        ]
    else:
        return ["Consult a doctor for proper diagnosis"]

# ------------------ MAIN APP ------------------
def main_app():
    menu = ["Home", "Skin Detection", "Feedback", "Logout"]
    choice = st.sidebar.selectbox("Menu", menu)

    # -------- HOME --------
    if choice == "Home":
        st.title("🧴 Skin Disease Detection App")
        st.write("Upload your skin image and get prediction + tips")

    # -------- SKIN DETECTION --------
    elif choice == "Skin Detection":
        st.title("🔍 Detect Skin Disease")

        uploaded_file = st.file_uploader("Upload Skin Image", type=["jpg","png","jpeg"])

        if uploaded_file:
            image = Image.open(uploaded_file)
            st.image(image, caption="Uploaded Image", use_column_width=True)

            disease = predict_disease()
            st.success(f"Detected Disease: {disease}")
            st.info("Confidence: 92%")

            # Tips
            st.subheader("🧴 Skin Care Tips")
            tips = skin_tips(disease)
            for tip in tips:
                st.write("✔", tip)

            # Precautions
            st.subheader("⚠ Precautions")
            st.write("✔ Avoid self-medication")
            st.write("✔ Consult dermatologist if condition worsens")
            st.write("✔ Keep skin clean and dry")

    # -------- FEEDBACK --------
    elif choice == "Feedback":
        st.title("💬 Feedback Form")

        name = st.text_input("Your Name")
        feedback = st.text_area("Your Feedback")

        if st.button("Submit"):
            st.success("Thank you for your feedback!")

    # -------- LOGOUT --------
    elif choice == "Logout":
        st.session_state.logged_in = False
        st.warning("Logged out successfully")

# ------------------ RUN APP ------------------
if st.session_state.logged_in:
    main_app()
else:
    login()
