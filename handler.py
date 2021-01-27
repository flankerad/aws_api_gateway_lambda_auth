import sys
import os
import json
import logging
import datetime
import secrets

sys.path.append(os.path.join(os.path.dirname(__file__), "libs"))

import jwt
import requests
import redis
import json

from utils import authorizer, authenticator

REDIS_URI = os.environ.get('REDIS_URI')
REDIS_PORT = os.environ.get('REDIS_PORT')
REDIS_DB = os.environ.get('REDIS_DB')
REDIS_SOCKET_TIMEOUT = os.environ.get('REDIS_SOCKET_TIMEOUT')

RESOURCE_API_URL = os.environ.get('RESOURCE_API_URL')
JWT_SECRET = os.environ.get('JWT_SECRET')
TOKEN_EXPIRY_DATE = os.environ.get('TOKEN_EXPIRY_DATE')

LOGGER = logging.getLogger(__name__)

def lambda_handler(event, context):
    LOGGER.debug('EVENT {}'.format(event))

    try:

        principalId = event['requestContext']['accountId']

        tmp = event['methodArn'].split(':')
        apiGatewayArnTmp = tmp[5].split('/')
        awsAccountId = tmp[4]

        policy = authorizer.AuthPolicy(principalId, awsAccountId)
        policy.restApiId = apiGatewayArnTmp[0]
        policy.region = tmp[3]
        policy.stage = apiGatewayArnTmp[1]

        LOGGER.info(f'POLICY GENERATED')
        auth_token = {k.lower(): v for k, v in event['headers'].items() if k.lower() == 'authorization'}

        is_valid_token = authenticator.Authentication.validate_jwt_token(auth_token)


        if is_valid_token:
            policy.allowMethod(event['requestContext']['httpMethod'], event['path'])
        else:
            policy.denyMethod(event['requestContext']['httpMethod'], event['path'])


    except Exception as e:
        LOGGER.error(e)
