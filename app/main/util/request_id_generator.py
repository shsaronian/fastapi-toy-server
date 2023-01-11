import random
import string


class RequestIdGenerator:

    @staticmethod
    def generate() -> str:
        return 'FASTAPI_TOY_SERVER-' + ''.join(random.choices(string.ascii_uppercase + string.digits + string.ascii_lowercase, k=8))
