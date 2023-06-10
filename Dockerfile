# pull the official base image
FROM pytorch/pytorch:latest
    
# set work directory
WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV DEBIAN_FRONTEND=noninteractive 

# packages linux---

RUN apt-get update && apt-get -y install python3
RUN apt-get -y install python3-pip
RUN pip3 install --upgrade pip



# Libraries or Dependencies -- 
COPY /requirements.txt /usr/src/app
RUN pip install -r requirements.txt
COPY /. /usr/src/app
RUN apt install -y git
RUN git clone https://github.com/suno-ai/bark
RUN cd bark && pip3 install . 

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]