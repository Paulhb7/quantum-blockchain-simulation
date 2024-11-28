# Quantum Blockchain with Grover's Algorithm

This project implements a blockchain that integrates quantum computation using Grover's algorithm for proof-of-work. It uses 12 qubits for mining blocks, leveraging quantum principles for enhanced security and computation.

## Features

- **Quantum Mining**: Uses Grover's algorithm with 12 qubits to mine blocks.
- **Blockchain Functionality**: Supports adding blocks and displaying the current blockchain.
- **Simulation and Real Hardware**:
  - Simulate Grover's algorithm using Qiskit's simulator.
  - (Optional) Extend to use IBM Quantum's real hardware for mining.
- **Dynamic Proof-of-Work**: Adjusts mining difficulty based on backend accuracy.

---

## Installation

### Prerequisites

1. **Python**: Version 3.8 or higher.
2. **Qiskit**: Install using pip.

   ```bash
   pip install qiskit
