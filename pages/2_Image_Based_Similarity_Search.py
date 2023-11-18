import streamlit as st
import requests
from s3_fetch import download_image_from_s3


st.set_page_config(layout="wide", page_title="Image-Based Similarity Search")
st.title("Image-Based Similarity Search")

markdown_content = """Upload an image or provide a URL, and our Image Retrieval App will find three other images that share similarities with the uploaded image. This feature is ideal for discovering variations of your favorite visuals or exploring related content based on a reference image.

## How It Works
1. Upload an Image or Provide a URL:
   - Use the provided input options to either upload an image file or enter the URL of the image.
2. Click "Find Similar Images":
   - Click the button to initiate the similarity search based on the uploaded image.
3. Explore the Results:
   - The app will display the uploaded image along with three additional images that are deemed similar based on the system's image retrieval capabilities.

## Tips for Effective Searches

- Choose clear and distinct images for better similarity results.
- Experiment with different types of images to explore a variety of visually related content.

Give it a try and explore the diverse world of visually similar images with our Image Retrieval App!
"""

st.markdown(markdown_content)
st.markdown("---")


fastapi_url = "http://localhost:8000"
s3_bucket_name = "bucketforclip"

def retrieve_similar_images():
    response = requests.get(f"{fastapi_url}/retrieve_similar_images")
    return response.json()

st.markdown("## Upload Image:")
uploaded_file = st.file_uploader("Upload Image", type=["jpg", "jpeg"], label_visibility="hidden")
if uploaded_file is not None:
    if st.button("Retrieve Similar Images"):

        with open("img.jpg", "wb") as f:
            f.write(uploaded_file.getbuffer())
            f.close()

        st.image(uploaded_file, caption="Uploaded Image", use_column_width=True)

        similar_images = retrieve_similar_images()

        st.write(similar_images)

        for similar_image in similar_images:
            st.image(f"{s3_bucket_url}{similar_image}.jpg")
