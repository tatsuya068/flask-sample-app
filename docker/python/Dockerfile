FROM python:3.10.0

WORKDIR /code

COPY requirements.txt .

RUN pip install -r requirements.txt

CMD ["gunicorn", "--bind", "0.0.0.0:5001", "wsgi:app"]