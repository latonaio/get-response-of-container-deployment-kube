FROM latonaio/l4t:latest

# Definition of a Device & Service
ENV POSITION=Runtime \
    SERVICE=get-response-of-container-deployment \
    AION_HOME=/var/lib/aion

# Setup Directoties
RUN mkdir -p $POSITION/$SERVICE
WORKDIR ${AION_HOME}/$POSITION/$SERVICE/

RUN pip3 install -U redis

ADD . .

CMD ["python3", "-u", "main.py"]