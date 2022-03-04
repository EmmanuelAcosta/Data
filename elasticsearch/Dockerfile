FROM node:16-buster-slim

WORKDIR /root/ui/

# Install system dependencies
RUN apt-get update -yqq && \
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

RUN cd /root/ui/

RUN sleep 10

RUN yarn add next

RUN yarn add axios

RUN yarn add firebase

RUN yarn add flat

RUN yarn add react-google-button

RUN yarn install

RUN sleep 10

CMD yarn start
