FROM python:3.9

WORKDIR /usr/src/app

ENV PORT 8080

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY . /usr/src/app

CMD [ "python", "./Server.py"]
CMD [ "python", "./request.py"]