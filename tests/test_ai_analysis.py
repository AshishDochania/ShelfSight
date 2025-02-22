import numpy as np
from src.ai_analysis.demand_predictor import DemandPredictor
from src.ai_analysis.anomaly_detector import AnomalyDetector

def test_demand_prediction():
    predictor = DemandPredictor()
    
    # Dummy training data (X: features, y: target values)
    X = np.random.rand(100, 5)
    y = np.random.rand(100)
    
    predictor.train(X, y)
    
    # Test prediction on new data
    X_test = np.random.rand(10, 5)
    predictions = predictor.predict(X_test)
    
    assert len(predictions) == len(X_test)

def test_anomaly_detection():
    detector = AnomalyDetector()
    
    # Dummy data with some anomalies
    X = np.random.rand(100, 5)
    X[95:] += 10  # Add anomalies
    
    detector.fit(X)
    
    anomalies = detector.detect_anomalies(X)
    
    assert len(anomalies) > 0