from fastapi import FastAPI
import pinecone
from process_input import encode_search_query, encode_image_query
from dotenv import load_dotenv
import streamlit as st

PINECONE_API_KEY = st.secrets["PINECONE_API_KEY"]
PINECONE_ENVIRONMENT = st.secrets["PINECONE_ENVIRONMENT"]

pinecone.init(api_key = PINECONE_API_KEY, environment = PINECONE_ENVIRONMENT)

PINECONE_INDEX = st.secrets["PINECONE_INDEX"]

index = pinecone.Index(PINECONE_INDEX)

app = FastAPI()

@app.get("/retrieve_closest_image")
def retrieve_closest_image(text: str):

    encoded_text = encode_search_query(text)

    closest_image_ids = index.query(
        vector=encoded_text,
        top_k=3,
        include_values=False
    )

    closest_image_ids = [i['id'] for i in closest_image_ids['matches']]

    return closest_image_ids

@app.get("/retrieve_similar_images")
def retrieve_similar_images():

    image_vector = encode_image_query()

    closest_image_ids = index.query(
        vector=image_vector,
        top_k=3, 
        metric='euclidean',
        include_values=False
    )

    print("We have reached here")

    closest_image_ids = [i['id'] for i in closest_image_ids['matches']]

    return closest_image_ids
