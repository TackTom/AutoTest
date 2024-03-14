import json

import pytest

from api.login import LoginApi
from common.userlogin import UserLogin


def build_data(json_file):
    json_data = []

    with open(json_file, "rb") as f:
        book_data = json.load(f)

        for case_data in book_data:
            book_id = case_data.get("book_id")
            status_code = case_data.get("status_code")
            info = case_data.get("info")
            code = case_data.get("code")
            json_data.append((book_id, status_code, info, code))

    return json_data


class TestBookDelete:

    token= None

    def setup_method(self):
        self.login_api = LoginApi()
        self.userlogin_api = UserLogin()

        # 取登录的token
        res_l = self.userlogin_api.login_method()
        TestBookDelete.token = res_l.json().get("data").get("token")


        book_data={
            "book_id": "89530"
        }
        self.login_api.putin_bookshelf(json_data=book_data,  token=TestBookDelete.token)



    def teardown_method(self):
        pass

    @pytest.mark.parametrize("book_id,status_code,info,code", build_data(json_file="../data/test04_bookdetele.json"))
    def test_bookdelete(self, book_id, status_code, info, code):
        test_book= {
            "book_id": book_id
        }
        res_bookdelete = self.login_api.book_delete(json_data=test_book, token=TestBookDelete.token)

        assert status_code == res_bookdelete.status_code
        assert info in res_bookdelete.json().get("info")
        assert code == res_bookdelete.json().get("code")