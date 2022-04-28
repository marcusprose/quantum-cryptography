"""

Bob.py

"""

from numpy.random import randint
import numpy as np

from qiskit import QuantumCircuit, Aer, transpile, assemble
from qiskit.visualization import plot_histogram, plot_bloch_multivector


class Bob:

    def __init__(self, n, message=[], measurements=[], bob_bases=[],
                 bob_results=[], bob_key=[], bob_sample=[],
                 alice_sample=[], shared_key=[]):
        self.n = n
        self.message = message
        self.measurements = measurements
        self.bob_bases = bob_bases
        self.bob_results = bob_results

        self.bob_key = bob_key
        self.bob_sample = bob_sample
        # self.alice_bases = alice_bases
        self.shared_key = shared_key

    def init_bases(self):
        """
        Initializes bases.

        """
        self.bob_bases = randint(2, size=self.n)
        return self.bob_bases

    def get_encoded_bitstring(self):
        return self.message

    def measure_message(self, message, bases):
        """
        s3
        After reciving alices message, Bob measures each qubit at random with
        random bases.
        
        https://qiskit.org/textbook/ch-algorithms/quantum-key-distribution.html


        """
        backend = Aer.get_backend('aer_simulator')
        for q in range(self.n):
            if bases[q] == 0:  # measuring in Z-basis
                message[q].measure(0, 0)
            if bases[q] == 1:  # measuring in X-basis
                message[q].h(0)
                message[q].measure(0, 0)
            aer_sim = Aer.get_backend('aer_simulator')
            qobj = assemble(message[q], shots=1, memory=True)
            result = aer_sim.run(qobj).result()
            measured_bit = int(result.get_memory()[0])
            self.measurements.append(measured_bit)
        return self.measurements  # bob_results -- should match alice bits

    def share_bases(self):
        """
        s4
        Publicy shares which basis they used for each qubit over Eve's
        channel. Done simultaneously when Alice reveals which bases she used
        to encode her qubits.

        Compare the share bases methods of both Alice and Bob:
        If Bob happens to measure a bit a bit in the same basis that Alice
        prepared it in, this means that the entry in bob_results will match the
        corresponding entry in alice_bits, and they use that bit as part of
        their shared key. If they measured in different bases, Bob's result is
        random, and they both throw that entry away (TODO: write throw_away).

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

    def share_random_sample(self, selection):
        """
        s5
        TODO

        """
        # sample = []
        # for i in selection:
        #     i = np.mod(i, len(remove_garbage()))
