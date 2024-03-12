import requests
import hashlib


url = "https://pcuserapi.xwabx.com/v1/user/login"
header_data = {
    "Content-Type": "application/json"
}

login_data = {
    "type": 2,
    "phone": "18280803475",
    # 把密码转换成MD5码
    "password": hashlib.md5(b"5201314star").hexdigest()
}

# 关闭https证书校验警告
requests.packages.urllib3.disable_warnings()
response = requests.post(url=url, headers=header_data, json=login_data, verify=False)



print(response.status_code)
print(response.json())