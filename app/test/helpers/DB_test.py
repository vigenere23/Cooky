import unittest
from assertpy import assert_that

class DB_test(unittest.TestCase):

    def test_(self):
        assert_that(True).is_false()

if __name__ == '__main__':
    unittest.main()
