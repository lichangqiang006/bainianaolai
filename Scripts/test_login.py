import pytest

from Base.get_driver import get_driver
from Base.read_yaml import ReadYaml
from Page.page_login import PageLogin

class TestLogin():
    def get_data(self):
        datas = ReadYaml("login.yaml").read_yaml()
        print(datas)
        arrs = []
        for data in datas.values():
            print(data)
            arrs.append((data.get("username"), data.get("password"), data.get("expext"), data.get("toast_except")))
        return arrs


    def setup_class(self):
        self.login= PageLogin(get_driver())

    def teardown_class(self):
        self.login.driver.quit()
    @pytest.mark.parametrize("username","password","expext","toast_expext",get_data())
    def test_login(self,username,password,expext,toast_expext):

        if expext:
            try:
                self.login.page_input_user(username)
                self.login.page_input_pwd(password)
                self.login.page_click_login_btn()
                assert expext in self.login.page_get_nickname()
                # 点击退出
                self.login.





