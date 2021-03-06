import os
import sys
import logging

sys.path.append(os.path.join(os.path.dirname(__file__), "libs"))

# from  psycopg2
import redis


PSQL_RDS_HOST = os.environ.get('PSQL_RDS_HOST')
PSQL_RDS_PORT = os.environ.get('PSQL_RDS_PORT')
PSQL_RDS_DBNAME = os.environ.get('PSQL_RDS_DBNAME')
PSQL_RDS_USER = os.environ.get('PSQL_RDS_USERNAME')
PSQL_RDS_PASSWORD = os.environ.get('PSQL_RDS_PASSWORD')

REDIS_HOST= os.environ.get('REDIS_HOST', 'localhost')
REDIS_PORT = os.environ.get('REDIS_PORT', 6379)
REDIS_DB = os.environ.get('REDIS_DB', 0)
REDIS_SOCKET_TIMEOUT = os.environ.get('REDIS_SOCKET_TIMEOUT')

logger = logging.getLogger()
logger.setLevel(logging.INFO)


# def get_postgres_conn():
#     try:
#         psql_conn = psycopg2.connect("dbname={} user={} host={} password={}".
#                 format(PSQL_RDS_DBNAME, PSQL_RDS_USER, PSQL_RDS_HOST, PSQL_RDS_PASSWORD))

#         print("SUCCESS: Connection to RDS Postgres SQL instance succeeded")

#         return psql_conn

#     except Exception as e:

#         logger.error("ERROR: Unexpected error: Could not connect to Postgres SQL instance.")
#         logger.error(e)
#         print(e)
#         sys.exit()


def get_redis_conn():
    try:
        redis_conn = redis.Redis(
                        host=REDIS_HOST,
                        port=REDIS_PORT,
                        db=REDIS_DB,
                        password='')

        print("SUCCESS: Connection to REDIS instance succeeded")

        return redis_conn

    except Exception as e:

        logger.error("ERROR: Unexpected error: Could not connect to Redis instance.")
        logger.error(e)
        print(e)
        sys.exit()


