import streamlit as st
import boto3
from botocore.exceptions import NoCredentialsError

def download_image_from_s3(bucket_name, object_key):

    s3 = boto3.client('s3')

    try:
        response = s3.get_object(Bucket=bucket_name, Key=object_key)
        image_data = response['Body'].read()
        print("this")
        return image_data
    except NoCredentialsError:
        st.error("Credentials not available. Please configure AWS credentials.")
        return None
    except Exception as e:
        st.error(f"Error: {e}")
        return None
