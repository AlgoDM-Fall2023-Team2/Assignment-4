import clip
import torch
from PIL import Image
from io import BytesIO

device = "cuda" if torch.cuda.is_available() else "cpu"
model, preprocess = clip.load("ViT-B/32", device=device)

def encode_search_query(search_query):

    with torch.no_grad():
        text_encoded = model.encode_text(clip.tokenize(search_query).to(device))
        text_encoded /= text_encoded.norm(dim=-1, keepdim=True)

    print(text_encoded.shape)

    return text_encoded.tolist()

def encode_image_query():

    print("image encoding has started")

    with open("img.jpg", "rb") as f:
        image_bytes = f.read()

    img = Image.open(BytesIO(image_bytes))
    
    image_preprocessed = preprocess(img).to(device)
    image_preprocessed = image_preprocessed.unsqueeze(0)

    print("Input image shape:", image_preprocessed.shape)

    with torch.no_grad():
        image_features = model.encode_image(image_preprocessed)
        image_features = image_features.squeeze(0)
        image_features /= image_features.norm(dim=-1, keepdim=True)
        image_features = image_features.unsqueeze(0)

    print("Output features shape:", image_features.shape)

    print("Image encoding has ended")

    return image_features.cpu().numpy().tolist()