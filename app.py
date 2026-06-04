import streamlit as st

st.set_page_config(
    page_title="Streamlit Web Interface",
    page_icon="🌐",
    layout="wide"
)

st.title("🌐 Streamlit Web Interface")

st.sidebar.header("Navigation")
page = st.sidebar.selectbox(
    "Choose a page",
    ["Home", "Upload File", "Settings"]
)

if page == "Home":
    st.header("Home")
    st.write("Welcome to the Streamlit web interface.")

    user_input = st.text_input("Enter some text")
    if st.button("Submit"):
        st.success(f"You entered: {user_input}")

elif page == "Upload File":
    st.header("File Upload")
    uploaded_file = st.file_uploader(
        "Choose a file",
        type=["csv", "txt", "pdf", "xlsx"]
    )

    if uploaded_file is not None:
        st.success(f"Uploaded: {uploaded_file.name}")
        st.write(f"File Size: {uploaded_file.size / 1024:.2f} KB")

elif page == "Settings":
    st.header("Settings")

    theme = st.selectbox(
        "Theme",
        ["Light", "Dark"]
    )

    notifications = st.checkbox(
        "Enable Notifications",
        value=True
    )

    if st.button("Save Settings"):
        st.success("Settings saved successfully!")

st.divider()
st.caption("Built with Streamlit")