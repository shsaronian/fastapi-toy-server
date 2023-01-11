from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware, RequestResponseEndpoint
from starlette.responses import Response

from app.main.helper.config.config import Config
from app.main.helper.logger.logger import Logger
from app.main.util.network_util import NetworkUtil
from app.main.util.request_id_generator import RequestIdGenerator
from app.main.util.request_vars import g

USE_XFF_IP = Config.get('General.useXFFIP')
logger: Logger = Logger.get_logger(__name__)


class BeforeAppRequest(BaseHTTPMiddleware):

    async def dispatch(self, request: Request, call_next: RequestResponseEndpoint) -> Response:
        request_id = RequestIdGenerator.generate()
        g.set(request_id)
        client_ip = NetworkUtil.get_client_ip(USE_XFF_IP, request)
        if client_ip is None:
            logger.warning(f"USE_XFF_IP config is True, but X-FORWARDED-FOR header is not set")
            client_ip = ""

        log_message = f"Client {client_ip} has requested {request.url} with method {request.method}"
        if request.url.path.replace('/', '') == 'health':
            logger.debug(log_message)
        else:
            logger.info(log_message)
        response = await call_next(request)
        return response
