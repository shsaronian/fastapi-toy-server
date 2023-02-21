import re
import pytest

from app.main.util.request_id_generator import RequestIdGenerator


class TestRequestIdGenerator:
    @staticmethod
    @pytest.mark.unit
    def test_generate():
        request_id = RequestIdGenerator.generate()
        assert len(request_id) == 27
        assert re.findall('\AFASTAPI_TOY_SERVER-\w+', request_id)
