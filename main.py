import streamlit as st
from simulation.majorana_sim import simulate_majorana
from simulation.qubit_noise import simulate_noise
from simulation.ml_predictor import train_predictor
from simulation.error_correction import error_correction_demo
import logging

# Configure app
st.set_page_config(layout="centered", page_title="QuantumSim Explorer", page_icon="🧊")
st.title("🧊 QuantumSim Explorer")
st.caption("An interactive journey into Majorana-based quantum computing")

# Sidebar with navigation
page = st.sidebar.radio("Navigate to:", [
    "🌌 Quantum Basics", 
    "🧬 Majorana Qubits", 
    "⚡ Simulations", 
    "🔮 Error Correction"
])

# Quantum Basics Page
if page == "🌌 Quantum Basics":
    st.header("🌌 Quantum Computing Fundamentals")
    
    tab1, tab2, tab3 = st.tabs(["Qubits 101", "Quantum vs Classical", "Applications"])
    
    with tab1:
        st.subheader("What is a Qubit?")
        st.write("""
        - Basic unit of quantum information (like a classical bit)
        - Can be 0, 1, or any quantum superposition of these states
        - Exhibits quantum properties like entanglement and interference
        """)
        
        if st.checkbox("Show qubit visualization"):
            st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/a/ad/Bloch_sphere.svg/1200px-Bloch_sphere.svg.png", 
                    caption="Bloch Sphere representation of a qubit state", width=300)
    
    with tab2:
        st.subheader("Quantum vs Classical Computing")
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("**Classical Bits**")
            st.write("- Either 0 or 1")
            st.write("- Deterministic operations")
            st.write("- No entanglement")
        
        with col2:
            st.markdown("**Quantum Qubits**")
            st.write("- Superposition of 0 and 1")
            st.write("- Probabilistic outcomes")
            st.write("- Entanglement possible")
        
        st.progress(0.75, text="Quantum advantage grows with problem complexity")
    
    with tab3:
        st.subheader("Real-world Applications")
        app = st.selectbox("Explore use cases:", [
            "Drug Discovery",
            "Financial Modeling", 
            "Cryptography",
            "Material Science"
        ])
        
        if app == "Drug Discovery":
            st.write("Quantum computers can simulate molecular interactions at atomic scale")
        elif app == "Financial Modeling":
            st.write("Portfolio optimization and risk analysis with quantum algorithms")
        elif app == "Cryptography":
            st.write("Breaking current encryption (Shor's algorithm) and quantum-safe cryptography")
        else:
            st.write("Designing new materials with specific properties like high-temperature superconductors")

# Majorana Qubits Page
elif page == "🧬 Majorana Qubits":
    st.header("🧬 Majorana Fermion Qubits")
    
    st.write("""
    Majorana qubits are topological qubits based on exotic particles called Majorana fermions 
    that are their own antiparticles. They offer inherent protection against decoherence.
    """)
    
    with st.expander("🔍 How Majorana Qubits Work"):
        st.image("https://www.quantamagazine.org/wp-content/uploads/2020/06/Majorana-Quanta-1-1440x960.jpg", 
                caption="Majorana particles emerge at ends of nanowires in topological superconductors")
        st.write("""
        1. **Nanowire Setup**: Semiconductor nanowire with strong spin-orbit coupling
        2. **Superconductivity**: Proximity-coupled to a superconductor
        3. **Magnetic Field**: Applied to create topological phase
        4. **Majoranas**: Appear as zero-energy modes at wire ends
        """)
    
    with st.expander("⚖️ Advantages"):
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("**Topological Protection**")
            st.write("- Errors require global changes")
            st.write("- More stable than conventional qubits")
        
        with col2:
            st.markdown("**Scalability**")
            st.write("- Braiding operations for gates")
            st.write("- Natural error resistance")
    
    if st.button("🚀 See Majorana Qubit Simulation"):
        path = simulate_majorana()
        st.image(path, caption="Majorana Fermion Qubit Simulation")
        logging.info("Ran Majorana simulation")

# Simulations Page
elif page == "⚡ Simulations":
    st.header("⚡ Interactive Quantum Simulations")
    
    sim_type = st.selectbox("Choose simulation:", [
        "Qubit Noise Dynamics",
        "Quantum Gate Operations",
        "Entanglement Visualization"
    ])
    
    if sim_type == "Qubit Noise Dynamics":
        st.write("Explore how different noise sources affect qubit coherence")
        noise_type = st.radio("Noise type:", ["Dephasing", "Amplitude Damping", "Thermal"])
        
        if st.button("Run Noise Simulation"):
            output, circuit = simulate_noise(noise_type)
            st.text(output)
            st.text(str(circuit))
            logging.info(f"Ran {noise_type} noise simulation")
    
    elif sim_type == "Quantum Gate Operations":
        gate = st.selectbox("Select gate:", ["Hadamard", "CNOT", "Pauli-X", "T Gate"])
        st.write(f"Applying {gate} gate to qubit state")
        
        if st.button("Apply Gate"):
            # Placeholder for gate operation visualization
            st.success(f"{gate} gate applied successfully!")
    
    else:
        st.write("Visualize quantum entanglement between two qubits")
        if st.button("Create Bell State"):
            st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/5/5a/Bell-state-circuit.png/800px-Bell-state-circuit.png",
                   caption="Circuit creating an entangled Bell state")

# Error Correction Page
elif page == "🔮 Error Correction":
    st.header("🔮 Quantum Error Correction")
    
    st.write("""
    Quantum error correction uses redundancy to protect quantum information 
    from errors due to decoherence and other quantum noise.
    """)
    
    with st.expander("🧩 Surface Code"):
        st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/7/7a/Surface_code.svg/1200px-Surface_code.svg.png",
               caption="Surface code - a topological quantum error correcting code")
    
    if st.button("Run Error Correction Demo"):
        result, circuit = error_correction_demo()
        st.text(result)
        st.text(str(circuit))
        logging.info("Ran error correction simulation")
    
    if st.checkbox("Train Error Prediction Model"):
        progress = st.progress(0)
        msg = train_predictor()
        progress.progress(100)
        st.success(msg)
        logging.info("Trained ML model")

# Footer
st.sidebar.markdown("---")
st.sidebar.caption("""
QuantumSim Explorer v1.0  
Explore the frontier of quantum computing!
""")
