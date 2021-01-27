import logging
import secrets
import datetime
import traceback

from database.connections import redis

LOGGER = logging.getLogger(__name__)


class Authentication:
    def __init__(self):
        self._name = 'Authentication'

    def generate_jwt_access_token(payload):
        secret = secrets.token_urlsafe(20)
        jwt_auth_token = jwt.encode({'username': payload.get('username'),
                            'merchant_name': payload.get('merchant_name'),
                            'uid': payload.get('uuid'),
                            'merchant_id': payload.get('merchant_id'),
                            'exp': datetime.datetime.utcnow() + datetime.timedelta(days=TOKEN_EXPIRY_DATE),
                            'iat': datetime.datetime.utcnow(),
                            secret,
                            algorithm='HS256')


    def validate_jwt_token(jwt_auth_token):
        try:
            return jwt.decode(encoded, key, algorithms="HS256")

        except expression as identifier:
            pass


    def get_auth_token_from_refresh_token(jwt_auth_token):
        try:
            payload = jwt.decode(encoded, key, algorithms="HS256")
            payload['exp'] = datetime.datetime.utcnow() + datetime.timedelta(days=TOKEN_EXPIRY_DATE)}
            jwt_auth_token = generate_jwt_access_token(payload)

        except expression as identifier:
            pass

        return jwt_auth_token