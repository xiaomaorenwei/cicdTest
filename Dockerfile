# 使用官方 Python 镜像作为基础环境
FROM swr.cn-north-4.myhuaweicloud.com/ddn-k8s/docker.io/python:3.11-slim

# 设置工作目录
WORKDIR /app

# 复制依赖文件并安装
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 复制项目代码（包括 web_app.py 等）
COPY . .

# 开放 Flask 默认端口
EXPOSE 5000

# 设置 Flask 启动入口（假设你的 web_app.py 启动 Flask 应用）
CMD ["python", "web_app.py"]
