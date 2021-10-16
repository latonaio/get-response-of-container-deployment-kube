from get_response_of_container_deployment_kube import redis_


def main(device_name, project_name, microservice_name, project_commit_id, status, error):
    redis_.hset(device_name, project_name, microservice_name, project_commit_id, status, error)
    return


if __name__ == "__main__":
    device_name = 'prometheus'
    project_name = 'sample-project'
    microservice_name = 'nginx'
    project_commit_id = 'XXXXXXXXXXXXXXXXX'
    status = 2
    error = 'Sample Error'

    main(device_name, project_name, microservice_name, project_commit_id, status, error)
