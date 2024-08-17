# Use the official Python image from the Docker Hub
FROM python:3.12-alpine

# Set the working directory in the container
WORKDIR /app

# Copy Python and requirements files from the current directory to the container /app folder
COPY *.py .
COPY requirements.txt .

# Install flask
RUN pip install flask

# Install the dependencies specified in the requirements file
RUN pip install --no-cache-dir -r requirements.txt

# External port
EXPOSE 8777

# Specify the command to run on container start
CMD python main_score.py
