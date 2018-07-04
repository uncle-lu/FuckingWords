FROM daocloud.io/library/ubuntu:12.10
ADD . /code
WORKDIR /code
RUN pip3 install -r requirements.txt
CMD [ "python", "./run.py" ]