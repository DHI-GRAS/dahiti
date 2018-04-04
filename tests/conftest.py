import os

import pytest


@pytest.fixture
def dahiti_credentials():
    envvars = dict(username='DAHITI_USERNAME',
                   password='DAHITI_PASSWORD')
    credentials = {
        name: os.environ.get(varname)
        for name, varname in envvars.items()}
    if None in list(credentials.values()):
        raise RuntimeError(
            'DAHITI credentials must be defined as environment variables: {}'
            .format(envvars))
    return credentials
