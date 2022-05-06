"""

unit_test.py

"""

import unittest

import Alice
import Bob


"""

Alice.py unit tests

"""

alice = Alice.Alice(32)


class TestAlice(unittest.TestCase):

    def test_upper(self):
        alice = Alice.Alice(32)
        bitstring = alice.init_bitstring()
        bases = alice.init_bases()

        print(f'Alice initial bitstring: {bitstring}')
        print(f'Alice basis initialization: {bases}')

        print()
        print('----------------MESSAGE AND BASES INITIALIZED---------------')
        print()

        # s3: encode bitstring with the random bases
        for i in range(32):
            print(
                f'Alice encoded bitstring for bit {i + 1}:  ')
            print(f'{alice.encode_bitstring(bitstring, bases)[i]}')

        print()
        print('-------------------BITSTRING ENCODED------------------------')
        print()

        # s4: Share bases
        print(f'Alice\'s bases to share: {alice.share_bases()}')

        # print(alice.remove_garbage(bases, bob_bases, bits))

        # s5: Bob and Alice compare a random selection of the bits in their
        # keys to make sure the protocol has worked correctly

        print()
        print('-------------------END ALICE TEST------------------------')
        print()


class TestBob(unittest.TestCase):
    def test_upper(self):
        bob = Bob.Bob(32)
        bases = bob.init_bases()

        # alice inits her bitstring and bases
        alice.init_bitstring()
        alice.init_bases()

        # incoming encoded message from alice
        encoded_message = alice.encode_bitstring(
            alice.alice_bits, alice.alice_bases)
        measure_message = bob.measure_message(encoded_message, bases)

        print(f'Bob basis initialization: {bases}')

        print()
        print('---------------------------BASES INITIALIZED---------------')
        print()

        print(f'Bob\'s measured message: {measure_message}')

        # TODO: the rest

        print()
        print('-------------------END BOB TEST------------------------')
        print()


if __name__ == '__main__':
    unittest.main()
