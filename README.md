# quantum-cryptography

This project is a simple exploration of the Quantum Key Distribution (QKD) protocol 
as well as some other examples of more formalized processes for quantum key generation
and distribution. In this project, you will find a jupyter notebook explaining the process,
as well as classes to run the program in your local terminal. Pleae see below for an explanation 
of each file. 
## Files

- main.py
    - main.py is where all of the classes are called and initialized. Run this file.
- Alice.py
    - Alice.py is a class that acts as the sender of bits to a Bob object. Alice.py contains methods to generate a sting of bits and bases
        and has the ability to encode and return her messages. See code comments for more detailed explanations of each method.
- Bob.py
    - Bob.py is a class that acts as the reciever of a message from the Alice object. Together, Alice and Bob represent two individuals communicating through a quantum channel.
        See code comments for more detailed explanations of each method.
- Eve.py
    - Eve.py is an interceptor class, acting as an individual attempting to tamper with the message that Alice and Bob are trying to generate.
- Encrypt.py
    - Encrypt.py is the master class that runs all the Alice, Bob, and Eve objects. 
- qkd.ipynb
    - This is the jupyternotebook that runs the simplified version of QKD implemented in main.py, 
        but it also includes a detailed explanaiton and implementation of the BB84 algorithm and circuit.
- unit_tests.py
    - These are the unit tests. See the below section for details on compilation.
## Run Locally

Clone the project and navigate to the project directory

```bash
  git clone https://link-to-project
```

Install any dependencies using pip3

```bash
  pip3 install qiskit
```

Run the program in the terminal using the following for without interception and interception, respectively

```bash
  python3 main.py -noeve
  python3 main.py -eve
```

## Running Tests

To run tests, navigate to the project directory and run the following command

```bash
  python3 unit_tests.py
```



## Acknowledgements

The following references were extremely helpful in my implementation and
understanding of Quantum Key Distribution. Further in the code are explicit
references to code that I built on or used.

 - [Qiskit documentation on QKD](https://qiskit.org/textbook/ch-algorithms/quantum-key-distribution.html#1.-Introduction)
 - [Simple python encryptor ](https://stackoverflow.com/questions/70040117/how-to-encrypt-strings-in-python-without-a-python-package)
 - [Building a progress bar](https://stackoverflow.com/questions/3173320/text-progress-bar-in-terminal-with-block-characters)
