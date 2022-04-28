import unittest

import Alice
# import Bob TODO


"""

Alice.py unit tests

"""

alice = Alice.Alice(32)


class TestAlice(unittest.TestCase):

    def test_upper(self):
        alice = Alice.Alice(32)
        print(alice.init_bitstring())
        print(alice.init_bases())


if __name__ == '__main__':
    unittest.main()
