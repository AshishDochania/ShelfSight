import cv2
import numpy as np
from src.computer_vision.image_processor import ImageProcessor
from src.computer_vision.object_detector import ObjectDetector

def test_image_preprocessing():
    processor = ImageProcessor()
    # Create a dummy image (black image)
    dummy_image = np.zeros((480, 640, 3), dtype=np.uint8)
    processed_image = processor.preprocess_image(dummy_image)
    
    assert processed_image is not None
    assert processed_image.shape == (480, 640)

def test_edge_detection():
    processor = ImageProcessor()
    # Create a dummy image (black image)
    dummy_image = np.zeros((480, 640, 3), dtype=np.uint8)
    edges = processor.detect_edges(dummy_image)
    
    assert edges is not None
    assert edges.shape == (480, 640)

def test_object_detection():
    detector = ObjectDetector()
    # Create a dummy image (black image)
    dummy_image = np.zeros((416, 416, 3), dtype=np.uint8)
    boxes, confidences, class_ids = detector.detect_objects(dummy_image)
    
    # Since it's a black image, no objects should be detected
    assert len(boxes) == 0
    assert len(confidences) == 0
    assert len(class_ids) == 0