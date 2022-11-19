import unittest
from yandex import YaUploader
from parameterized import parameterized
from unittest.mock import patch
from unittest import mock

fixture = [
    ('NewFolder', 'Ok'),
    ('Документы', 'Такая папка существует') #используйте тут название уже существующей папки
]

class MyTestCase(unittest.TestCase):

    @parameterized.expand(fixture)
    def test_new_folder(self, name, resp):
        self.ya = YaUploader()
        self.assertEqual(self.ya.new_folder(name), resp)

    def teardown(self):


if __name__ == '__main__':
    unittest.main()
