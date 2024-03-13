from api.login import LoginApi
import hashlib

class TestBookshelf:
    # 初始化token
    token = None

    # 前置处理
    def setup_method(self):
        self.login_api = LoginApi()

    # 后置处理
    def teardown_method(self):
        pass

    # 登录
    def test01_putin_bookshelf_success(self):

        login_data = {
            "type": 2,
            "phone": "18280803475",
            # 把密码转换成MD5码
            "password": hashlib.md5(b"5201314star").hexdigest()
        }
        # 用户登录
        res_login = self.login_api.login_method(json_data=login_data)
        print(res_login.status_code)
        print(res_login.json())

    # 获取书本
        res_book = self.login_api.get_book(test_data="?book_id=89530")
        print(res_book.status_code)
        print(res_book.json())

    # 放入书架

        bookshelf_data={
            # "book_id": "21"
            "book_id":  res_book.json().get("data").get("book").get("book_id")
        }

        TestBookshelf.token = res_login.json().get("data").get("token")
        print(TestBookshelf.token)

        res_bookshelf = self.login_api.putin_bookshelf(json_data=bookshelf_data, token=TestBookshelf.token)
        print(res_bookshelf.status_code)
        print(res_bookshelf.json())