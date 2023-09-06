# Pull base image
FROM python:3.9
# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
# Set work directory
# WORKDIR /chachacode
# Install dependencies
# COPY Pipfile Pipfile.lock /chachacode/
# RUN pip install pipenv  && pipenv install --system
# Copy project
# COPY . /chachacode/
# set work directory
WORKDIR /opt/app 
RUN pip install --upgrade pip
COPY ./requirements.txt /opt/app/requirements.txt 
RUN chmod +x /opt/app/requirements.txt
RUN pip install -r requirements.txt
# copy project
COPY . /opt/app/


# EXPOSE 80