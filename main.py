import streamlit as st
from simulation.majorana_sim import simulate_majorana
from simulation.qubit_noise import simulate_noise
from simulation.ml_predictor import train_predictor
from simulation.error_correction import error_correction_demo
import logging

st.set_page_config(layout="centered", page_title="QuantumSim App 🧠")

st.title("🧬 Majorana-Based Quantum Simulator")

if st.button("1️⃣ Simulate Majorana Qubit"):
    path = simulate_majorana()
    st.image(path, caption="Majorana Fermion Qubit Simulation")
    logging.info("Ran Majorana simulation")

if st.button("2️⃣ Simulate Qubit Noise"):
    output, circuit = simulate_noise()
    st.text(output)
    st.text(str(circuit))
    logging.info("Ran noise simulation")

if st.button("3️⃣ Train Qubit Error Predictor"):
    msg = train_predictor()
    st.success(msg)
    logging.info("Trained ML model")

if st.button("4️⃣ Run Quantum Error Correction"):
    result, circuit = error_correction_demo()
    st.text(result)
    st.text(str(circuit))
    logging.info("Ran error correction simulation")
