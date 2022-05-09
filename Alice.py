"""

Alice.py

"""
from numpy.random import randint
import numpy as np

from qiskit import QuantumCircuit


class Alice:

    def __init__(self, n, alice_bits=np.array([]), alice_bases=np.array([]),
                 message=[], alice_key=np.array([]), alice_sample=np.array([]),
                 shared_key=np.array([]), incoming_basis=np.array([])):
        """
        Purpose: Constructor

        """
        self.n = n
        self.alice_bits = alice_bits
        self.alice_bases = alice_bases
        self.message = message
        self.alice_key = alice_key
        self.alice_sample = alice_sample
        self.shared_key = shared_key
        self.incoming_basis = incoming_basis

    def init_bitstring(self):
        """
        Purpose: Initializes a random bitstring for to be encoded in the bases
        initialized in the following method

        Returns: the bitstring

        """
        np.random.seed(seed=0)
        self.alice_bits = randint(2, size=self.n)
        return self.alice_bits

    def init_bases(self):
        """
        Purpose: Initializes bases

        Returns: Alices's bases used for her encoding

        """
        # bitstring = self.init_bitstring()
        self.alice_bases = randint(2, size=self.n)
        return self.alice_bases

    # Method from:
    # https://qiskit.org/textbook/ch-algorithms/quantum-key-distribution.html
    def encode_bitstring(self, bits, bases):
        """

        Purpose: encodes the given bitstring using the Pauli X and Z matrices

        Returns: the encoded bitstring that she will send to Bob

        Notes: After Alice chooses a string of random bits of size n and a
        random basis for each bit (perhaps one of the Pauli matrices or really
        any unitary transfomration that properly serves as a basis), she
        encodes each bit nto a string of qubits using the basis she chose.

        Source:
        https://qiskit.org/textbook/ch-algorithms/quantum-key-distribution.html
        (very slightly modified)

        """
        for i in range(self.n):
            qc = QuantumCircuit(1, 1)
            if bases[i] == 0:
                if bits[i] == 0:
                    pass
                else:
                    qc.x(0)
            else:
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
        Purpose: Publicly shares which bases were used in init_bases

        Returns: the original bases that were initialized

        Publicy shares which basis they used for each qubit over Eve's
        channel. Just returns the bases Alice used for each qubit.

        """
        return self.init_bases()

    # Method from:
    # https://qiskit.org/textbook/ch-algorithms/quantum-key-distribution.html
    def remove_garbage(self, alice_bases, bob_bases, bits):
        """

        Purpose: removes any bit that doesn't match in Alice and Bob's bases

        Returns: the original bases that were initialized

        Source:
        https://qiskit.org/textbook/ch-algorithms/quantum-key-distribution.html

        This method is the same for Alice and Bob.

        """
        common_bits = []
        for i in range(self.n):
            if alice_bases[i] == bob_bases[i]:
                common_bits.append(bits[i])
        return common_bits

    def share_random_sample(self, bits, selection):
        """

        Purpose: selects a random sample from the bitstring

        Returns: the original bases that were initialized

        At the end of the QKD procedure, both Alice and Bob need to share a
        random sample of their key to make sure they match. If they are the
        same, then QKD was successful. If not, then there was either
        eavesdropping or quantum noise, in which case the procedure fails.

        This method is the same for Alice and Bob.

        """
        sample = []
        for i in selection:
            i = np.mod(i, len(bits))
            sample.append(bits.pop(i))
        return sample
