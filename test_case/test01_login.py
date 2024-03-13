import json
from api.login import LoginApi
import hashlib
import pytest


def build_data(json_file):
    # 定义一个空列表用于存放数据
    test_data = []
    #     打开文件
    with open(json_file, "rb") as f:
        json_data = json.load(f)
        # 遍历文件中的数据
        for case_data in json_data:
            phone = case_data.get("phone")
            password = case_data.get("password")
            status_code = case_data.get("status_code")
            info = case_data.get("info")
            code = case_data.get("code")
            # 以元组的形式存放在列表中
            test_data.append((phone, password, status_code, info, code))
    # 返回数据
    return test_data



class TestLogin:
    # @classmethod
    def setup_method(self):
        self.login_api = LoginApi()
    # @classmethod
    def teardown_method(self):
        pass

    # 测试手机号和密码正确登录成功
    @pytest.mark.parametrize("phone,password,status_code,info,code", build_data(json_file="../data/test01_login.json"))
    def test_login01(self, phone, password, status_code, info, code):
        login_data = {
            "type": 2,
            "phone": phone,
            "password": hashlib.md5(password.encode("utf-8")).hexdigest()
        }

        res_l = self.login_api.login_method(json_data=login_data)
        print(res_l.status_code)
        print(res_l.json())
        assert status_code == res_l.status_code
        assert info in res_l.json().get("info")
        assert code == res_l.json().get("code")

    # 测试手机号为空，登录失败
    # def test_login02(self):
    #     login_data = {
    #         "type": 2,
    #         "phone": "",
    #         "password": hashlib.md5(b"5201314star").hexdigest()
    #     }
    #
    #     res_l = self.login_api.login_method(json_data=login_data)
    #     print(res_l.status_code)
    #     print(res_l.json())
    #     assert 200 == res_l.status_code
    #     assert "手机号不能为空" in res_l.json().get("info")
    #     assert 0 == res_l.json().get("code")
    #
    # # 测试密码错误，登录失败
    # def test_login03(self):
    #     login_data = {
    #         "type": 2,
    #         "phone": "18280803475",
    #         "password": hashlib.md5(b"5201314sta").hexdigest()
    #     }
    #
    #     res_l = self.login_api.login_method(json_data=login_data)
    #     print(res_l.status_code)
    #     print(res_l.json())
    #     assert 200 == res_l.status_code
    #     assert "密码不正确" in res_l.json().get("info")
    #     assert 0 == res_l.json().get("code")