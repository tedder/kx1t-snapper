FROM debian:stable-slim
ENV PYTHONUNBUFFERED=1
ENV DEBIAN_FRONTEND=noninteractive

RUN apt update && apt install -y python3-selenium chromium chromium-driver python3-pip vim
COPY requirements.txt /opt/app/
RUN pip3 install -r /opt/app/requirements.txt

COPY *.py /opt/app/

WORKDIR /opt/app/
CMD /opt/app/snap.py

