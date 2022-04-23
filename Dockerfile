# 用于后端的 Dockerfile 可视情况进行修改以适应自己的需要
# 一般使用推荐用 -e 传递参数
FROM python:3.9.8-alpine
LABEL cocoapush.image.author="Luckykeeper<https://luckykeeper.site|luckykeeper@luckykeeper.site>"
WORKDIR /usr/src/app

COPY ./CocoaServer_Docker.py ./
COPY ./run.sh ./
RUN pip install DingtalkChatbot

RUN apk --update add tzdata wget && \
    cp /usr/share/zoneinfo/Asia/Shanghai /etc/localtime && \
    echo "Asia/Shanghai" > /etc/timezone && \
    apk del tzdata && \
    rm -rf /var/cache/apk/*

# 相关环境变量
ENV debug=False CocoaServer_port='22119' py_dingpusher_token='KxA0ubjN8DMZCKrhS19uhKB2EYYnpNm60S3'
EXPOSE 22119/udp
ENTRYPOINT /bin/sh /usr/src/app/run.sh ${debug} ${webhook_url} ${token} ${CocoaServer_port} ${py_dingpusher_token}