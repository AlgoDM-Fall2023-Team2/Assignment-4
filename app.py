from fastapi import FastAPI
import pinecone
from process_input import encode_search_query, encode_image_query

#pinecone.init(api_key = "751e7796-d00e-4382-98aa-557196118a24", environment="gcp-starter")
pinecone.init(api_key = "bb5c549b-3015-44a6-9e7b-f7939252ffbc", environment="gcp-starter")

index = pinecone.Index("vectors")

app = FastAPI()

s3_bucket_url = "https://your-s3-bucket-url.s3.amazonaws.com/"

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
