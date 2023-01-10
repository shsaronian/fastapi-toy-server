import uvicorn

from app.main.app import create_app, init_config, init_logger, init_port_number

if __name__ == '__main__':
    init_config()
    init_logger()
    app = create_app()
    uvicorn.run(app, port=init_port_number())
