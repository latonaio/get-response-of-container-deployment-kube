import datetime
import redis

from get_response_of_container_deployment_kube import config


def get_client():
    return redis.Redis(
        host=config.REDIS_HOST,
        port=int(config.REDIS_PORT),
        password=config.REDIS_PASSWORD,
        db=int(config.REDIS_DB)
    )


def hset(device_name, project_name, microservice_name, project_commit_id, status, error):
    name = f'{device_name},{project_name},{microservice_name}'

    r = get_client()
    with r.pipeline() as pipe:
        pipe.hset(name, key='status', value=status)
        pipe.hset(name, key='error', value=error)
        pipe.hset(name, key='updated_by', value=config.MICROSERVICE_NAME)
        pipe.hset(name, key='updated_at', value=datetime.datetime.now().isoformat())

        pipe_result = pipe.execute()
    return
