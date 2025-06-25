From python:3.10-slim

WORKDIR /app

COPY ..

RUN pip install --no-catch-dir -r requirements.txt

EXPOSE 5000

CMD ["python","web_app.py"]

