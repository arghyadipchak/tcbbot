FROM python:3.8.6

RUN apt update && apt upgrade -y

RUN ln -fs /usr/share/zoneinfo/Asia/Kolkata /etc/localtime
ENV DEBIAN_FRONTEND noninteractive
RUN dpkg-reconfigure --frontend noninteractive tzdata

RUN apt -y install supervisor nano
COPY configs/supervisor.conf /etc/supervisor.conf

WORKDIR /home
ENV APP /home/bot

COPY requirements.txt .
RUN pip install -r requirements.txt
RUN rm requirements.txt

COPY bot $APP

CMD ["supervisord", "-c", "/etc/supervisor.conf"]