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
    def test01_login(self):

        login_data = {
            "type": 2,
            "phone": "18280803475",
            # 把密码转换成MD5码
            "password": hashlib.md5("5201314star".encode("utf-8")).hexdigest()
        }
        # 用户登录
        res_login = self.login_api.login_method(json_data=login_data)
        TestBookshelf.token = res_login.json().get("data").get("token")
        print(TestBookshelf.token)
        print(res_login.status_code)
        print(res_login.json())

    def test02_getbook(self):
        # 获取书本
        res_book = self.login_api.get_book(test_data="?book_id=89530")
        self.book_id = res_book.json().get("data").get("book").get("book_id")
        print(res_book.status_code)
        print(res_book.json())

    # 放入书架
    def test03_bookshelf(self):
        self.test02_getbook()
        bookshelf_data={
            # "book_id": "21"
            "book_id": self.book_id
        }

        res_bookshelf = self.login_api.putin_bookshelf(json_data=bookshelf_data, token=TestBookshelf.token)
        print(res_bookshelf.status_code)
        print(res_bookshelf.json())

        # 从书架删除
    def test04_bookdelete(self):
        self.test02_getbook()
        bookdelete_data={
            "book_id": self.book_id
        }
        res_bookdelete = self.login_api.book_delete(json_data=bookdelete_data, token=TestBookshelf.token)
        print(res_bookdelete.status_code)
        print(res_bookdelete.json())
