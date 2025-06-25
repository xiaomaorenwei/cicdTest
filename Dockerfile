FROM scratch
COPY ./venv /venv
COPY ./app /app

ENV PATH="/venv/bin:$PATH"
WORKDIR /app

CMD ["python", "main.py"]
