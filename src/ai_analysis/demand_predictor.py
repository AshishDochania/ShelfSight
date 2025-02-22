import numpy as np
from sklearn.ensemble import IsolationForest

class AnomalyDetector:
    def __init__(self):
        self.model = IsolationForest(contamination=0.1, random_state=42)

    def fit(self, X):
        self.model.fit(X)

    def detect_anomalies(self, X):
        predictions = self.model.predict(X)
        return np.where(predictions == -1)[0]