import uvicorn

from app.main.app import create_app, init_config, init_logger

if __name__ == '__main__':
    init_config()
    init_logger()
    app = create_app()
    uvicorn.run(app, port=5000)
