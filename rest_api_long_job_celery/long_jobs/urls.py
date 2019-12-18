from django.urls import path

from . import views

urlpatterns = [
    path('', views.JobTriggerView.as_view(), name='job_trigger'),
    path('<uuid:task_id>/status/', views.JotStatusView.as_view(), name='job_status'),
]
