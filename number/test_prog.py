import unittest

import prog


class TestClient(unittest.TestCase):

    def test_is_prime(self):
        parameters = (
            (1, False),
            (2, True),
            (4, False),
            (5, True),
            (71, True),
            (91, False),
        )
        for x, expected in parameters:
            with self.subTest(x=x, expected=expected):
                self.assertEqual(prog.is_prime(x), expected)

if __name__ == '__main__':
    unittest.main(verbosity=2)
