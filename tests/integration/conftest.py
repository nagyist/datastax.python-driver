import pytest

from tests.integration import teardown_package


@pytest.fixture(scope='session', autouse=True)
def setup_and_teardown_packages():
    print('setup')
    yield
    teardown_package()
