# Using unittest.mock
from unittest.mock import patch

@patch('your_module.requests.get')
def test_server_call(mock_get):
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {'data': 'test'}
    # Your test code here
