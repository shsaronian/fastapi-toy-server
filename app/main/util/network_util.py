from fastapi import Request


class NetworkUtil:

    @staticmethod
    def get_client_ip(use_xff_ip: bool, request: Request) -> str:
        remote_address = None
        if not use_xff_ip:
            remote_address = request.client.host
        else:
            if 'X-FORWARDED-FOR' in request.headers:
                proxy_data = request.headers['X-FORWARDED-FOR']
                remote_address = proxy_data.split(',')[-1]
        return remote_address
