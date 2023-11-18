import streamlit as st
import requests
import clip
from process_input import encode_image_query
from PIL import Image

fastapi_url = "http://localhost:8000"

def retrieve_closest_image(text):
    response = requests.get(f"{fastapi_url}/retrieve_closest_image", params={"text": text})
    return response.json()

def retrieve_similar_images(image_vector):
    response = requests.get(f"{fastapi_url}/retrieve_similar_images", params={"image_vector": image_vector})
    return response.json()

# Streamlit app
def main():
    st.title("Fashion Image Retrieval App")

    text_input = st.text_input("Enter text description:")
    if st.button("Retrieve Closest Image"):
        closest_image = retrieve_closest_image(text_input)
        st.write(closest_image)

    uploaded_file = st.file_uploader("Upload Image", type=["jpg", "jpeg"])
    if uploaded_file is not None:
        if st.button("Retrieve Similar Images"):

            img = Image.open(uploaded_file)

            st.image(uploaded_file, caption="Uploaded Image", use_column_width=True)

            image_vector = encode_image_query(img)

            print(type(image_vector))

            similar_images = retrieve_similar_images(image_vector)

            st.write(similar_images)

            '''for similar_image in similar_images:
                st.image(f"{s3_bucket_url}{similar_image['image_id']}.jpg")'''

if __name__ == "__main__":
    main()
