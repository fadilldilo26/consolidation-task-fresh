# Use official Python image as base
FROM python:3.12-slim

# Set working directory inside container
WORKDIR /app

# Copy requirements first for caching efficiency
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy rest of project files
COPY . .

# Expose Django default port
EXPOSE 8000

# Command to run server accessible externally
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]