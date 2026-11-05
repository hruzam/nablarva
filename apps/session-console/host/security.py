"""One authenticated, exact-origin boundary for static, API, file and WS routes."""
import base64
import hmac
from urllib.parse import urlsplit

from aiohttp import web


class APIError(Exception):
    def __init__(self, status, code, message):
        self.status, self.code, self.message = status, code, message


def security_middleware(credential, origin):
    parsed = urlsplit(origin)
    if (parsed.scheme not in {'http', 'https'} or not parsed.netloc or
            parsed.path or parsed.query or parsed.fragment or parsed.username):
        raise ValueError('origin must be an exact http(s) scheme://host:port')
    expected_auth = 'Basic ' + base64.b64encode(credential.encode()).decode()

    @web.middleware
    async def boundary(request, handler):
        try:
            if len(request.headers.getall('Host', [])) != 1 or request.host != parsed.netloc:
                raise APIError(403, 'host', 'Unexpected Host')
            supplied = request.headers.get('Authorization', '')
            if not hmac.compare_digest(supplied.encode(), expected_auth.encode()):
                return web.json_response({'error': {'code': 'auth', 'message': 'Authentication required'}},
                    status=401, headers={'WWW-Authenticate': 'Basic realm="session-console"',
                                         'Cache-Control': 'no-store'})
            origins = request.headers.getall('Origin', [])
            mutating = request.method not in {'GET', 'HEAD'}
            websocket = request.headers.get('Upgrade', '').lower() == 'websocket'
            if (origins and origins != [origin]) or ((mutating or websocket) and origins != [origin]):
                raise APIError(403, 'origin', 'Exact configured Origin required')
            if mutating and request.headers.get('X-Console-Action') != '1':
                raise APIError(403, 'csrf', 'Explicit console action required')
            response = await handler(request)
            if not response.prepared:
                response.headers['Cache-Control'] = 'no-store'
                response.headers['X-Content-Type-Options'] = 'nosniff'
            return response
        except APIError as error:
            return web.json_response({'error': {'code': error.code, 'message': error.message}},
                                     status=error.status, headers={'Cache-Control': 'no-store'})
        except web.HTTPException as error:
            return web.json_response({'error': {'code': 'http', 'message': error.reason}},
                                     status=error.status, headers={'Cache-Control': 'no-store'})
        except (ValueError, KeyError, TypeError):
            return web.json_response({'error': {'code': 'invalid', 'message': 'Invalid request'}}, status=400)
    return boundary
