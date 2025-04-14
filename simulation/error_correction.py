import cirq

def error_correction_demo():
    # Create qubits
    q = [cirq.LineQubit(i) for i in range(3)]
    
    # Create circuit with fixed error
    circuit = cirq.Circuit(
        cirq.H(q[0]),
        cirq.CNOT(q[0], q[1]),
        cirq.CNOT(q[0], q[2]),
        
        # Fixed error on qubit 1
        cirq.X(q[1]).with_probability(1.0),  # Force error for demonstration
        
        # Syndrome measurement
        cirq.CNOT(q[0], q[1]),
        cirq.CNOT(q[0], q[2]),
        cirq.H(q[0]),
        
        # Measure all qubits
        cirq.measure(*q, key='result')
    )
    
    # Simulate with fixed seed
    sim = cirq.Simulator(seed=42)
    result = sim.run(circuit, repetitions=5)
    
    explanation = """
    Error Correction Demonstration:
    1. Encoded |+⟩ state across 3 qubits
    2. Introduced X error on qubit 1
    3. Performed syndrome measurement
    4. Results show error detection capability
    """
    
    return explanation + "\n\nMeasurements:\n" + str(result), circuit
