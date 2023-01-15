import json
import pytest
from graphene_file_upload.django.testing import file_graphql_query


@pytest.fixture
def client_query(client):
    def func(*args, **kwargs):
        return file_graphql_query(*args, **kwargs, client=client)

    return func


# Test your query using the client_query fixture
def test_some_query(client_query):
    test_file = SimpleUploadedFile(name='test.txt', content=file_text.encode('utf-8'))

    response = client_query(
        '''
        mutation testMutation($file: Upload!) {
            myUpload(fileIn: $file) {
                ok
            }
        }
        ''',
        op_name='testMutation'
    files = {'file': test_file},
    )

    content = json.loads(response.content)
    assert 'errors' not in content