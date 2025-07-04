# Use lightweight Python image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy requirements and install dependencies
COPY app/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application files
COPY app/ .

# Expose port and define the startup command
EXPOSE 5000
CMD ["gunicorn", "-b", "0.0.0.0:5000", "main:app"]
