# coding: utf-8

import unittest
from login import app
import json

class LoginTest(unittest.TestCase):
    '''测试登录参数为空的情况'''
    def setUp(self):
        # testing模式开启之后　视图函数的错误可以知道
        app.testing = True

        # 1. 创建向后端发送数据的客户端
        # 在不同的对象函数中都要用这个client对象: 写成
        # self.client
        self.client = app.test_client()

    # 测试的函数必须以test开头
    def test_empty_username_password(self):
        # 2. 客户端以post方式发送数据,返回响应
        res = self.client.post("/login", data={})
        # 3. 响应.data 获得响应体
        resp = res.data
        # 4. 响应体是json格式，转化为python类型
        resp = json.loads(resp)
        # 5. 因为返回过来的数据是dict, 用dict的方式得到数据判断
        self.assertIn("code", resp)
        self.assertEqual(resp["code"], 1)

    def test_wrong_username_password(self):
        # 2. 客户端以post方式发送数据,返回响应
        res = self.client.post("/login", data={
            "username": "itcast",
            "password": "pass"
        })
        # 3. 响应.data 获得响应体
        resp = res.data
        # 4. 响应体是json格式，转化为python类型
        resp = json.loads(resp)
        # 5. 因为返回过来的数据是dict, 用dict的方式得到数据判断
        self.assertIn("code", resp)
        self.assertEqual(resp["code"], 2)

if __name__ == '__main__':
    unittest.main() # 单元测试的main函数运行