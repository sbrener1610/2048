import unittest
from field import Field2048

class TestField(unittest.TestCase):

    def setUp(self):
        self.field=Field2048()

    def test_sweep_row(self):
        self.assertEqual(self.field.sweep_row([2,16,4,16]),[2,16,4,16])

    def test_field_from_row(self):
        self.assertEqual(self.field.make_field_from_rows([2,4,2,4],[4,8,4,2],[8,8,2,4],[8,4,2,2]),[[2,4,2,4],[4,8,4,2],[8,8,2,4],[8,4,2,2]])

    def test_field_from_columns(self):
        self.assertEqual(self.field.make_field_from_columns([2,4,2,4],[4,8,4,2],[8,8,2,4],[8,4,2,2]),[[2,4,8,8],[4,8,8,4],[2,4,2,2],[4,2,4,2]])


if __name__ == '__main__':
    unittest.main()