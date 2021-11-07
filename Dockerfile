#FROM ubuntu:latest
FROM ubuntu:20.04
MAINTAINER jeongwook_lee "rightlit@gmail.com"

#RUN apt-get update -y
RUN apt-get update -y && apt-get upgrade -y

#RUN apt-get install -y python-pip python-dev build-essential
RUN apt-get install -y python3 python3-pip python3-dev build-essential
RUN ln -s /usr/bin/python3 /usr/bin/python
#RUN ln -s /usr/bin/pip3 /usr/bin/pip

COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["run_task_all.py"]