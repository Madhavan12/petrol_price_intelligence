from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

# Define your Python functions
def say_hello():
    print("👋 Hello from Airflow!")

def say_goodbye():
    print("👋 Goodbye from Airflow!")

# DAG default arguments
default_args = {
    'start_date': datetime(2024, 1, 1),
    'catchup': False
}

# Define the DAG
with DAG(
    dag_id='my_first_airflow_dag',
    description='A simple DAG that says hello and goodbye',
    default_args=default_args,
    schedule_interval='@daily',
    tags=['demo'],
) as dag:

    task1 = PythonOperator(
        task_id='say_hello_task',
        python_callable=say_hello
    )

    task2 = PythonOperator(
        task_id='say_goodbye_task',
        python_callable=say_goodbye
    )

    task1 >> task2  # Set task order
