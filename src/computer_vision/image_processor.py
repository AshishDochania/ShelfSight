import cv2
import numpy as np

class ImageProcessor:
    def __init__(self):
        pass

    def preprocess_image(self, image):
        # Resize image to a standard size
        resized = cv2.resize(image, (640, 480))
        # Convert to grayscale
        gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)
        # Apply Gaussian blur
        blurred = cv2.GaussianBlur(gray, (5, 5), 0)
        return blurred

    def detect_edges(self, image):
        # Apply Canny edge detection
        edges = cv2.Canny(image, 100, 200)
        return edges

    def process_shelf_image(self, image):
        preprocessed = self.preprocess_image(image)
        edges = self.detect_edges(preprocessed)
        # Further processing can be added here
        return edges
