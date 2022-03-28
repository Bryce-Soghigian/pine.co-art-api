import os
from minio import Minio

def get_client():
    return Minio(
        os.getenv('MINIO_HOST'),
        access_key=os.getenv('MINIO_ACCESS_KEY'),
        secret_key=os.getenv('MINIO_SECRET_KEY'),
    )