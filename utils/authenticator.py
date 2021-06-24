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

REDIS_SOCKET_TIMEOUT = os.environ.get('REDIS_SOCKET_TIMEOUT')

RESOURCE_API_URL = os.environ.get('RESOURCE_API_URL')
JWT_SECRET = os.environ.get('JWT_SECRET')
TOKEN_EXPIRY_DATE = os.environ.get('TOKEN_EXPIRY_DATE')

LOGGER = logging.getLogger(__name__)

def lambda_handler(event, context):
    print('EVENT {}'.format(event))

    try:
        principalId = 'User'
        tmp = event['methodArn'].split(':')
        apiGatewayArnTmp = tmp[5].split('/')
        awsAccountId = tmp[4]

        policy = authorizer.AuthPolicy(principalId, awsAccountId)

        policy.restApiId = apiGatewayArnTmp[0]
        policy.region = tmp[3]
        policy.stage = apiGatewayArnTmp[1]
        method = apiGatewayArnTmp[2]
        auth_token = event.get('authorizationToken')
        resource = apiGatewayArnTmp[3]

        print(f'POLICY GENERATED {policy}' )

        if not auth_token:
            body = "Missing Authentication Token"

        is_valid_token = authenticator.Authentication.validate_jwt_token(auth_token)

        if is_valid_token:
            policy.allowMethod(method, resource)
        else:
            policy.denyMethod(method, resource)

        return {
            "statusCode": 200,
            "body": body,
            "isBase64Encoded": False
        }

    except Exception as e:
        LOGGER.error(e)
