FROM python:3.11

WORKDIR /app
ENV PYTHONUNBUFFERED = 1
COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000
CMD ["python3","manage.py","runserver"]