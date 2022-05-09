"""

Encrypt.py

Notes: enocde_xor, decode_xor, and printProgressBar were three methods obtained
from stackoverflow. Please see below for more details and reference.

"""

import Alice
import Bob
import Eve

from numpy.random import randint
import numpy as np
import time


class Encrypt:

    def __init__(self, n=100, sample_size=8, bob_results=[], alice_key=[],
                 bob_key=[], alice_sample=[], bob_sample=[],
                 intercept_message=[], eve_bases=[]):
        """
        Purpose: Constructor

        """
        self.n = n
        self.sample_size = sample_size
        self.bob_results = bob_results
        self.alice_key = alice_key
        self.bob_key = bob_key
        self.alice_sample = alice_sample
        self.bob_sample = bob_sample

    def list_to_key(self, list):
        """
        Purpose: A simple method to convert a list of integers to an int

        Returns: int

        """
        var = ''
        for i in list:
            var += str(i)
        return int(var)

    def run_without_intercept(self):
        """
        Purpose: Runs the QKD process without any interception. This method
        should be called in main. Returns true if successful (should be true).

        Returns: boolean

        n := number of bits

        """
        # initialize Alice and Bob objects each with 100 bits (hardcoded)
        alice = Alice.Alice(self.n)
        bob = Bob.Bob(self.n)

        np.random.seed(seed=0)

        # Alice generates bits and bases
        alice_bits = randint(2, size=self.n)
        alice_bases = randint(2, size=self.n)
        # alice encodes her bitstring in var message
        message = alice.encode_bitstring(alice_bits, alice_bases)

        # now bob measures the message in a random sequence of bases of his
        # choosing
        bob_bases = randint(2, size=self.n)
        # this is the result for step 3.. bob keeps this result private
        self.bob_results = bob.measure_message(message, bob_bases)

        self.alice_key = alice.remove_garbage(
            alice_bases, bob_bases, alice_bits)
        self.bob_key = bob.remove_garbage(
            alice_bases, bob_bases, self.bob_results)

        # now testing a random sample to make sure the protocol worked
        # correctly
        bit_selection = randint(self.n, size=self.sample_size)

        self.bob_sample = bob.share_random_sample(self.bob_key, bit_selection)
        # print("bob_sample = " + str(bob_sample))
        self.alice_sample = alice.share_random_sample(
            self.alice_key, bit_selection)
        # print("alice_sample = " + str(alice_sample))

        # if successful, true
        samples = (self.bob_sample == self.alice_sample)

        return samples

    def run_with_intercept(self):
        """
        Purpose: Runs the QKD process with Eve acting as an interceptor. This
        method should be called in main. Returns true if successful 
        (should be false).

        Returns: boolean

        """
        alice = Alice.Alice(100)
        bob = Bob.Bob(100)
        eve = Eve.Eve(100)

        alice_bits = alice.init_bitstring()
        alice_bases = alice.init_bases()

        self.message = alice.encode_bitstring(alice_bits, alice_bases)
        self.eve_bases = eve.init_bases()
        self.intercept_message = eve.intercept_message(
            self.message, self.eve_bases)

        # Bob then checks like before and measures the message with his own
        # choice of bases
        bob_bases = bob.init_bases()
        bob_results = bob.measure_message(self.message, bob_bases)
        # just like before, Bob and Alice reveal choice of basis over Eve's
        # public channel
        self.bob_key = bob.remove_garbage(alice_bases, bob_bases, bob_results)
        self.alice_key = alice.remove_garbage(
            alice_bases, bob_bases, alice_bits)

        sample_size = 15
        bit_selection = randint(100, size=sample_size)
        self.bob_sample = bob.share_random_sample(self.bob_key, bit_selection)
        self.alice_sample = alice.share_random_sample(
            self.alice_key, bit_selection)

        samples = (self.bob_sample == self.alice_sample)
        return samples

    # Method not written by me. Method from:
    # https://stackoverflow.com/questions/70040117/how-to-encrypt-strings-in-python-without-a-python-package
    def encode_xor(self):
        """
        Purpose: Encodes a message and outputs the encrypted message to an
        output file that is specified.

        Returns:

        """
        # filename = input('Enter file for encryption: ')
        # # cleartext = input("Enter string: ")
        # key = input("Enter decryption key: ")
        # encrypted_file = input("Enter save name: ")

        # reps = (len(cleartext)-1)//len(key) + 1
        #
        # cipher = open(filename, 'rb').read()
        #
        # a1 = cleartext.encode('utf-8')
        # key = (key * reps)[:len(cleartext)].encode('utf-8')
        # clear = bytes([i1 ^ i2 for (i1, i2) in zip(a1, key)])
        # open(filename, 'wb').write(cipher)

    # Method not written by me. Method from:
    # https://stackoverflow.com/questions/70040117/how-to-encrypt-strings-in-python-without-a-python-package
    def decode_xor(self):
        """
        Purpose: Decodes a message and outputs the decoded message in the
        terminal.

        Returns: 

        """
        key = input("Enter decryption password: ")
        filename = input("Enter save name: ")

        cipher = open(filename, 'rb').read()
        reps = (len(cipher)-1)//len(key) + 1
        key = (key * reps)[:len(cipher)].encode('utf-8')
        clear = bytes([i1 ^ i2 for (i1, i2) in zip(cipher, key)])
        return clear.decode('utf-8')

    # Method not written by me. Method from:
    # https://stackoverflow.com/questions/3173320/text-progress-bar-in-terminal-with-block-characters
    def printProgressBar(self, iteration, total, prefix='', suffix='',
                         decimals=1, length=100, fill='█', printEnd="\r"):
        """
        Call in a loop to create terminal progress bar
        @params:
            iteration   - Required  : current iteration (Int)
            total       - Required  : total iterations (Int)
            prefix      - Optional  : prefix string (Str)
            suffix      - Optional  : suffix string (Str)
            decimals    - Optional  : positive number of decimals in percent complete (Int)
            length      - Optional  : character length of bar (Int)
            fill        - Optional  : bar fill character (Str)
            printEnd    - Optional  : end character (e.g. "\r", "\r\n") (Str)
        """
        percent = ("{0:." + str(decimals) + "f}").format(100
                                                         * (iteration / float(total)))
        filledLength = int(length * iteration // total)
        bar = fill * filledLength + '-' * (length - filledLength)
        print(f'\r{prefix} |{bar}| {percent}% {suffix}', end=printEnd)
        # Print New Line on Complete
        if iteration == total:
            print()

    def print_info_1(self):
        """
        Purpose: Print layout in the terminal for the without intercept case.
        Called in main.

        Returns: None

        """
        print()
        print(f'Bob\'s results = {self.bob_results}')
        print()

        print(f'Alice key = {self.alice_key}')
        print(f'Bob key = {self.bob_key}')
        print()

        print(f'Len_alice = {len(self.alice_key)}')
        print(f'Len_bob = {len(self.bob_key)}')
        print()

        print("bob_sample = " + str(self.bob_sample))
        print("alice_sample = " + str(self.alice_sample))
        print(f'Simulation successful: {self.alice_sample == self.bob_sample}')
        print()

        print(f'Shared private key = {self.list_to_key(self.alice_key)}')

    def print_info_2(self):
        """
        Purpose: Print layout in the terminal for the with intercept case.
        Called in main.

        Returns: 

        Notes: same as above, for intercept case

        """
        print()
        print(f'Eve\'s bases = {self.eve_bases}')
        print()

        print(f'Alice key = {self.alice_key}')
        print(f'Bob key = {self.bob_key}')
        print()

        print(f'Len_alice = {len(self.alice_key)}')
        print(f'Len_bob = {len(self.bob_key)}')
        print()

        print("bob_sample = " + str(self.bob_sample))
        print("alice_sample = " + str(self.alice_sample))
        print(f'Simulation successful: {self.alice_sample == self.bob_sample}')
        print()

        if not (self.alice_sample == self.bob_sample):
            print('Transmission failed')
