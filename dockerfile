# Use the official Python image from the Docker Hub
FROM python:3.12

# Set the working directory in the container
WORKDIR /app

# Copy all Python files from the current directory to the container
COPY *.py /app

# Specify the command to run on container start
CMD ["python", "./main.py"]

