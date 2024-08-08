# Use the official Python image from the Docker Hub
FROM python:3.12-alpine

# Install flask
RUN pip install flask

# Copy all Python files from the current directory to the container
COPY *.py .

# External port
EXPOSE 8777

# Specify the command to run on container start
CMD python main_score.py
