import rembg as rb
from PIL import Image
import streamlit as st
from io import BytesIO

# Set page configuration
st.set_page_config(page_title="Background Remover", layout="wide")

# Custom CSS for styling
st.markdown(
    """
    <style>
    .main {
        background-color: #f0f2f5;
        padding: 20px;
        border-radius: 10px;
    }
    h1 {
        color: #4a4a4a;
    }
    h2 {
        color: #4a4a4a;
    }
    .sidebar {
        background-color: #ffffff;
        padding: 20px;
        border-radius: 10px;
    }
    .footer {
        text-align: center;
        margin-top: 20px;
        font-size: 14px;
        color: #888888;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Title
st.title("Background Remover")
st.markdown("### Remove backgrounds from your images effortlessly!")

# Sidebar content
with st.sidebar:
    st.write("### About the Developer")
    st.write("Nithish")
    st.caption("Follow me here↓")
    st.write("LinkedIn: [LinkedIn](https://www.linkedin.com/in/nithish-s-53a9a5292/)")
    st.write("Github: [Github](https://github.com/Nithish3115/)")
    # st.image("https://via.placeholder.com/150", caption="Your image here", use_column_width=True)

# File uploader
img_inp = st.file_uploader("Upload your image here", type=["jpg", "png", "jpeg"], accept_multiple_files=False)

def downloadable(img):
    buf = BytesIO()
    img.save(buf, format="PNG")
    byte_im = buf.getvalue()
    return byte_im

if img_inp is not None:
    image = Image.open(img_inp)
    fixed = rb.remove(image)
    downloadable_image = downloadable(fixed)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.header("Your Uploaded Image")
        st.image(image, use_column_width=True)
        
    with col2:
        st.header("Background Removed Image")
        st.image(downloadable_image, use_column_width=True)

    st.download_button("Download BG Removed Image", downloadable_image, key="download_button", file_name="bgremoved.png")

# Footer section
st.markdown(
    """
    <div class="footer">
        <p>Created with ❤️ by Nithish</p>
    </div>
    """,
    unsafe_allow_html=True,
)