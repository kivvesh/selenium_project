FROM jenkins/jenkins:lts

USER root

# Установка Python 3, pip и Docker
RUN apt-get update && \
    apt-get install -y python3 python3-pip docker.io && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Вернуться к пользователю Jenkins
USER jenkins