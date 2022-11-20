import unittest
from yandex import YaUploader
from parameterized import parameterized


fixture = [
    ('NewFolder', 'Ok'),
    ('NewFolder', 'Такая папка существует')
]

class MyTestCase(unittest.TestCase):

    @parameterized.expand(fixture)
    def test_new_folder(self, name, resp):
        self.ya = YaUploader()
        self.assertEqual(self.ya.new_folder(name), resp)

    @classmethod
    def tearDownClass(self):
        self.ya = YaUploader()
        self.ya.del_folder('NewFolder')


if __name__ == '__main__':
    unittest.main()
