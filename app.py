import streamlit as st
from PIL import Image

st.set_page_config(page_title="Skin Disease App", layout="centered")

# Sidebar navigation
menu = ["Login", "Detection", "Feedback"]
choice = st.sidebar.selectbox("Menu", menu)

# ---------------- LOGIN ----------------
if choice == "Login":
    st.title("🔐 Login Page")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if username == "admin" and password == "1234":
            st.success("Login Successful ✅")
        else:
            st.error("Invalid Credentials ❌")

# ---------------- DETECTION ----------------
elif choice == "Detection":
    st.title("🩺 Skin Disease Detection")

    def predict_disease():
        return "Acne"

    uploaded_file = st.file_uploader("Upload Skin Image", type=["jpg","png","jpeg"])

    if uploaded_file:
        image = Image.open(uploaded_file)
        st.image(image)

        disease = predict_disease()
        st.success("Detected Disease: " + disease)

        st.subheader("Recommended Hospitals")
        st.write("• Apollo Hospital")
        st.write("• AIIMS")
        st.write("• Fortis Hospital")

# ---------------- FEEDBACK ----------------
elif choice == "Feedback":
    st.title("📝 Feedback Form")

    name = st.text_input("Name")
    feedback = st.text_area("Feedback")

    if st.button("Submit"):
        if name and feedback:
            st.success("Feedback Submitted ✅")
        else:
            st.warning("Please fill all fields ⚠️")
