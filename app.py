import streamlit as st
from PIL import Image

# ---------- PAGE SETTINGS ----------
st.set_page_config(page_title="Skin Disease Detector", layout="wide")

# ---------- SIMPLE LOGIN ----------
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
            st.error("Invalid Credentials")

# ---------- MAIN APP ----------
def main_app():
    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Go to", ["Skin Detection", "Feedback"])

    # ---------- SKIN DETECTION ----------
    if page == "Skin Detection":
        st.title("🧴 Skin Disease Detection")

        uploaded_file = st.file_uploader("Upload Skin Image", type=["jpg", "png", "jpeg"])

        if uploaded_file:
            image = Image.open(uploaded_file)
            st.image(image, caption="Uploaded Image", use_column_width=True)

            # Dummy prediction
            disease = "Acne"

            st.success(f"Detected Disease: {disease}")
            st.info("Confidence: 92%")

            # ---------- TIPS ----------
            st.subheader("🧴 Skin Care Tips")
            if disease == "Acne":
                st.write("• Wash your face twice daily")
                st.write("• Avoid oily and junk food")
                st.write("• Use mild face wash")
                st.write("• Drink plenty of water")

            # ---------- PRECAUTIONS ----------
            st.subheader("⚠️ Precautions")
            st.write("• Do not touch or scratch the skin")
            st.write("• Avoid direct sunlight")
            st.write("• Keep skin clean and dry")
            st.write("• Consult a doctor if severe")

            # ---------- HOSPITALS ----------
            st.subheader("🏥 Recommended Hospitals")
            st.write("• Apollo Hospital")
            st.write("• AIIMS")
            st.write("• Fortis Hospital")

    # ---------- FEEDBACK ----------
    elif page == "Feedback":
        st.title("💬 Feedback Form")

        name = st.text_input("Name")
        feedback = st.text_area("Your Feedback")

        if st.button("Submit"):
            st.success("Thank you for your feedback!")

# ---------- RUN ----------
if not st.session_state.logged_in:
    login()
else:
    main_app()
            
