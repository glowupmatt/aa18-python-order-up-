FROM python:3.9.6

WORKDIR /app

COPY requirements.txt /app/

RUN pip install --upgrade pip

RUN pip install -r requirements.txt

WORKDIR /app

COPY . /app/

COPY init_db.sh /app/

EXPOSE 5000

ENTRYPOINT ["/app/init_db.sh"]
CMD ["flask", "run", "--host=0.0.0.0"]