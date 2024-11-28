from qiskit import QuantumCircuit, BasicAer, execute
from hashlib import sha256
import time

# --- Quantum Functions ---
def create_phase_oracle(input_string):
    """
    Create a phase oracle for a 12-qubit Grover's algorithm.
    """
    n = len(input_string)
    oracle_circuit = QuantumCircuit(n, name="Phase Oracle")

    # Apply X gates to invert qubits where the input string is '0'
    for i, bit in enumerate(input_string):
        if bit == '0':
            oracle_circuit.x(i)

    # Apply multi-controlled Z gate
    oracle_circuit.h(n - 1)
    oracle_circuit.mcx(list(range(n - 1)), n - 1)
    oracle_circuit.h(n - 1)

    # Revert X gates
    for i, bit in enumerate(input_string):
        if bit == '0':
            oracle_circuit.x(i)

    return oracle_circuit.to_gate()

def create_amplification_gate(n):
    """
    Create an amplification gate for a 12-qubit Grover's algorithm.
    """
    amplification_circuit = QuantumCircuit(n, name="Amplification Gate")

    # Apply X gates
    for i in range(n):
        amplification_circuit.x(i)

    # Apply multi-controlled Z gate
    amplification_circuit.h(n - 1)
    amplification_circuit.mcx(list(range(n - 1)), n - 1)
    amplification_circuit.h(n - 1)

    # Revert X gates
    for i in range(n):
        amplification_circuit.x(i)

    return amplification_circuit.to_gate()

def run_grover_algorithm(input_string, shots=8192):
    """
    Run Grover's algorithm for 12 qubits based on the input string.
    """
    n = len(input_string)
    circuit = QuantumCircuit(n, n)  # n qubits and n classical bits

    # Apply Hadamard gates to all qubits
    for i in range(n):
        circuit.h(i)

    # Add the phase oracle for the input string
    circuit.append(create_phase_oracle(input_string), range(n))

    # Add the amplification gate
    circuit.append(create_amplification_gate(n), range(n))

    # Measure all qubits
    circuit.measure(range(n), range(n))

    # Execute on simulator
    backend = BasicAer.get_backend('qasm_simulator')
    job = execute(circuit, backend, shots=shots)
    result = job.result()
    counts = result.get_counts()

    return counts

# --- Blockchain Implementation ---
class Block:
    def __init__(self, sender, receiver, amount, previous_hash, block_number, accuracy_threshold):
        """
        Initialize a blockchain block with sender, receiver, amount, and mining details.
        """
        self.sender = sender
        self.receiver = receiver
        self.amount = amount
        self.previous_hash = previous_hash
        self.block_number = block_number
        self.timestamp = time.time()

        # Mining Process
        binary_previous_hash = ''.join(format(ord(char), '08b') for char in previous_hash)
        self.nonce = binary_previous_hash[-12:]  # 12-bit nonce
        self.accuracy = 0
        iteration_count = 0
        total_accuracy = 0

        while self.accuracy < accuracy_threshold:
            iteration_count += 1
            counts = run_grover_algorithm(self.nonce)
            target_state = self.nonce[::-1]  # Reverse for little-endian
            self.accuracy = (counts.get(target_state, 0) / 8192) * 100
            total_accuracy += self.accuracy

        average_accuracy = total_accuracy / iteration_count
        print(f"Final Accuracy: {self.accuracy}%")
        print(f"Iterations: {iteration_count}")
        print(f"Average Accuracy: {average_accuracy}%")

        # Generate Block Hash
        block_content = f"{previous_hash}{sender}{receiver}{amount}{self.timestamp}{self.nonce}{self.accuracy}"
        self.block_hash = sha256(block_content.encode('utf-8')).hexdigest()

class Blockchain:
    def __init__(self):
        """
        Initialize the blockchain with a genesis block.
        """
        self.chain = []
        genesis_block = Block("Genesis", "Genesis", "0", "0", 1, 0)
        self.chain.append(genesis_block)

    def add_block(self, block):
        """
        Add a new block to the blockchain.
        """
        self.chain.append(block)

    def display_chain(self):
        """
        Display all blocks in the blockchain.
        """
        print("Block Number | Block Hash                                 | Receiver   | Sender     | Amount | Accuracy")
        for block in self.chain:
            print(f"{block.block_number}            | {block.block_hash} | {block.receiver} | {block.sender} | {block.amount} | {block.accuracy:.2f}%")

# --- Main Program ---
def main():
    sim_accuracy = 90.0  # Simulation accuracy
    quantum_accuracy = 40.0  # Quantum hardware accuracy

    print("Choose backend: (1) Simulator or (2) Real Quantum Hardware")
    backend_choice = input().strip()
    accuracy_threshold = sim_accuracy if backend_choice == "1" else quantum_accuracy

    blockchain = Blockchain()

    while True:
        print("\nOptions:")
        print("1. Add a new block")
        print("2. Display blockchain")
        print("3. Exit")
        user_choice = input("Enter your choice: ").strip()

        if user_choice == "1":
            sender = input("Enter sender address: ")
            receiver = input("Enter receiver address: ")
            amount = input("Enter amount: ")
            previous_block = blockchain.chain[-1]
            new_block = Block(sender, receiver, amount, previous_block.block_hash, len(blockchain.chain) + 1, accuracy_threshold)
            blockchain.add_block(new_block)
        elif user_choice == "2":
            blockchain.display_chain()
        elif user_choice == "3":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
