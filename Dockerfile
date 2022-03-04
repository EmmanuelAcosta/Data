FROM python:3.7-slim-buster

WORKDIR /root

# Install system dependencies
RUN mkdir -p /root/.ssh && \
    apt-get update -yqq && \
    apt-get install -yqq --no-install-recommends \
    apt-utils \
    git \
    curl \
    ssh-client \
    build-essential \
    locales \
    unzip \
    less \
    gnupg2

RUN apt-get install --no-install-recommends --no-install-suggests -y \
    libgtk-3-0 \
    libdbus-glib-1-2 \
    bzip2 \
    && apt install --assume-yes libx11-xcb1 libasound2 x11-apps libice6 libsm6 libxaw7 libxft2 libxmu6 libxpm4 libxt6 x11-apps xbitmaps \
    && apt-get install wget \
    && wget https://ftp.mozilla.org/pub/firefox/releases/81.0/linux-x86_64/en-US/firefox-81.0.tar.bz2 \
    && tar -xvf firefox-81.0.tar.bz2 \
    && ln -s /app/firefox/firefox /usr/local/bin/

RUN wget https://github.com/mozilla/geckodriver/releases/download/v0.27.0/geckodriver-v0.27.0-linux64.tar.gz \
    && tar -xzf geckodriver-v0.27.0-linux64.tar.gz -C /usr/local/bin

RUN echo "deb [signed-by=/usr/share/keyrings/cloud.google.gpg] http://packages.cloud.google.com/apt cloud-sdk main" | tee -a /etc/apt/sources.list.d/google-cloud-sdk.list && curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | apt-key --keyring /usr/share/keyrings/cloud.google.gpg  add - && apt-get update -y && apt-get install google-cloud-sdk -y

# Upgrade pip
RUN python -m pip install --upgrade pip

# Install Python dependencies from requirements.txt
COPY ./requirements.txt /tmp/tap/requirements.txt
RUN cd /tmp/tap && pip install -r requirements.txt

# Add Airflow configuration and entrypoint script
# COPY ./config/airflow.cfg /root/airflow/airflow.cfg
COPY ./entrypoint.sh ./entrypoint.sh

WORKDIR /root/airflow
RUN mkdir dags
COPY dags dags/
WORKDIR /root
ENTRYPOINT ["sh", "./entrypoint.sh"]