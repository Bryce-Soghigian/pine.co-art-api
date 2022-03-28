from django import views, http
from django.http import HttpResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from .task_runners.task_definitions import TaskDefinitions


def index(request):
    return HttpResponse('Jobs3 home.')


class TaskFactory:
    """
    Class Responsible for creating dagster job instance.
    """
    def __init__(self, task_type: str):
        self.task_definition: function = TaskDefinitions[task_type]


@method_decorator(csrf_exempt, name='dispatch')
class TaskExecutor(views.View):
    """
    View responsible for executing a task.
    """

    def post(self, request: http.HttpRequest, task_type: str) -> http.HttpResponse:
        """
        Trigger a new task.
        :param request:
        :param job_type:
        :return:
        """
        task = TaskFactory(task_type)
        task.task_definition.execute_in_process()
        return HttpResponse('ok.')
