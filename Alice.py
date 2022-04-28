"""

Alice.py

"""
from numpy.random import randint
import numpy as np

from qiskit import QuantumCircuit, Aer, transpile, assemble
from qiskit.visualization import plot_histogram, plot_bloch_multivector


class Alice:

    """

    Alice.py

    """

    def __init__(self, n, alice_bits=np.array([]), alice_bases=np.array([]),
                 message=[],
                 alice_key=np.array([]), alice_sample=np.array([]),
                 shared_key=np.array([])):
        self.n = n
        self.alice_bits = alice_bits
        self.alice_bases = alice_bases
        self.message = message
        self.alice_key = alice_key
        self.alice_sample = alice_sample
        self.shared_key = shared_key

    def init_bitstring(self):
        np.random.seed(seed=0)
        self.alice_bits = randint(2, size=self.n)
        return self.alice_bits

    def init_bases(self):
        # bitstring = self.init_bitstring()
        self.alice_bases = randint(2, size=self.n)
        return self.alice_bases

    def encode_bitstring(self, bits, bases):
        """
        s2
        After Alice chooses a string of random bits of size n and a random
        basis for each bit (perhaps one of the Pauli matrices or really any
        unitary transfomration that properly serves as a basis), she encodes
        each bit nto a string of qubits using the basis she chose.


        Returns: the encoded bitstring that she will send to Bob

        Code source:
        https://qiskit.org/textbook/ch-algorithms/quantum-key-distribution.html
        (very slightly modified)

        """
        for i in range(self.n):
            qc = QuantumCircuit(1, 1)
            if bases[i] == 0:  # Prepare qubit in Z-basis
                if bits[i] == 0:
                    pass
                else:
                    qc.x(0)
            else:  # Prepare qubit in X-basis
                if bits[i] == 0:
                    qc.h(0)
                else:
                    qc.x(0)
                    qc.h(0)
            qc.barrier()
            self.message.append(qc)
        return self.message

    def share_bases(self):
        """
        s4
        Publicy shares which basis they used for each qubit over Eve's
        channel. Just returns the bases Alice used for each qubit.

        """
        return self.init_bases()

    def remove_garbage(self, alice_bases, bob_bases, bits):
        """

        https://qiskit.org/textbook/ch-algorithms/quantum-key-distribution.html

        """
        common_bits = []
        for i in range(self.n):
            if alice_bases[i] == bob_bases[i]:
                common_bits.append(bits[i])
        return common_bits

    def share_random_sample(self):
        """
        s5
        TODO

        """
        return
