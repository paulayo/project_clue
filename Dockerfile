# The first instruction is what image we want to base our container on
# We Use an official Python runtime as a parent image
FROM python:3

# The enviroment variable ensures that the python output is set straight
# to the terminal with out buffering it first
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

# create root directory for our project in the container
RUN mkdir ./web

# Set the working directory to /web
WORKDIR ./web

# Copy the current directory contents into the container at /web
ADD . /web/

# Install any needed packages specified in requirements.txt
FROM kennethreitz/pipenv as pipenv

RUN pip install --upgrade pip
RUN pipenv install --dev \
 && pipenv lock -r > requirements.txt

COPY . .

CMD ["python","manage.py runserver"]