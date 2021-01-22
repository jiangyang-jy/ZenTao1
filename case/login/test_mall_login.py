import requests
import pytest
import os
from common.read_yaml import get_yaml
s = requests.Session()
# yaml_file = os.path.join(os.path.dirname(os.path.realpath(__file__)), "test_data.yml")
file = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
yaml_file = file + str(r"\test_data.yml")
print(f"读取到文件地址：{yaml_file}")
test_data = get_yaml(yaml_file)


class Test_login():
    """登录成功"""
    @pytest.mark.parametrize("test_input, expect", test_data["test_login_true"])
    def test_login_true(self, test_input, expect, base_url):
        url = base_url + "/user/login"
        r = s.post(url, json=test_input)
        print(r.text)
        assert r.json()["msg"] == expect["msg"]

    """登录失败"""
    @pytest.mark.parametrize("test_input, expect", test_data["test_login_false"])
    def test_login_false(self, test_input, expect, base_url):
        url = base_url + "/user/login"
        r = s.post(url, json=test_input)
        print(r.text)
        assert r.json()["code"] == expect["code"]


if __name__ == '__main__':
    pytest.main(["-s", "test_mall_login.py"])
