

from dagster import job

from tasks.task_runners.base import DagsterRunner


class CleanTrainingData(DagsterRunner):
    """
    Task Responsible for cleaning and resizing the images we have collected.
    """

    @job
    def clean_training_data():
        pass