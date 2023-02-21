from typing import Union

from fastapi import APIRouter, Query

from app.main.helper.logger.logger import Logger
from starlette.responses import PlainTextResponse

router = APIRouter()
logger: Logger = Logger.get_logger(__name__)


@router.get('/hello',
            summary='Hello Endpoints',
            response_class=PlainTextResponse,
            description="Whenever a request to this endpoint is made, the service returns the string <Hello {user's name}>. If a name is not provided, a fixed string is returned.")
async def hello(name: Union[None, str] = Query(default=None, description="Return greeting string based on user's name")):
    response = f"Hello {name}" if name is not None else "Hello Stranger"
    status_code = 200
    logger.info(f"Response: {response} sent to client with status code {status_code}")
    return response

@router.get('/author',
            summary='Author Endpoint',
            response_class=PlainTextResponse,
            description="This endpoint returns the author of this server.")
async def author():
    response = "Sharon Saronian"
    status_code = 200
    logger.info(f"Response: {response} sent to client with status code {status_code}")
    return response

