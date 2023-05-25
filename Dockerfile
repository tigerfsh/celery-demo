FROM ubuntu:20.04

ENV TZ=Asia/Shanghai

RUN apt update && apt install -y python3 python3-pip
RUN pip install -i http://pypi.douban.com/simple/ --trusted-host pypi.douban.com -U "celery[redis]"

COPY app.py /app/
COPY entrypoint.sh /app/

WORKDIR /app/

# CMD ["celery" "-A", "app", "worker", "-B"]
ENTRYPOINT [ "bash", "entrypoint.sh" ]