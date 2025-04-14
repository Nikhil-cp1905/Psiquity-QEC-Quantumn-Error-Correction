import cirq

def simulate_noise():
    # Create qubit and circuit
    q = cirq.LineQubit(0)
    circuit = cirq.Circuit(
        cirq.H(q),  # Create superposition
        
        # Fixed noise operations (for demonstration)
        cirq.X(q).with_probability(0.3),  # Bit flip error
        cirq.Z(q).with_probability(0.2),  # Phase flip error
        
        cirq.measure(q, key='result')
    )
    
    # Simulate with fixed seed for reproducibility
    sim = cirq.Simulator(seed=42)
    result = sim.run(circuit, repetitions=10)
    
    return f"Measurement results: {result.measurements['result']}", circuit
