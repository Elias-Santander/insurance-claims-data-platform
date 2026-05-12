from sqlalchemy import create_engine
from etl.config.db_config import DB_CONFIG
from etl.utils.logger import logger


def load_to_postgres(df, table_name):
    try:
        connection_string = (
            f"postgresql://"
            f"{DB_CONFIG['user']}:"
            f"{DB_CONFIG['password']}@"
            f"{DB_CONFIG['host']}:"
            f"{DB_CONFIG['port']}/"
            f"{DB_CONFIG['database']}"
        )
        engine = create_engine(
            connection_string
        )
        logger.info(
            f"Loading data into {table_name}"
        )
        df.to_sql(
            table_name,
            engine,
            if_exists="replace",
            index=False
        )
        logger.info(
            f"Data loaded successfully into "
            f"{table_name}"
        )

    except Exception as e:
        logger.error(
            f"Error loading {table_name}: "
            f"{str(e)}"
        )
        raise