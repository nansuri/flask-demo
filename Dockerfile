FROM tiangolo/uwsgi-nginx-flask:python3.7

COPY ./app /app

docker run -d --name flask-mini -p 80:80 -v $(pwd)/app:/app myimage
