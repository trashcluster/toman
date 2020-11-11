FROM python:alpine


#RUN apt install openssl libstdc++
RUN pip install --upgrade pip
COPY ./requirements.txt ./
RUN pip install -r requirements.txt

ADD ./database.py .
ADD ./csgo.py .
ADD ./app.py .

EXPOSE 5000
ENV MONGODBURL changeme
CMD python /app.py