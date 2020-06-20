import unittest

class TestStringMethods(unittest.TestCase):  # 继承 unittest.TestCase 是固定的写法

    def test_upper(self):  # 单测函数一般以test开头
        self.assertEqual('foo'.upper(), 'FOO')  # 使用assert断言判断测试结果是否符合预期

if __name__ == '__main__':
    unittest.main()  # 这个也是固定写法
