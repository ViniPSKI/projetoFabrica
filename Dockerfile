FROM python:3.8

WORKDIR /app/API/api_times

COPY requirements.txt /app/API/api_times/

RUN pip install -r requirements.txt

COPY /app /app

ENV DEBUG=True
ENV SECRET_KEY=mysecretkey

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
