# Dockerfile - this is a comment. Delete me if you want.
# Su WinZoz con Docker toolbox si deve accedere a questo indirizzo http://192.168.99.100:5000
FROM python:3.7
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
RUN chmod 644 run.py
ENTRYPOINT ["python"]
CMD ["run.py"]