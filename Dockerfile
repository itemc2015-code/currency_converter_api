FROM python:11-slim
COPY requirements.txt .
INSTALL pip --no-cache-dir -r requirements.txt
COPY . .
CMD ["app","app.py"]