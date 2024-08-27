import json
from jose import jwt
from urllib.request import urlopen
from django.conf import settings
from rest_framework import authentication, exceptions

class Auth0JSONWebTokenAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        auth = request.headers.get('Authorization', None)
        if not auth:
            return None

        parts = auth.split()

        if parts[0].lower() != 'bearer':
            raise exceptions.AuthenticationFailed('Authorization header must start with Bearer')
        elif len(parts) == 1:
            raise exceptions.AuthenticationFailed('Token not found')
        elif len(parts) > 2:
            raise exceptions.AuthenticationFailed('Authorization header must be Bearer token')

        token = parts[1]
        try:
            payload = self.decode_jwt(token)
        except jwt.ExpiredSignatureError:
            raise exceptions.AuthenticationFailed('token is expired')
        except jwt.JWTClaimsError:
            raise exceptions.AuthenticationFailed('incorrect claims, please check the audience and issuer')
        except Exception:
            raise exceptions.AuthenticationFailed('Unable to parse authentication token.')

        return (payload, token)

    def decode_jwt(self, token):
        header = jwt.get_unverified_header(token)
        rsa_key = {}
        jsonurl = urlopen(f"https://{settings.AUTH0_DOMAIN}/.well-known/jwks.json")
        jwks = json.loads(jsonurl.read())
        for key in jwks['keys']:
            if key['kid'] == header['kid']:
                rsa_key = {
                    'kty': key['kty'],
                    'kid': key['kid'],
                    'use': key['use'],
                    'n': key['n'],
                    'e': key['e']
                }
        if rsa_key:
            return jwt.decode(
                token,
                rsa_key,
                algorithms=['RS256'],
                audience=settings.AUTH0_CLIENT_ID,
                issuer=f"https://{settings.AUTH0_DOMAIN}/"
            )
        raise exceptions.AuthenticationFailed('Unable to find appropriate key')

