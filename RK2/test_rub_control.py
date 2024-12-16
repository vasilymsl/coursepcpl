import unittest
from main import (
    create_one_to_many,
    create_many_to_many,
    task1,
    task2,
    task3,
    Computer,
    HardDrive,
    ComputerHardDrive
)


class TestRubControl(unittest.TestCase):
    def setUp(self):
        self.computers = [
            Computer(1, 'AlphaPC'),
            Computer(2, 'BetaPC'),
            Computer(3, 'GammaPC')
        ]
        self.hard_drives = [
            HardDrive(1, 'Seagate', 1000, 1),
            HardDrive(2, 'WD Blue', 2000, 1),
            HardDrive(3, 'Samsung EVO', 500, 2),
            HardDrive(4, 'Toshiba', 750, 3),
            HardDrive(5, 'Hitachi', 1500, 3)
        ]
        self.computer_hard_drives = [
            ComputerHardDrive(1, 1),
            ComputerHardDrive(1, 2),
            ComputerHardDrive(2, 3),
            ComputerHardDrive(3, 4),
            ComputerHardDrive(3, 5)
        ]

    def test_create_one_to_many(self):
        result = create_one_to_many(self.computers, self.hard_drives)
        expected = [
            ('Seagate', 1000, 'AlphaPC'),
            ('WD Blue', 2000, 'AlphaPC'),
            ('Samsung EVO', 500, 'BetaPC'),
            ('Toshiba', 750, 'GammaPC'),
            ('Hitachi', 1500, 'GammaPC')
        ]
        self.assertEqual(result, expected)

    def test_create_many_to_many(self):
        result = create_many_to_many(
            self.computers, self.computer_hard_drives, self.hard_drives
        )
        expected = [
            ('Seagate', 1000, 'AlphaPC'),
            ('WD Blue', 2000, 'AlphaPC'),
            ('Samsung EVO', 500, 'BetaPC'),
            ('Toshiba', 750, 'GammaPC'),
            ('Hitachi', 1500, 'GammaPC')
        ]
        self.assertEqual(result, expected)

    def test_task1(self):
        one_to_many = create_one_to_many(self.computers, self.hard_drives)
        result = task1(one_to_many)
        expected = [('Seagate', 'AlphaPC'), ('WD Blue', 'AlphaPC')]
        self.assertEqual(result, expected)

    def test_task2(self):
        one_to_many = create_one_to_many(self.computers, self.hard_drives)
        result = task2(self.computers, one_to_many)
        expected = [('AlphaPC', 2000), ('GammaPC', 1500), ('BetaPC', 500)]
        self.assertEqual(result, expected)

    def test_task3(self):
        many_to_many = create_many_to_many(
            self.computers, self.computer_hard_drives, self.hard_drives
        )
        result = task3(many_to_many)
        expected = [
            ('Seagate', 'AlphaPC'),
            ('WD Blue', 'AlphaPC'),
            ('Samsung EVO', 'BetaPC'),
            ('Toshiba', 'GammaPC'),
            ('Hitachi', 'GammaPC')
        ]
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
