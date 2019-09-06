FROM python:3.5

RUN mkdir -p /usr/src/app/

WORKDIR /usr/src/app

COPY src /usr/src/app/
COPY requirements.txt /usr/src/app/
COPY data /usr/src/app/

RUN apt-get -qqy update && apt-get install -qqy \
        curl \
        gcc \
        python-dev \
        python-setuptools \
        lsb-release \
        openssh-client

RUN pip install --no-cache-dir -r requirements.txt

# Setting Persistent data
VOLUME ["/app-data"]

CMD ["python3", "-u", "transformer.py"]