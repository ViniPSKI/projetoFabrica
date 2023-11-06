FROM python:3.8

WORKDIR /hc-team-composition/API/api_times

COPY requirements.txt /hc-team-composition/API/api_times/

RUN pip install -r requirements.txt

COPY /hc-team-composition /hc-team-composition

ENV DEBUG=True
ENV SECRET_KEY=mysecretkey

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
