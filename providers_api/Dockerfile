FROM python:3.7-slim-buster

WORKDIR /root/providers_api/

# Install system dependencies
RUN mkdir -p /root/.ssh && \
    apt-get update -yqq && \
    apt-get install -yqq --no-install-recommends \
    apt-utils \
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
    && apt install --assume-yes libx11-xcb1 libasound2 x11-apps libice6 libsm6 libxaw7 libxft2 libxmu6 libxpm4 libxt6 x11-apps xbitmaps

RUN echo "deb [signed-by=/usr/share/keyrings/cloud.google.gpg] http://packages.cloud.google.com/apt cloud-sdk main" | tee -a /etc/apt/sources.list.d/google-cloud-sdk.list && curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | apt-key --keyring /usr/share/keyrings/cloud.google.gpg  add - && apt-get update -y && apt-get install google-cloud-sdk -y

# Upgrade pip
RUN python -m pip install --upgrade pip

# Install Python dependencies from requirements.txt
COPY ./requirements.txt /tmp/provider-api/requirements.txt
RUN cd /tmp/provider-api && pip install -r requirements.txt

RUN cd /root/providers_api/

ENTRYPOINT ["python", "app.py"]
