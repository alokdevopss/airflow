from airflow import DAG
from datetime import datetime, timedelta
from airflow.contrib.operators.kubernetes_pod_operator import KubernetesPodOperator
from airflow.operators.dummy_operator import DummyOperator

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime.utcnow(),
#     'email': ['airflow@example.com'],
#     'email_on_failure': False,
#     'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5)
}

# dag = DAG('kubernetes_hello_world1', default_args=default_args, schedule_interval=timedelta(minutes=10))
dag = DAG(dag_id='DAG_1', default_args=default_args, catchup=False, scheule_interval='@once')


start = DummyOperator(task_id='start', dag=dag)



# failing = KubernetesPodOperator(namespace='gessa-dataprocessing-dev',
#                           image="ubuntu:16.04",
#                           cmds=["python","-c"],
#                           arguments=["print('hello world')"],
#                           labels={"foo": "bar"},
#                           name="fail",
#                           task_id="failing-task",
#                           get_logs=True,
#                           dag=dag
#                           )

end = DummyOperator(task_id='end', dag=dag)



# failing.set_upstream(start)

# failing.set_downstream(end)
