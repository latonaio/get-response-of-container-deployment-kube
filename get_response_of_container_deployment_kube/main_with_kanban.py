from aion.microservice import Options, main_decorator
from aion.logger import lprint, initialize_logger
from get_response_of_container_deployment_kube import config, main


initialize_logger(config.MICROSERVICE_NAME)


@main_decorator(config.MICROSERVICE_NAME)
def main_with_kanban(opt: Options):
    conn = opt.get_conn()
    num = opt.get_number()

    try:
        for kanban in conn.get_kanban_itr(config.MICROSERVICE_NAME, num):
            metadata = kanban.get_metadata()
            # Check metadata
            keys = ['deviceName', 'projectName', 'microserviceName', 'projectCommitId', 'status', 'error']
            for key in keys:
                if key not in metadata:
                    raise RuntimeError(f"Not found '{key}' in metadadata.")

            main.main(
                metadata['deviceName'],
                metadata['projectName'],
                metadata['microserviceName'],
                metadata['projectCommitId'],
                metadata['status'],
                metadata['error'])

            conn.output_kanban(
                metadata=metadata
            )
            lprint(f'Output kanban {metadata}.')

    except Exception as e:
        lprint(str(e))


if __name__ == "__main__":
    main_with_kanban()
