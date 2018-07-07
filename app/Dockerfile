FROM ubuntu
ADD ./FW FW
ADD ./run.py run.py
RUN apt-get update
RUN apt-get install -y wkhtmltopdf
RUN pip3 install -r requirements.txt
CMD [ "python3", "./run.py" ]