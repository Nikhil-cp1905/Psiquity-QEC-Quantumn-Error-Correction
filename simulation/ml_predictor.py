import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

def train_predictor():
    # Create deterministic dataset
    np.random.seed(42)
    states = np.random.uniform(-1, 1, (1000, 3))
    # Create correlated error patterns
    bit_flip = (states @ np.array([0.3, -0.2, 0.1]) > 0.2).astype(int)
    phase_flip = (states @ np.array([-0.1, 0.4, 0.2]) > 0.3).astype(int)
    
    df = pd.DataFrame(states, columns=["X", "Y", "Z"])
    df["BitFlip"] = bit_flip
    df["PhaseFlip"] = phase_flip
    
    X = df[["X", "Y", "Z"]]
    y = df[["BitFlip", "PhaseFlip"]]
    
    # Train model
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )
    
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    
    # Calculate accuracy for each error type separately
    y_pred = model.predict(X_test)
    bit_flip_acc = accuracy_score(y_test["BitFlip"], y_pred[:, 0])
    phase_flip_acc = accuracy_score(y_test["PhaseFlip"], y_pred[:, 1])
    
    return f"Model trained. Accuracy: BitFlip {bit_flip_acc*100:.1f}%, PhaseFlip {phase_flip_acc*100:.1f}%"
