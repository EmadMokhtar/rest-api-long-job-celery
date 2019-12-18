from celery import uuid
from django_celery_results.models import TaskResult

from django.urls import reverse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .tasks import very_long_task


class JobTriggerView(APIView):
    def post(self, request, *args, **kwargs):
        task_id = uuid()
        very_long_task.apply_async(task_id=task_id)
        status_url = reverse('job_status', kwargs={'task_id': task_id})
        headers = {'location': status_url}
        return Response(status=status.HTTP_202_ACCEPTED, headers=headers)


class JotStatusView(APIView):
    def get(self, request, *args, **kwargs):
        task_id = kwargs.get('task_id')
        try:
            task_result = TaskResult.objects.get(task_id=task_id)
            return Response(status=status.HTTP_200_OK,
                            data={'status': task_result.status,
                                  'result': task_result.result,
                                  'done_at': task_result.date_done.isoformat()})
        except TaskResult.DoesNotExist:
            # TODO: Enhance the checking for the task status
            return Response(status=status.HTTP_404_NOT_FOUND,
                            data={'status': 'IN-PROGRESS'})
