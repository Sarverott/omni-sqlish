FROM alpine:latest
RUN apk add --no-cache mysql-client mysql postgresql15 python3 py3-pip podman
#RUN rc-service mariadb start
#RUN rc-service postgresql start
WORKDIR /app
#RUN python3 -m venv /app/.venv
#RUN source /app/.venv/bin/activate
#RUN python3 -m ensurepip
RUN pip3 install --no-cache --upgrade pip setuptools poetry go-task-bin --break-system-packages

WORKDIR /app
COPY . /app/

#RUN poetry add poetry-plugin-export
RUN task build
#RUN poetry export -f requirements.txt --output requirements.txt
#RUN pip3 install -r /app/requirements.txt --break-system-packages

ENTRYPOINT ["poetry", "run", "python3", "/app/src/contain.py"]
CMD ["poetry", "run", "python3", "/app/src/omnisqlish/__init__.py"]
#ENTRYPOINT ["mysql"]