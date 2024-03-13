import requests
import hashlib
from api.login import LoginApi


# 加入书架单接口的测试
class TestBook:

    def setup_method(self):
        self.login_api = LoginApi()

    def teardown_method(self):
        pass

    # 获取书籍成功
    def test_book01(self):
        res_book = self.login_api.get_book(test_data="?book_id=89530")
        print(res_book.status_code)
        print(res_book.json())

        assert 200 == res_book.status_code
        assert "Success" in res_book.json().get("info")
        assert 1 == res_book.json().get("code")

    # 获取失败
    def test_book02(self):
        res_book = self.login_api.get_book(test_data="?book=12")
        print(res_book.status_code)
        print(res_book.json())

        assert 200 == res_book.status_code
        assert "书籍信息不存在" in res_book.json().get("info")
        assert 0 == res_book.json().get("code")