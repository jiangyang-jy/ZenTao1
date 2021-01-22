import pytest
import os
import requests
from common.read_yaml import get_yaml
s = requests.Session()
# yaml_file = os.path.join(os.path.dirname(os.path.realpath(__file__)), "test_data.yml")
file = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
yaml_file = file + str(r"\test_data.yml")
print(f"读取到文件地址：{yaml_file}")
test_data = get_yaml(yaml_file)


class TestRegister():
    @pytest.mark.parametrize("test_input, expect", test_data["test_register_1"])
    def test_register_1(self, test_input, expect, base_url, dele):
        url = base_url+"/user/register"
        r = s.post(url, json=test_input)
        print(r.text)
        assert r.json()["msg"] == expect["msg"]
