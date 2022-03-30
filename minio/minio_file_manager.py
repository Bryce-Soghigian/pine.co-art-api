"""
What does a file manager need to be able to do? 



What common functionaity can we take for minio?








FileRead


FileWrite



CreateBucket





"""


from xmlrpc.client import ResponseError
from minio.client import get_client


class BucketManager:
    def __init__(self):
        self.client = get_client()
        self.buckets: set = self._get_buckets()

    def _get_buckets(self) -> set:
        return set([bucket for bucket in self.client.list_buckets()])

    def create_bucket(self, bucket_name: str):
        """
        Create bucket if it doesn't exist.
        """
        if bucket_name not in self.buckets:
            try:
                self.client.make_bucket(bucket_name, location='us-east-1')
            except ResponseError as err:
                print(err)

    def remove_bucket(self, bucket_name):
        """
        Why you tryna get info from this docstring. It removes a bucket bruh.
        """
        try:
            self.client.remove_bucket(bucket_name)
        except ResponseError as err:
            print(err)

    