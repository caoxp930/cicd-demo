dockerfile入
FROM python:3.9-slim
#Install git tool
RUN apt-get update && apt-get install-y git && rm -rf /var/lib/apt/lists/*
WORKDIR /app
COPY..
RUN pip install flask
EXPOSE 5000
CMD「"python","app.py"]