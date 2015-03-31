# Hardware eventually fails,
# Sowtware eventually works.

# TDD:
# 1. Write test that fails
# 2. Make it work
# 3. Refactor while testing
# 4. Loop back to 1)
# Интеграционните тестове са за цялата система (проект), unit тестовете
# са за отделни класове, отделни методи (най-ниското ниво на тестване)

import unittest

# в unittest имаме клас TestCase, в него са дефинирани методите за сравняване


class CashDeskTest(unittest.TestCase):
    def test_is_the_universe_ok(self):  # метода трябва да започва с test_.. за да се пусне
        self.assertEqual(2+2, 4)

if __name__ == '__main__':
    unittest.main()
