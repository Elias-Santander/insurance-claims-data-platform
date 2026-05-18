from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta


default_args = {
    "owner": "data-engineering",
    "depends_on_past": False,
    "retries": 2,
    "retry_delay": timedelta(minutes=2)
}

with DAG(
    dag_id="insurance_claims_pipeline",
    default_args=default_args,
    description="Insurance Claims ETL Pipeline",
    schedule="@daily",
    start_date=datetime(2025, 1, 1),
    catchup=False,
    tags=["insurance", "etl", "dbt"]
) as dag:

    # ==================================================
    # ETL PIPELINE
    # ==================================================

    run_etl = BashOperator(
        task_id="run_etl",
        bash_command="cd /opt/airflow && python -m etl.main",
        sla=timedelta(minutes=10)
    )

    # ==================================================
    # DBT RUN
    # ==================================================

    run_dbt = BashOperator(
        task_id="run_dbt",
        bash_command="""
        cd /opt/airflow/dbt/insurance_claims_dbt &&
        dbt run
        """
    )

    # ==================================================
    # DBT TEST
    # ==================================================

    test_dbt = BashOperator(
        task_id="test_dbt",
        bash_command="""
        cd /opt/airflow/dbt/insurance_claims_dbt &&
        dbt test
        """
    )

    # ==================================================
    # PIPELINE FLOW
    # ==================================================

    run_etl >> run_dbt >> test_dbt