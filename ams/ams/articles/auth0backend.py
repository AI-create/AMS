import json
import requests
from jose import jwt
from django.conf import settings
from django.contrib.auth.models import User
from rest_framework_jwt.authentication import BaseJSONWebTokenAuthentication

class Auth0JSONWebTokenAuthentication(BaseJSONWebTokenAuthentication):
    def decode_handler(self, token):
        header = jwt.get_unverified_header(token)
        rsa_key = {}
        jwks = requests.get(f'https://{settings.AUTH0_DOMAIN}/.well-known/jwks.json').json()
        for key in jwks['keys']:
            if key['kid'] == header['kid']:
                rsa_key = {
                    'kty': key['kty'],
                    'kid': key['kid'],
                    'use': key['use'],
                    'n': key['n'],
                    'e': key['e']
                }
        return jwt.decode(
            token,
            rsa_key,
            algorithms=['RS256'],
            audience=settings.AUTH0_CLIENT_ID,
            issuer=f'https://{settings.AUTH0_DOMAIN}/'
        )

    def authenticate(self, request):
        auth = request.headers.get('Authorization', None)
        if auth:
            parts = auth.split()

            if parts[0].lower() != 'bearer':
                return None
            elif len(parts) == 1:
                return None
            elif len(parts) > 2:
                return None

            token = parts[1]
            try:
                payload = self.decode_handler(token)
                user, _ = User.objects.get_or_create(username=payload['sub'])
                return (user, token)
            except jwt.ExpiredSignatureError:
                return None
            except jwt.JWTClaimsError:
                return None
            except Exception:
                return None
        return None
