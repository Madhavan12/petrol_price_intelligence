from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

# Task functions
def start_pipeline():
    print("🚀 Petrol Price Pipeline Started")

def end_pipeline():
    print("✅ Pipeline Completed Successfully")

# Define the DAG
with DAG(
    dag_id='petrol_price_pipeline_v1',  # Unique identifier for the DAG
    description='Base DAG for Petrol Price Pipeline',  # Description of the DAG
    start_date=datetime(2024, 1, 1),  # Start date of the DAG
    schedule_interval='0 7 * * *',  # Runs daily at 7 AM
    catchup=False,  # Prevents backfilling of past runs
    tags=['petrol', 'phase1'],  # Custom tags to organize your DAGs
) as dag:

    # Task 1: Start Task
    start_task = PythonOperator(
        task_id='start_pipeline',  # Unique task identifier
        python_callable=start_pipeline  # Function to call
    )

    # Task 2: End Task
    end_task = PythonOperator(
        task_id='end_pipeline',
        python_callable=end_pipeline
    )

    # Define task dependencies: start first, then end
    start_task >> end_task
