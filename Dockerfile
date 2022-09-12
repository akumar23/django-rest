FROM python:3 

COPY requirements.txt requirements.txt
RUN pyton -m pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . .

WORKDIR /restapi