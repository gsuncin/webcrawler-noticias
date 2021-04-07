FROM python:3.9.4-slim-buster

# Copy your application code to the container (make sure you create a .dockerignore file if any large files or directories should be excluded)
COPY . /code/webcrawler
WORKDIR /code/webcrawler
RUN apt-get update && pip install -r requirements.txt

# uWSGI will listen on this port
EXPOSE 8080

# Add any static environment variables needed by Django or your settings file here:
ENV DJANGO_SETTINGS_MODULE=core.settings

# Call collectstatic (customize the following line with the minimal environment variables needed for manage.py to run):
#RUN DATABASE_URL='' python manage.py collectstatic --noinput
RUN mkdir -p /code/webcrawler/static

#
CMD ["python", "manage.py", "runserver", "0.0.0.0:8080"]