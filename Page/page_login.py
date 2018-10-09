import allure
import Page

from Base.base import Base
import Page


class PageLogin(Base):
    # 点击我
    @allure.step("点击我")
    def page_click_me(self):
        self.base_click(Page.me_btn)

    # 点击已有账号，去登录
    @allure.step("点击已有账号，去登录")
    def page_click_info(self):
        self.base_click(Page.user)

    # 输入账号
    @allure.step("输入账号")
    def page_input_user(self,user_name):
        self.base_input(Page.user_name,user_name)

    # 输入密码
    @allure.step("输入密码")
    def page_input_pwd(self,update_pwd):

        self.base_input(Page.update_pwd,update_pwd)
    # 点击登录按钮
    @allure.step("点击登录按钮")
    def page_click_login_btn(self):
        self.base_click(Page.login_btn)

    # 点击设置按钮
    @allure.step("点击设置按钮")
    def page_setting_btn(self):
        self.base_click(Page.setting_btn)

    # 滑动元素  消息推送----修改密码
    @allure.step("滑动元素  消息推送----修改密码")
    def page_drag_and_drop(self):
        el1 = self.base_xpath(Page.msg_send)
        el2 = self.base_xpath(Page.update_pwd)

        self.base_drage_and_drop(el1, el2)

    # 点击退出
    @allure.step("点击退出")
    def page_exit_btn(self):
        self.base_click(Page.exit_btn)

    # 点击确认按钮
    @allure.step("点击确认按钮")
    def page_exit_ok(self):
        self.base_click(Page.exit_ok)

    # 登录操作封装
    def page_login(self,username,password):
        self.page_click_me()
        self.page_click_info()
        self.page_input_user(username)
        self.page_input_pwd(password)
        self.page_click_login_btn()

    # 退出登录封装
    def page_login_logout(self):
        # 点击设置
        self.page_click_setting()
        # 滑动屏幕  消息推送滑到修改密码
        self.page_drag_and_drop()
        # 点击退出按钮
        self.page_click_exit()
        # 确认退出
        self.page_click_exit_ok()

    # 封装 获取nickname的方法
    @allure.step("获取nickname的方法")
    def page_get_nickname(self):
         return self.base_get_toast(Page.me_nickname)

