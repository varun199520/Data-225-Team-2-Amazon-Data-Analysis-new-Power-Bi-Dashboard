
from datetime import timedelta


from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.providers.amazon.aws.operators.glue import GlueJobOperator
from airflow.utils.dates import days_ago
from Live_data_ETL import fetch_and_save_deals



default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': days_ago(2),
    'email': ['airflow@example.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}


region_name='us-east-1' #Refer to Image below
glue_job_name='ETL-Deals'  #Refer to Image below



dag = DAG(
    'LIVE_DATA_ETL',
    default_args=default_args,
    description='ETL for Live data.',
    schedule_interval=timedelta(days=1),
)


t1 = PythonOperator(
    task_id='FETCHING_AND_STORING_IN_S3',
    python_callable=fetch_and_save_deals,
    dag=dag,
)


start_glue_job = GlueJobOperator(
        task_id = "ETL_FROM_S3_TO_REDSHIFT",
        job_name = glue_job_name,
        job_desc = "ETL from S3 to Redshift",
        region_name = region_name,
        script_location = "s3://aws-glue-assets-533267125994-us-east-1/scripts/ETL-Deals.py",
        s3_bucket = "aws-glue-assets-533267125994-us-east-1",
        iam_role_name = "Glue-IAM-Project",
        num_of_dpus = 10,
        create_job_kwargs={"GlueVersion": "4.0", "NumberOfWorkers": 2, "WorkerType": "G.1X"},
        dag = dag
        )



t1 >> start_glue_job 