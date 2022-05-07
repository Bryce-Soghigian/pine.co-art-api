import typing
import os
import urllib3
from common.utils import verify_env_vars
from minio import Minio
from urllib3.exceptions import MaxRetryError


def get_client() -> typing.Union[Minio, None]:
    verify_env_vars(['MINIO_HOST', 'MINIO_ACCESS_KEY', 'MINIO_SECRET_KEY'])
    url = f"http://{os.getenv('MINIO_HOST')}"
    config = {
        "endpoint": "localhost:9000",
        "access_key": os.getenv('MINIO_ACCESS_KEY'),
        "secret_key": os.getenv("MINIO_SECRET_KEY"),
        "secure": False,
        "http_client": urllib3.PoolManager(
            num_pools=10,
        )
    }
    try:
        client = Minio(**config)
        print(dir(client))
        client.list_buckets()
        print(client)
        return client
    except MaxRetryError:
        print("Object Storage Not Reachable.")