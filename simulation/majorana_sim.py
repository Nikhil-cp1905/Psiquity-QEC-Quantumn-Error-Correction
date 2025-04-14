import numpy as np
import matplotlib.pyplot as plt
from qutip import *
import os

def simulate_majorana():
    # Kitaev chain parameters (simplified Majorana model)
    t = 1.0  # hopping amplitude
    delta = 0.5  # superconducting pairing
    mu = 0.0  # chemical potential
    
    # Create Majorana operators
    gamma1 = (sigmax() + 1j*sigmay())/2
    gamma2 = (sigmax() - 1j*sigmay())/2
    
    # Hamiltonian for Majorana zero modes
    H = -1j * t * gamma1 * gamma2 + delta * (gamma1 * gamma1.dag() - gamma2 * gamma2.dag())
    
    # Time evolution
    times = np.linspace(0, 10, 100)
    psi0 = (basis(2,0) + basis(2,1)).unit()  # Initial superposition state
    
    # Simulate evolution
    result = mesolve(H, psi0, times, [], [gamma1, gamma2, sigmaz()])
    
    # Plot results
    plt.figure(figsize=(10,6))
    plt.plot(times, result.expect[0], label="Majorana γ₁")
    plt.plot(times, result.expect[1], label="Majorana γ₂")
    plt.plot(times, result.expect[2], label="Pauli Z")
    plt.xlabel("Time")
    plt.ylabel("Expectation Value")
    plt.title("Majorana Fermion Dynamics")
    plt.legend()
    plt.grid(True)
    
    # Save plot
    os.makedirs("assets/plots", exist_ok=True)
    path = "assets/plots/majorana_plot.png"
    plt.savefig(path)
    plt.close()
    return path
