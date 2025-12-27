FROM python:3.12

# Set working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# Run the web service on container startup
# Note: $PORT is an environment variable set by Cloud Run
CMD uvicorn main:app --host 0.0.0.0 --port 8080