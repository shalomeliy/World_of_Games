# Use the official Python image from the Docker Hub
FROM python:3.12-alpine

# Set the working directory in the container
WORKDIR /app

# Install flask
RUN pip install flask

# Install Chromium and ChromeDriver
RUN apk add --no-cache \
    chromium \
    chromium-chromedriver

# Install pip and necessary Python packages
RUN python3 -m pip install --upgrade pip selenium

# Set environment variables for Chromium
ENV CHROME_BIN=/usr/lib/chromium/chrome
ENV CHROME_DRIVER=/usr/lib/chromium/chromedriver

# Copy all Python files from the current directory to the container
COPY *.py /app

# External port
EXPOSE 8777

# Specify the command to run on container start
CMD python ./app/main_score.py
