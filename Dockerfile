FROM python:3.8

WORKDIR /API/api_times

COPY requirements.txt /API/api_times/

RUN pip install -r requirements.txt

COPY /API /API

ENV DEBUG=True
ENV SECRET_KEY=mysecretkey

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
