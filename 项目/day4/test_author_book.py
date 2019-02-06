# coding: utf-8
import unittest
from author_book import app, db, Author

class DatabaseTest(unittest.TestCase):

    def setUp(self):
        app.testing = True
        app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:mysql@127.0.0.1:3306/flask_test"
        db.create_all()

    def test_add_author(self):
        author = Author(name="zhang", email="123@163.com", mobile="18612345678")
        db.session.add(author)
        db.session.commit()

        import time
        time.sleep(20)
        # 加入一条数据之后的测试: 应该能查出来数据: 数据非空
        author_test = Author.query.filter_by(name="zhang").first()
        self.assertIsNotNone(author_test)

    def tearDown(self):
        db.session.remove() # 断开测试和数据库的连接
        db.drop_all()

if __name__ == '__main__':
    unittest.main()