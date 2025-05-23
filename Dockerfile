FROM alpine:latest
RUN apk add --no-cache mysql-client mysql postgresql15 python3 py3-pip podman
#RUN rc-service mariadb start
#RUN rc-service postgresql start
WORKDIR /app
#RUN python3 -m venv /app/.venv
#RUN source /app/.venv/bin/activate
#RUN python3 -m ensurepip
RUN pip3 install --no-cache --upgrade pip setuptools poetry --break-system-packages

WORKDIR /app
COPY . /app/

RUN poetry update
RUN poetry build
RUN poetry install 

ENTRYPOINT ["python3", "/app/src/main.py"]
#ENTRYPOINT ["mysql"]