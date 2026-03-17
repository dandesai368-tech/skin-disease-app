import streamlit as st
from PIL import Image

# -------- PAGE SETTINGS --------
st.set_page_config(page_title="Skin Disease App", layout="centered")

# -------- SESSION --------
if "login" not in st.session_state:
    st.session_state.login = False

# -------- LOGIN PAGE --------
def login_page():
    st.title("🔐 Login Page")

    user = st.text_input("Username")
    pwd = st.text_input("Password", type="password")

    if st.button("Login"):
        if user == "admin" and pwd == "1234":
            st.session_state.login = True
            st.success("Login Successful ✅")
            st.rerun()   # 🔥 THIS FIXES YOUR PROBLEM
        else:
            st.error("Wrong Username/Password ❌")

# -------- MAIN APP --------
def app():
    st.sidebar.title("Menu")
    choice = st.sidebar.radio("Select", ["Skin Detection", "Feedback"])

    # -------- SKIN DETECTION --------
    if choice == "Skin Detection":
        st.title("🧴 Skin Disease Detection")

        file = st.file_uploader("Upload Skin Image", type=["jpg","png","jpeg"])

        if file:
            img = Image.open(file)
            st.image(img, caption="Uploaded Image", use_column_width=True)

            # Dummy prediction
            disease = "Acne"

            st.success("Detected Disease: " + disease)

            # -------- TIPS --------
            st.subheader("💡 Skin Care Tips")
            st.write("• Wash face twice daily")
            st.write("• Drink more water")
            st.write("• Avoid oily food")

            # -------- PRECAUTIONS --------
            st.subheader("⚠️ Precautions")
            st.write("• Do not touch affected area")
            st.write("• Avoid sunlight")
            st.write("• Keep skin clean")

    # -------- FEEDBACK --------
    if choice == "Feedback":
        st.title("💬 Feedback Form")

        name = st.text_input("Enter your name")
        msg = st.text_area("Your feedback")

        if st.button("Submit"):
            st.success("Thank you for your feedback!")

# -------- RUN --------
if st.session_state.login == False:
    login_page()
else:
    app()
