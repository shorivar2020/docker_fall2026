
FROM python:3.12-slim

WORKDIR /app

COPY myow_v2.py .

EXPOSE 8080

CMD ["python", "-u", "myow_v2.py"]
