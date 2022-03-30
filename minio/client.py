import os
from common.utils import verify_env_vars
from minio import Minio


def get_client():
    verify_env_vars(['MINIO_HOST', 'MINIO_ACCESS_KEY', 'MINIO_SECRET_KEY'])
    return Minio(
        os.getenv('MINIO_HOST'),
        access_key=os.getenv('MINIO_ACCESS_KEY'),
        secret_key=os.getenv('MINIO_SECRET_KEY'),
    )