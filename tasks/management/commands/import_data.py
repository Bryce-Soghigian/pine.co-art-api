import typing
import os
from django.core.management.base import BaseCommand, CommandError

from bucket_storage.minio_file_manager import FileManager
from common.constants import GAN_TRAINING_DATA


class Command(BaseCommand):
    help = 'Command used for importing data into a bucket'

    def add_arguments(self, parser) -> None:
        parser.add_argument('bucket_name')
        parser.add_argument('data_path')

    def _upload_images(self, image_paths: typing.List[typing.Tuple[str, str]]):

        file_manager = FileManager()

        for image_path,image_name in image_paths:
            file_manager.upload_file(GAN_TRAINING_DATA,image_name, image_path)
        

    def handle(self, *args, bucket_name, data_path, **options):
        """
        Main function that gets executed when calling the command.
        

        1. Check to see if data_path exists:
            if not true:
                exit
        2. if true:
            iterate through that directory and get all of the files
        
        """
        if not os.path.isdir(data_path):
            self.stdout.write(f'{data_path} is not a valid directory.')
            return
        self.stdout.write(f'Importing data to {bucket_name} from {data_path}....')
        image_paths = []
        current_path = os.getcwd()
        for name in os.listdir(data_path):
            if name.endswith('.jpg'):
                image_paths.append((current_path + name, name))
        

        self.stdout.write('Attempting to upload images....')
        self._upload_images(image_paths=image_paths)
        self.stdout.write('Successfully uploaded images.')



