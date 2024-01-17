import streamlit as st
import requests
from s3_fetch import download_image_from_s3

st.set_page_config(layout="wide", page_title="Text Based Image Retrieval")
st.title("Text Based Image Retrieval")

markdown_content = """Describe the image you have in mind, and our Image Retrieval App will find the closest match for you based on your text input. Whether you're looking for specific fashion styles, scenic landscapes, or any other visual concept, our app is designed to provide accurate and relevant results.

## How It Works
1. Enter a Text Description:
   - Use the input field to describe the image you are looking for in detail.
2. Click "Retrieve Image":
   - Click the button to initiate the retrieval process based on your text input.
3. Explore the Results:
   - The app will dynamically display the image that best matches your description.

## Tips for Effective Searches

- Be specific in your text description to get more accurate results.
- Experiment with different keywords and details to refine your search.

Give it a try and experience the power of text-based image retrieval with our innovative app!
"""

st.markdown(markdown_content)
st.markdown("---")

fastapi_url = "http://localhost:8000"
s3_bucket_name = "smalladmbucket"


def retrieve_closest_image(text):
    response = requests.get(f"{fastapi_url}/retrieve_closest_image", params={"text": text})
    return response.json()

st.markdown("## Enter text description:")
text_input = st.text_input("Enter text description:", label_visibility="hidden")
if st.button("Retrieve Closest Image"):
    closest_images = retrieve_closest_image(text_input)
    #st.write(closest_images)

    for closest_image in closest_images:
        image_data = download_image_from_s3(s3_bucket_name, f'img/{closest_image}.jpg')
        st.image(image_data)