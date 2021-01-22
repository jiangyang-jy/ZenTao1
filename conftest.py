import requests
import pytest
from case.common_function import login
from case.register.del_register import sql_delete


@pytest.fixture(scope="session")
def login_s(base_url):
    s = requests.Session()
    login(s)
    yield s
    print("这是后置操作")


@pytest.fixture(scope="session", name="dele")
def dele_sql():
    sql_delete()







