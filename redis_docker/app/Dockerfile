FROM python:3.7-alpine
WORKDIR /code
RUN apk update && \
    apk add --virtual build-deps gcc musl-dev
RUN apk add --no-cache gcc musl-dev linux-headers
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
EXPOSE 5000
COPY . .
ADD app.py .
ADD tasks1.py .
ADD supervisor.conf .



RUN apk update && apk add --no-cache supervisor

# default command
#CMD ["python3", "app.py"]
CMD ["supervisord", "-c", "supervisor.conf"]

