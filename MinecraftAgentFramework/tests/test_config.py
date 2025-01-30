import os

def get_server_url():
    # Use environment variable in CI, fallback to localhost:4711 for local development
    return os.getenv('TEST_SERVER_URL', 'http://localhost:4711')

def is_ci_environment():
    return os.getenv('TEST_MODE') == 'ci'
