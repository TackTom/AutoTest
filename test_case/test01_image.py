import requests

url = "https://pcuser.xwabx.com/static/png/img1-7a0f158c.png"
# 关闭https证书校验警告
requests.packages.urllib3.disable_warnings()
response = requests.get(url=url, verify= False)

print(response.status_code)
print(response.text)