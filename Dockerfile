# Use the official Python image from the Docker Hub
FROM python:3.12-alpine

# Set the working directory in the container
WORKDIR /app

# Upgrade pip and install necessary libraries
RUN python3 -m pip install --upgrade pip \
    && python3 -m pip install selenium webdriver-manager \
    && apk add --no-cache chromium chromium-chromedriver

# Set environment variables for Chromium
ENV CHROME_BIN=/usr/bin/chromium-browser
ENV CHROME_DRIVER=/usr/bin/chromedriver

# Copy all Python files from the current directory to the container
COPY *.py /app

# External port
EXPOSE 8777

# Specify the command to run on container start
CMD ["python", "./main_score.py"]
