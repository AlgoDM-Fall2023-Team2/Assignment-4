import streamlit as st
import requests
from s3_fetch import download_image_from_s3
import subprocess

subprocess.Popen(["uvicorn", "app:app", "--reload"])

fastapi_url = "http://localhost:8000"
s3_bucket_name = "smalladmbucket"


def retrieve_closest_image(text):
    response = requests.get(f"{fastapi_url}/retrieve_closest_image", params={"text": text})
    return response.json()

def retrieve_similar_images():
    response = requests.get(f"{fastapi_url}/retrieve_similar_images")
    return response.json()

# Streamlit app
def main():
    st.title("Fashion Image Retrieval App")

    text_input = st.text_input("Enter text description:")
    if st.button("Retrieve Closest Image"):
        closest_images = retrieve_closest_image(text_input)
        st.write(closest_images)

        for closest_image in closest_images:
            image_data = download_image_from_s3(s3_bucket_name, f'img/{closest_image}.jpg')
            st.image(image_data)

    uploaded_file = st.file_uploader("Upload Image", type=["jpg", "jpeg"])
    if uploaded_file is not None:
        if st.button("Retrieve Similar Images"):

            with open("img.jpg", "wb") as f:
                f.write(uploaded_file.getbuffer())
                f.close()

            st.image(uploaded_file, caption="Uploaded Image", use_column_width=True)

            similar_images = retrieve_similar_images()

            st.write(similar_images)

            for similar_image in similar_images:
                image_data = download_image_from_s3(s3_bucket_name, f'img/{similar_image}.jpg')
                st.image(image_data)

if __name__ == "__main__":
    main()
