import typing
from bucket_storage.client import get_client

class FileManager:
    def __init__(self) -> None:
        self.client = get_client()
        self.bucket_manager = BucketManager()
        
    def upload_file(self, bucket: str, key: str, path: str):
        """
        Uploads a file.
        """
        self.bucket_manager.create_bucket(bucket) # creates bucket if it doesnt exist
        self.client.fput_object(bucket, key, path)
    
    def retrieve_file(self, key, bucket):
        pass
        
class BucketManager:
    def __init__(self):
        self.client = get_client()
        self.buckets: typing.List[str] = self._get_buckets()

    def _get_buckets(self) -> set:
        buckets = self.client.list_buckets()
        return [bucket for bucket in buckets]

    def create_bucket(self, bucket_name: str):
        """
        Create bucket if it doesn't exist.
        """
        if bucket_name not in self.buckets:
            self.client.make_bucket(bucket_name, location='us-east-1')

    def remove_bucket(self, bucket_name):
        """
        Why you tryna get info from this docstring. It removes a bucket bruh.
        """
        try:
            self.client.remove_bucket(bucket_name)
        except ResponseError as err:
            print(err)

    