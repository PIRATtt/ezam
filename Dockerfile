FROM python:3
WORKDIR .
COPY . .
RUN pip install flask && pip install flask-login && pip install pysqlite3
CMD ["python3", "app.py"]