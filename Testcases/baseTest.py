import pytest


@pytest.mark.usefixtures("log_on_failure", "get_browser1")
class basetest():
    pass
