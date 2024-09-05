FROM nginx:latest
COPY index.html /usr/share/nginx/html/
COPY 1.jpg /usr/share/nginx/html/
RUN apt-get update && apt-get install -y nginx
COPY nginx.conf /etc/nginx/conf.d/default.conf

FROM python:3.12-slim
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY app.py /app/app.py
WORKDIR /app
CMD ["python", "app.py"]
EXPOSE 3478