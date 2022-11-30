#


```
docker build -t app .
```

```
docker run --name app -p 8000:8000 app
```

```
gunicorn run:app --workers 4 --worker-class uvicorn.workers.UvicornWorker
```


## Results
Requests take about 900-1000ms for 3.3MB payloads
1. Using FastAPI + uvicorn is slower than Flask
