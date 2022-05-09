"""

Eve.py

"""

from numpy.random import randint
from qiskit import Aer, assemble


class Eve:

    def __init__(self, n, message=[], measurements=[], eve_bases=[],
                 eve_results=[]):
        """
        Purpose: Constructor

        """
        self.n = n
        self.message = message
        self.measurements = measurements
        self.eve_bases = eve_bases

    def init_bases(self):
        """
        Purpose: Initializes bases

        Returns: Eve's bases used for her interception

        """
        self.eve_bases = randint(2, size=self.n)
        return self.eve_bases

    def intercept_message(self, message, bases):
        """
        Purpose: Measures the coded message from Alice

        Returns: Returns the measured message (her bases) recieved from Alcie

        After reciving alices message, Bob measures each qubit at random with
        random bases

        Source:
        https://qiskit.org/textbook/ch-algorithms/quantum-key-distribution.html

        This is the same as the Bob meaure_message method

        """
        for q in range(self.n):
            if bases[q] == 0:
                message[q].measure(0, 0)
            if bases[q] == 1:
                message[q].h(0)
                message[q].measure(0, 0)
            aer_sim = Aer.get_backend('aer_simulator')
            qobj = assemble(message[q], shots=1, memory=True)
            result = aer_sim.run(qobj).result()
            measured_bit = int(result.get_memory()[0])
            self.measurements.append(measured_bit)
        return self.measurements
