from datetime import timedelta
from airflow import DAG
from airflow.operators.dummy_operators import DummyOperator
from datetime import datetime

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2022, 5, 11),
    'retries': 0

}

dag = DAG(dag_id='DAG_1', default_args=default_args, catchup=False, scheule_interval='@once')

start = DummyOperator(task_id='start', dag=dag)
end = DummyOperator(task_id='end', dag=dag)

start >> end