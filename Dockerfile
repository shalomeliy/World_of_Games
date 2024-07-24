# Use the official Python image from the Docker Hub
FROM python:alpine

# Set the working directory in the container
WORKDIR /app

# Run flask library
RUN pip install flask

# Copy all Python files from the current directory to the container
COPY *.py /app

# Specify the command to run on container start
CMD ["python", "./main.py"]

