"""
This file is storing the definitions of the tasks we want to execute.
"""
import typing
from tasks.task_runners.base import DagsterRunner
from tasks.task_runners.clean_training_data import CleanTrainingData
from tasks.task_runners.populate_training_data import PopulateTrainingData

clean_data_runner: DagsterRunner = CleanTrainingData()
populate_training_data_runner: DagsterRunner = PopulateTrainingData()

TaskDefinitions: typing.Dict[str, function] = {
    'clean_training_data': clean_data_runner.clean_training_data,
    'populate_training_data': populate_training_data_runner.populate_training_data
}