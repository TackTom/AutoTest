import requests
import hashlib

"""接口封装时，重点是依据接口文档封装接口信息，需要使用的测试数据是从测试用例传递、接口方法被调用是需要返回对应的响应结果
"""

class LoginApi:
    # 初始化
    # 定义接口地址
    def __init__(self):
        self.login_url = "https://pcuserapi.xwabx.com/v1/user/login"

    def login_method(self, test_data, header_data):
        requests.packages.urllib3.disable_warnings()
        return requests.post(url=self.login_url, json=test_data, headers=header_data, verify=False)


header_data = {
    "Content-Type": "application/json"
}

test_data = {
    "type": 2,
    "phone": "18280803475",
    # 把密码转换成MD5码
    "password": hashlib.md5(b"5201314star").hexdigest()
}

res = LoginApi().login_method(test_data, header_data)
print(res.status_code)
print(res.json())