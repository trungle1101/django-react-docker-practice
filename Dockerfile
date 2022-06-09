FROM python:3.8-slim-buster

EXPOSE 8000
# Below added to project docker file
RUN apt-get update && apt-get install wkhtmltopdf -y
RUN apt-get install poppler-utils -y

ADD /requirements.txt /project/
WORKDIR /project
RUN pip install -r /project/requirements.txt

CMD python ./admin/manage.py runserver 0.0.0.0:8000