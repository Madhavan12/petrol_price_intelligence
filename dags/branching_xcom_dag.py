from airflow import DAG
from airflow.operators.python import PythonOperator, BranchPythonOperator
from airflow.operators.dummy import DummyOperator
from datetime import datetime
import random

# Task: Generate a random number
def generate_number(ti):
    num = random.randint(1, 100)
    ti.xcom_push(key='random_number', value=num)
    print(f"Generated number: {num}")

# Branching logic
def decide_branch(ti):
    num = ti.xcom_pull(key='random_number', task_ids='generate_number')
    if num % 2 == 0:
        return 'even_task'
    else:
        return 'odd_task'

# Dummy follow-up tasks
def even_message():
    print("🔵 It's an even number!")

def odd_message():
    print("🟠 It's an odd number!")

with DAG(
    dag_id='branching_xcom_dag',
    start_date=datetime(2024, 1, 1),
    schedule_interval='@daily',
    catchup=False,
    tags=['xcom', 'branching'],
) as dag:

    start = PythonOperator(
        task_id='generate_number',
        python_callable=generate_number
    )

    branch = BranchPythonOperator(
        task_id='branch_decision',
        python_callable=decide_branch
    )

    even = PythonOperator(
        task_id='even_task',
        python_callable=even_message
    )

    odd = PythonOperator(
        task_id='odd_task',
        python_callable=odd_message
    )

    end = DummyOperator(task_id='end')

    # DAG flow
    start >> branch
    branch >> [even, odd] >> end
