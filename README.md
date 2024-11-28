# Quantum Blockchain with Grover's Algorithm

This project implements a blockchain that integrates quantum computation using Grover's algorithm for proof-of-work. It uses 12 qubits for mining blocks, leveraging quantum principles for enhanced security and computation.

## Goal
The primary goal of this project is to simulate and explore the use of quantum algorithms for blockchain mining, focusing on:

- **Efficiency**: Using Grover's algorithm to mine blocks faster than classical approaches.
- **Accuracy**: Balancing the inherent noise in quantum hardware with reliable proof-of-work mechanisms.
- **Proof of Concept**: Demonstrating how quantum technology could be integrated into blockchain protocols in the future.

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
