import hashlib
import requests
import config

class UserLogin:
    def __init__(self):
        self.login_url = config.BASE_URL + "/v1/user/login"
        self.login_body = {
            "type": 2,
            "phone": "18280803475",
            # 把密码转换成MD5码
            "password": hashlib.md5("5201314star".encode("utf-8")).hexdigest()
        }

    def login_method(self):
        requests.packages.urllib3.disable_warnings()
        return requests.post(url=self.login_url, json=self.login_body, verify=False)
