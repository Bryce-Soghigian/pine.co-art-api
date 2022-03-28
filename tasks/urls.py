from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('trigger/<task_type>', views.TaskExecutor.as_view(), name='trigger'),

]
