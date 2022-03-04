#!/usr/bin/env bash

# Install the project
pip install -e ./tap

# Initialize a new secret key if one isn't provided
: "${SECRET_KEY:=$(openssl rand -hex 30)}"
export FERNET_KEY

# Initialize a new fernet key if one isn't provided
: "${FERNET_KEY:=$(python -c "from cryptography.fernet import Fernet; FERNET_KEY = Fernet.generate_key().decode(); print(FERNET_KEY)")}}"
export SECRET_KEY

# Link Airflow dags directory to tap dags directory
ln -s -T /root/tap/tap/airflow/dags /root/airflow/dags

# Wrap the airflow commands to initialize the Airflow database and launch the Airflow webserver
case "$1" in
  webserver)
    airflow initdb
    exec airflow webserver
    ;;
  scheduler)
    # Give the webserver time to run initdb.
    sleep 15
    exec airflow "$@"
    ;;
  *)
    exec "$@"
    ;;
esac
