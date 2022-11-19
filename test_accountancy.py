import unittest
from unittest.mock import patch
from parameterized import parameterized
from accountancy import *

fixture_01 = [
    ('2207 876234', 'Василий Гупкин'),
    ('11-2', 'Геннадий Покемонов'),
    ('Q', 'Возврат в меню.'),
    ('874565ftytk', 'Документ не найден, введите номер документа: ')
]

fixture_02 = [
    ('5455 028765', 'Он на полке 1'),
    ('Q', 'Возврат в меню.'),
    ('agafgag', 'Документ не найден, введите номер документа: ')
]

fixture_03 = [
    (),
]

class MyTestCase(unittest.TestCase):
    @parameterized.expand(fixture_01)
    def test_show_name_by_doc(self, number, name):
        with patch('accountancy.input', return_value=number) as _raw_input:
            self.assertEqual(show_name_by_doc(documents, directories), name)

    @parameterized.expand(fixture_02)
    def test_show_shelf_by_doc(self, number, shelf):
        with patch('accountancy.input', return_value=number) as _raw_input:
            self.assertEqual(show_shelf_by_doc(documents, directories), shelf)

    def test_all_documents(self):
        self.assertEqual(all_documents(documents, directories), ['passport "2207 876234" "Василий Гупкин"', 'invoice "11-2" "Геннадий Покемонов"', 'insurance "10006" "Аристарх Павлов"'])


    # @parameterized.expand(fixture_03)
    # def test_show_shelf_by_doc(self, number, shelf):
    #     with patch('accountancy.input', return_value=number) as _raw_input:
    #         self.assertEqual(show_shelf_by_doc(documents, directories), shelf)


            
if __name__ == '__main__':
    unittest.main()
