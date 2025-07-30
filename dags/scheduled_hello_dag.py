from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta

# First task
def print_message():
    print("✅ This DAG runs on a schedule!")

# Second task
def print_done():
    print("🎉 Task completed!")

default_args = {
    'start_date': datetime(2024, 1, 1),
    'retries': 3,                            # Retry up to 3 times on failure
    'retry_delay': timedelta(minutes=2),    # Wait 2 mins between retries
}

with DAG(
    dag_id='scheduled_hello_dag',
    description='DAG that runs every hour with two tasks',
    default_args=default_args,
    schedule_interval='@hourly',  # You changed this from */2 to hourly
    catchup=True,                 # Allow backfilling of missed runs
    tags=['schedule', 'retry'],
) as dag:

    task1 = PythonOperator(
        task_id='print_scheduled_message',
        python_callable=print_message
    )

    task2 = PythonOperator(
        task_id='done',
        python_callable=print_done
    )

    task1 >> task2  # Set dependency: run task2 after task1
