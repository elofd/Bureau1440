FROM python:3.11-slim-bullseye

ENV APP_ROOT /src
COPY . ${APP_ROOT}

RUN echo "===> Install requirements..." &&  \
    python -m pip install --upgrade pip setuptools &&  \
    pip install -r ${APP_ROOT}/requirements.txt --no-input

WORKDIR ${APP_ROOT}

CMD ["python", "main.py"]
