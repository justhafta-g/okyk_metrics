# Use the official image python from dockerhub
FROM python:3

MAINTAINER Oleksandr Kyktenko <o.kyktenko@ukr.net>

# Set the working directory
WORKDIR /usr/src/app

# Copy the current directory contents into the container
COPY dependencies.txt .
COPY sys_metrics.py /usr/src/app

# Install any needed dependencies 
RUN pip3 install --trusted-host pypi.python.org -r dependencies.txt

# Define environment variable
ENTRYPOINT ["python", "sys_metrics.py"]
