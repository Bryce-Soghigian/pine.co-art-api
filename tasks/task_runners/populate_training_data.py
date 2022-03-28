from dagster import job, op

from tasks.task_runners.base import DagsterRunner
from ...minio.client import get_client


class PopulateTrainingData(DagsterRunner):
    """
    Task for populating the minio training bucket.
    """

    TRAINING_BUCKET_NAME: str = 'GAN_TRAINING_DATA'

    @op
    def _initialize_bucket_if_not_exist(self):
        """
        Method for managing the creation of the gan training data bucket.
        """
        pass

    @op
    def _add_abscract_art_gallery(self):
        """
        """
        pass
    
    @job
    def populate_training_data(self,):
        """
        Populate training data bucket.
        """
        self._initialize_bucket_if_not_exist()