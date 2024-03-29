import requests
import hashlib

"""接口封装时，重点是依据接口文档封装接口信息，需要使用的测试数据是从测试用例传递、接口方法被调用是需要返回对应的响应结果
"""

class LoginApi:
    # 初始化
    # 定义接口地址
    def __init__(self):
        self.login_url = "https://pcuserapi.xwabx.com/v1/user/login"
        self.getbook_url = "https://pcuserapi.xwabx.com/v1/book/getBookInfo"
        self.putin_bookshelf_url = "https://pcuserapi.xwabx.com/v1/book/shelve/create"
        self.deletebook_url = "https://pcuserapi.xwabx.com/v1/book/shelve/delete"

    def login_method(self, json_data):
        requests.packages.urllib3.disable_warnings()
        return requests.post(url=self.login_url, json=json_data, verify=False)

    def get_book(self, test_data):
        requests.packages.urllib3.disable_warnings()
        return requests.get(url=self.getbook_url + f"/{test_data}", verify=False)

    def putin_bookshelf(self, json_data, token):
        requests.packages.urllib3.disable_warnings()
        return requests.post(url=self.putin_bookshelf_url, json=json_data, headers={"Authorization": token}, verify=False)

    def book_delete(self, json_data, token):
        requests.packages.urllib3.disable_warnings()
        return requests.delete(url=self.deletebook_url, json=json_data, headers={"Authorization": token}, verify=False)






