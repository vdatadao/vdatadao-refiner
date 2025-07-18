FROM python:3.12-slim

WORKDIR /app

COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# API server olarak çalıştır
CMD ["python", "-m", "refiner.api_server"]
