FROM python:3.7-alpine

EXPOSE 80

# Move files onto application
# RUN mkdir /usr/share/nginx/app
COPY app /usr/src

WORKDIR /usr/src

# Install dependencies
RUN pip install -r requirements.prod.txt
RUN ./setup.sh
CMD gunicorn -b 0.0.0.0:80 gamesapi.wsgi