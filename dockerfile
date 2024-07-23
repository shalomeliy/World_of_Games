FROM python:3.12
WORKDIR /app
COPY *.py /app
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 80
ENV 
CMD [ "python", "./main.py" ]
