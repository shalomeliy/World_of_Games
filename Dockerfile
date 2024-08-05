# Use the official Python image from the Docker Hub
FROM python:alpine

# Set the working directory in the container
WORKDIR /app

# Run flask library
RUN python3 -m pip install --upgrade pip
RUN python3 -m pip install --upgrade selenium webdriver-manager
RUN python3 -m pip install --upgrade webdriver-manager


# Copy all Python files from the current directory to the container
COPY *.py /app

# External port
EXPOSE 8777

# Specify the command to run on container start
CMD ["python", "./main_score.py"]

