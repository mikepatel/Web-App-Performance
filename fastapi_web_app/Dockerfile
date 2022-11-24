FROM python:3

COPY requirements.txt requirements.txt
COPY run.py run.py

RUN python -m pip install -r requirements.txt

EXPOSE 8000

CMD ["gunicorn",  "run:app", "--bind=0.0.0.0:8000", "--workers=10", "--worker-class=uvicorn.workers.UvicornWorker"]
