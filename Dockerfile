# Base image (Python slim version for small size)
FROM python:3.10-slim

# Set working directory inside container
WORKDIR /app

# Copy only requirements first (better caching)
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Install awscli (if your project needs it)
RUN apt-get update -y && apt-get install -y awscli

# Copy the rest of the code
COPY . .

# Expose Flask port (good practice)
EXPOSE 5000

# Run the application
CMD ["python3", "applicacation.py"]