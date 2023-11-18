# Image Retrieval Application

This repository contains the code for an Image Retrieval Application that leverages text-based image retrieval and image-based similarity search functionalities. The application is designed to compute embeddings for images from the DeepFashion dataset, store them using PINECONE, and allow users to interact with the system through a user-friendly interface.
1. [CodeLabs Link](https://codelabs-preview.appspot.com/?file_id=1Ww3bBMuvr5AdwmC-yPtXWK67wCeVEtW54jPR4uboBBg#0)
2. [Streamlit Application]()


## Installation

To run this application, follow these steps:

1. Install the required dependencies by running the following command in your terminal:

   ```bash
   pip install -r requirements.txt
    ```
2. Open two new terminals for concurrent processes.

    In Terminal 1, run the Streamlit application:
    ```bash
    streamlit run Hello.py
    ```
3. In Terminal 2, run the FastAPI application using Uvicorn:
    ```bash
    uvicorn app:app --reload
   ```
    This will launch the FastAPI server, enabling the backend logic for efficient image retrieval based on user requests. 

## Usage
Once both processes are running, navigate to the provided Streamlit app URL (usually http://localhost:8501) in your web browser. The app will guide you through text-based image retrieval and image-based similarity search functionalities.

- For text-based image retrieval, enter a descriptive text in the input field and click the appropriate button to retrieve the closest matching image.

- For image-based similarity search, either upload an image or provide a URL. Click the corresponding button to find three other images similar to the uploaded one.

Explore the rich world of image retrieval with this application!

# Background Information
The application utilizes PINECONE for efficient storage and retrieval of image embeddings, and images are securely stored in an Amazon S3 bucket. The FastAPI backend seamlessly integrates with the Streamlit frontend, providing a smooth and responsive user experience.

Feel free to customize and extend this application based on your specific requirements and use cases. Happy exploring!