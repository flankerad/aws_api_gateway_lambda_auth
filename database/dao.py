import sys
import os
import logging
# from database.connections import get_postgres_conn as psql
from database.connections import get_redis_conn as redis


LOGGER = logging.getLogger(__name__)


def save(uid, token):
    print('SAVING..', uid)
    redis.hset('uid', 'token', token)

    # with psql.cursor() as cur:
    #     cur.execute('insert into jwt_token (token_id, token) values({}, {})'.format(uid, token))
    # psql.commit()

def get(uid):
    return redis.hget('uid', 'token')
