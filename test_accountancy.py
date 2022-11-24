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
    ('passport', '101202', 'Максим', '1'),
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
        self.assertEqual(all_documents(documents, directories), ['passport "2207 876234" "Василий Гупкин"', 'invoice "11-2" "Геннадий Покемонов"', 'insurance "10006" "Аристарх Павлов"', 'passport "101202" "Максим"'])


#тут проблема, потому что я не знаю, как замокать цикличный ввод
    @patch('builtins.input')
    def test_add_new_doc(self, m_input):
        m_input.side_effect = ['passport', '101202', 'Максим', '1']
        self.assertEqual(add_new_doc(documents, directories), 'Успешно помещено на полку 1')

    def delete_doc(self): #очень удобно, тестирование этой функции удалит тестовый документ
        with patch('accountancy.input', return_value='101202') as _raw_input:
            self.assertEqual(delete_doc(documents, directories), 'Удалено')
            
if __name__ == '__main__':
    unittest.main()
