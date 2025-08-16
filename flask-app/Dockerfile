FROM python:3.9-slim
WORKDIR /app
ADD . /app
RUN pip install --trusted-host pypi.python.org flask
EXPOSE 8080
CMD ["python", "app.py"]