# importing the required libraries
from datetime import timedelta, datetime
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.operators.bash_operator import BashOperator



default_args = {
    'owner': 'datateam',
    'depends_on_past': False,
    'start_date': datetime(2022,1,1),
    'email': ['data@psicologia'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=1)
}


# define the DAG
dag = DAG(
    'actividad_1',
    default_args=default_args,
    description='Actividad semana 1 Reto Summer 2022',
    schedule_interval=timedelta(hours=1), # run every hour
    catchup=False # do not perform a backfill of missing runs
)


bash1 = BashOperator(
    task_id='bash1',
    bash_command='python3 /home/matiolo/airflow/dags/extract_users_to_staging.py',
    dag=dag
)

# bash1