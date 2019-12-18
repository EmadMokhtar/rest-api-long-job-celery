# rest-api-long-job-celery
Sample project to demonstrate how to trigger a long running job without blocking the request.

# Run

## Broker (RabbitMQ)

```bash
$ docker run -d -p 5462:5462 rabbitmq
```

## Celery

```bash
celery -A rest_api_long_job_celery worker -l info
```

## Django App

```bash
./manage.py runserver
```
