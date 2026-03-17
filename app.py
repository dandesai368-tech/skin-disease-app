import streamlit as st
from PIL import Image

# Page settings
st.set_page_config(page_title="Skin Disease App", layout="wide")

# White background
st.markdown("""
<style>
body {
    background-color: white;
}
</style>
""", unsafe_allow_html=True)

# Sidebar navigation
page = st.sidebar.selectbox("Menu", ["Login", "Skin Detection", "Feedback"])

# ---------------- LOGIN PAGE ----------------
if page == "Login":
    st.title("🔐 Login Page")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if username == "admin" and password == "1234":
            st.success("Login Successful ✅")
        else:
            st.error("Invalid Username or Password ❌")

# ---------------- SKIN DETECTION ----------------
elif page == "Skin Detection":
    st.title("🧴 Skin Disease Detection")

    uploaded_file = st.file_uploader("Upload Skin Image", type=["jpg", "png", "jpeg"])

    if uploaded_file:
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image", use_column_width=True)

        # Fake prediction
        disease = "Acne"

        st.success("Detected Disease: " + disease)

        st.subheader("🏥 Recommended Hospitals")
        st.write("• Apollo Hospital")
        st.write("• AIIMS")
        st.write("• Fortis Hospital")

# ---------------- FEEDBACK ----------------
elif page == "Feedback":
    st.title("💬 Feedback Form")

    name = st.text_input("Your Name")
    rating = st.slider("Rate us", 1, 5)
    feedback = st.text_area("Your Feedback")

    if st.button("Submit"):
        st.success("Thank you for your feedback! ❤️")
