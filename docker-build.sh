#!/bin/sh

PUSH=$1
DATE="$(date "XXXXXX")"
REPOSITORY_PREFIX="latonaio"
SERVICE_NAME="get-response-of-container-deployment"

DOCKER_BUILDKIT=1 docker build --progress=plain -t ${SERVICE_NAME}:"${DATE}" .

# tagging
docker tag ${SERVICE_NAME}:"${DATE}" ${SERVICE_NAME}:latest
docker tag ${SERVICE_NAME}:"${DATE}" ${REPOSITORY_PREFIX}/${SERVICE_NAME}:"${DATE}"
docker tag ${REPOSITORY_PREFIX}/${SERVICE_NAME}:"${DATE}" ${REPOSITORY_PREFIX}/${SERVICE_NAME}:latest

if [[ $PUSH == "push" ]]; then
    docker push ${REPOSITORY_PREFIX}/${SERVICE_NAME}:"${DATE}"
    docker push ${REPOSITORY_PREFIX}/${SERVICE_NAME}:latest
fi