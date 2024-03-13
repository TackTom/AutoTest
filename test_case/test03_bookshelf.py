import json
import pytest
from api.login import LoginApi
from common.userlogin import UserLogin
import hashlib



def build_data(file_data):
    book_data = []

    with open(file_data, "rb") as f:
        json_data = json.load(f)
        for case_data in json_data:
            book_id = case_data.get("book_id")
            status_code = case_data.get("status_code")
            info = case_data.get("info")
            code = case_data.get("code")

        book_data.append((book_id, status_code, info, code))

    return book_data

class TestBookself:

    token = None

    def setup_method(self):
        self.login_api = LoginApi()
        self.login_user = UserLogin()


        res_l = self.login_user.login_method()

        TestBookself.token = res_l.json().get("data").get("token")
        print(TestBookself.token)




    def teardown_method(self):
        pass

    @pytest.mark.parametrize("book_id, status_code, info, code", build_data(file_data="../data/test03_bookshelf.json"))
    def test_bookself(self, book_id, status_code, info, code):
        res_bs = self.login_api.putin_bookshelf(json_data=book_id, token=TestBookself.token)

        assert status_code == res_bs.status_code
        assert info in res_bs.json().get("info")
        assert code == res_bs.json().get("code")

