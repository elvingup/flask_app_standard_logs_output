
FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# CMD ["python", "app.py"]
CMD ["sh", "-c", "python app.py > /var/log/flask_stdout.log 2>&1"]
