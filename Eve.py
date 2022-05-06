"""

Eve.py

"""

from numpy.random import randint
import numpy as np

from qiskit import QuantumCircuit, Aer, transpile, assemble
from qiskit.visualization import plot_histogram, plot_bloch_multivector


class Eve:

    """

    Eve.py

    """

    def __init__(self, n, message=[], measurements=[], eve_bases=[],
                 eve_results=[]):
        self.n = n
        self.message = message
        self.measurements = measurements
        self.eve_bases = eve_bases

    def init_bases(self):
        """
        Initializes bases.

        """
        self.eve_bases = randint(2, size=self.n)
        return self.eve_bases

    def intercept_message(self, message, bases):
        """

        Same as Bob measure_message method.

        https://qiskit.org/textbook/ch-algorithms/quantum-key-distribution.html


        """
        backend = Aer.get_backend('aer_simulator')  # TODO
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
        return self.measurements
