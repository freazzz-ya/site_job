FROM python:3.8

WORKDIR /app

COPY requirements.txt .
RUN pip install gunicorn==20.1.0
RUN pip install -r requirements.txt --no-cache-dir

COPY . .

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "max_site.wsgi"] 
