#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/12/4 21:09
# @Author : moon
import json
import unittest

from libs.my_ddt import ddt, data

from common.base_test_case import BaseTestCase


@ddt
class TestLogin(BaseTestCase):
    name = '登录接口'

    cases = BaseTestCase.load_cases('login')

    @data(*cases)
    def test_login(self, case):
        # 1.测试数据
        request_data = json.loads(case['request_data'])
        expect_data = json.loads(case['expect_data'])

        # 2.测试步骤
        url = self.settings.PROJECT_HOST + self.settings.INTERFACE['login']
        res = self.send_request(url=url, method=case['method'], json=request_data).json()
        # 3.断言
        res_data = {'code': res['code'], 'msg': res['msg']}




if __name__ == '__main__':
    unittest.main()
