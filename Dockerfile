FROM python:3.11-slim

# Установка необходимых зависимостей
RUN apt-get update && apt-get install -y \
    wget \
    unzip \
    xvfb \
    libnss3 \
    libgconf-2-4 \
    libxi6 \
    libxcomposite1 \
    libasound2 \
    libxrandr2 \
    libxss1 \
    libxtst6 \
    fonts-liberation \
    gnupg && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Добавление ключа и репозитория для Google Chrome
RUN wget -q -O - https://dl.google.com/linux/linux_signing_key.pub | gpg --dearmor > /etc/apt/trusted.gpg.d/google-chrome.gpg && \
    echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" > /etc/apt/sources.list.d/google-chrome.list

# Установка Google Chrome
RUN apt-get update && apt-get install -y google-chrome-stable && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Копирование файла зависимостей
COPY requirements.txt .

# Установка Python-зависимостей
RUN pip install --no-cache-dir --upgrade pip && pip install --no-cache-dir -r requirements.txt

# Копирование проекта и установка рабочей директории
COPY . /pytest_app
WORKDIR /pytest_app

# Установка точки входа
ENTRYPOINT ["pytest"]
