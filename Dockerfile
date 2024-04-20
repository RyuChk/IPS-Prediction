# Use a Python base image
FROM python:3.9-slim AS base

# Set the working directory in the container
WORKDIR /app

# Copy the Python dependencies file
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt
# RUN make

# Copy the source code into the container
COPY . .

# Expose the port your server runs on
EXPOSE 50051

# Command to run the server
CMD ["python", "-u", "server.py"]
