from src.api.helpers.requests.login_reg import LoginReq

class TestLoginPage:
    def testValidLogin(self):

        email="admin@halterranch.com"
        pswrd="click_here_to_obtain_good_adm1n_password_EXE"

        lR = LoginReq(email, pswrd)
        lR.login()

