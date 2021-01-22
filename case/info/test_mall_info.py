import pytest
import os
from common.read_yaml import get_yaml
file = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))  # 获取上一层目录的路径
yaml_file = file + str(r"\test_data.yml")
print(f"读取到文件地址：{yaml_file}")
test_data = get_yaml(yaml_file)


class TestInfo():
    """修改昵称成功"""
    @pytest.mark.parametrize("test_input, expect", test_data["test_info_1"])
    def test_info_1(self, test_input, expect, login_s, base_url):
        url = base_url+"/user/editUserInfo"
        r = login_s.post(url, json=test_input)
        print(r.text)
        assert r.json()["msg"] == expect["msg"]


if __name__ == '__main__':
    pytest.main(["-s", "test_mall_login.py"])
