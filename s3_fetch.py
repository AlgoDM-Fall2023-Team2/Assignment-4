import streamlit as st
import boto3
from botocore.exceptions import NoCredentialsError
import os
from dotenv import load_dotenv

load_dotenv()

def download_image_from_s3(bucket_name, object_key):

    os.environ["AWS_ACCESS_KEY_ID"] = st.secrets["AWS_ACCESS_KEY_ID"]
    os.environ["AWS_SECRET_ACCESS_KEY"] = st.secrets["AWS_SECRET_ACCESS_KEY"]
    os.environ["AWS_DEFAULT_REGION"] = st.secrets["AWS_DEFAULT_REGION"]

    s3 = boto3.client('s3')

    try:
        response = s3.get_object(Bucket=bucket_name, Key=object_key)
        image_data = response['Body'].read()
        return image_data
    except NoCredentialsError:
        st.error("Credentials not available. Please configure AWS credentials.")
        return None
    except Exception as e:
        st.error(f"Error: {e}")
        return None