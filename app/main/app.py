from fastapi import FastAPI

from . import __version__

server_name = "FastAPI Toy Server"


def create_app() -> FastAPI:
    app = FastAPI(title=server_name, version=__version__, debug=True)
    return app
