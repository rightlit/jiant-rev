#가져올 이미지
FROM python:3.7-alpine

# app 디렉토리 선정
#RUN mkdir /opt/app
#RUN git clone https://github.com/rightlit/jiant-rev /opt/app

#WORKDIR /opt/app
#COPY ./requirements.txt .
#COPY ./requirements-no-torch.txt .
COPY . .

#WORKDIR /opt/app/jiant-rev
RUN pip install -r requirements.txt

CMD ["run_task_all.py"]

ENTRYPOINT ["python"]