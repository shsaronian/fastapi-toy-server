import pytest


@pytest.mark.endtoend
def test_hello_without_name(client):
    response = client.get('/api/endpoints/hello')
    assert response.status_code == 200
    assert response.content.decode("utf-8") == 'Hello Stranger'


@pytest.mark.endtoend
@pytest.mark.parametrize('name, expected',
                         [('Sharon Saronian', 'Sharon Saronian')])
def test_hello_with_name(client, name: str, expected: str):
    response = client.get('/api/endpoints/hello?name=' + name)
    assert response.status_code == 200
    assert response.content.decode("utf-8") == 'Hello ' + expected


@pytest.mark.endtoend
def test_author(client):
    response = client.get('/api/endpoints/author')
    assert response.status_code == 200
    assert response.content.decode("utf-8") == 'Sharon Saronian'
