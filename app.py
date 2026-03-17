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
            st.success("Login successful ✅")
        else:
            st.error("Invalid credentials ❌")

# ---------------- DETECTION ----------------
elif choice == "Detection":
    st.title("🩺 Skin Disease Detection")

    def predict_disease():
        return "Acne"

    file = st.file_uploader("Upload Skin Image", type=["jpg","png","jpeg"])

    if file:
        img = Image.open(file)
        st.image(img, caption="Uploaded Image")

        disease = predict_disease()
        st.success("Detected Disease: " + disease)

        st.subheader("Recommended Hospitals")
        st.write("• Apollo Hospital")
        st.write("• AIIMS")
        st.write("• Fortis Hospital")

# ---------------- FEEDBACK ----------------
elif choice == "Feedback":
    st.title("📝 Feedback Form")

    name = st.text_input("Your Name")
    feedback = st.text_area("Your Feedback")

    # ⭐ Rating system
    rating = st.slider("Rate our service (1 = Bad, 5 = Excellent)", 1, 5)

    if st.button("Submit Feedback"):
        if name and feedback:
            st.success(f"Thanks {name}! ⭐ Rating: {rating}")
        else:
            st.warning("Please fill all fields")
