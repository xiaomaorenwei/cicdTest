FROM ubuntu:22.04

# 手动安装 python
RUN apt update && apt install -y python3 python3-pip

# 复制你本地的代码和依赖
COPY ./app /app
COPY ./venv /venv

WORKDIR /app
ENV PATH="/venv/bin:$PATH"

CMD ["python3", "main.py"]
