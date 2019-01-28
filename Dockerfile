FROM python:3
LABEL maintainer="radoslaw.lisowski@schibsted.com"

RUN pip3 install flask

WORKDIR /app
COPY app.py /app

EXPOSE 5000

CMD ["python", "app.py"]
