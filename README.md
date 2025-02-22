ShelfSight AI
ShelfSight AI is an AI-powered retail shelf monitoring system that uses computer vision and AI to enhance inventory management. It provides real-time insights into stock levels, automates shelf monitoring, and ensures efficient restocking processes.

Features
Computer Vision: Detects objects and processes shelf images to estimate stock levels.

AI Analysis: Predicts product demand and detects anomalies in inventory data.

API: Provides endpoints for shelf status, tasks, and other functionalities.

Frontend Dashboard: Displays store layout, key metrics, tasks, and analytics.

Testing: Comprehensive tests for backend APIs, computer vision, and AI analysis.

File Structure
text
shelfsight-ai/
├── src/
│   ├── computer_vision/
│   │   ├── __init__.py
│   │   ├── image_processor.py
│   │   └── object_detector.py
│   ├── ai_analysis/
│   │   ├── __init__.py
│   │   ├── demand_predictor.py
│   │   └── anomaly_detector.py
│   ├── api/
│   │   ├── __init__.py
│   │   ├── main.py
│   │   └── routes/
│   │       ├── __init__.py
│   │       ├── shelf_status.py
│   │       └── tasks.py
├── tests/
│   ├── test_computer_vision.py
│   ├── test_ai_analysis.py
│   └── test_api.py
How to Run the Project
1. Backend Setup (FastAPI)
Prerequisites:
Python 3.8 or higher installed

Steps:
Navigate to the project directory:

bash
cd shelfsight-ai/src/api
Install dependencies:

bash
pip install fastapi uvicorn pydantic numpy scikit-learn opencv-python
Run the FastAPI server:

bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
Access the API documentation:

Open your browser and go to http://127.0.0.1:8000/docs for interactive API documentation.

2. Frontend Setup (React)
Prerequisites:
Node.js and npm installed

Steps:
Navigate to the frontend directory:

bash
cd shelfsight-ai/src/frontend
Install dependencies:

bash
npm install
Start the development server:

bash
npm start
Access the frontend dashboard:

Open your browser and go to http://localhost:3000.

3. Running Tests
Prerequisites:
pytest installed for Python tests

Steps:
Navigate to the project root directory:

bash
cd shelfsight-ai/
Run all tests:

bash
pytest tests/
View detailed test results:

bash
pytest -v tests/
API Endpoints
Root Endpoint:
GET /

Returns a welcome message.

Shelf Status Endpoints:
GET /shelf_status

Returns a list of all shelves with their stock levels.

GET /shelf_status/{shelf_id}

Returns details of a specific shelf by ID.

Task Management Endpoints:
GET /tasks

Returns a list of all tasks.

GET /tasks/{task_id}

Returns details of a specific task by ID.

Frontend Features
The frontend dashboard provides an intuitive interface for managing inventory:

Dashboard:

Displays store layout with color-coded shelves (green, yellow, red) based on stock levels.

Shows key metrics like out-of-stock items and planogram compliance.

Shelf Detail View:

Provides detailed information about a specific shelf, including product placements and stock levels.

Task Management:

Lists tasks such as restocking or cleaning with priority indicators (high/medium/low).

Analytics Dashboard:

Offers insights into inventory trends, sales impact, and demand forecasting.

Technologies Used
Backend:
FastAPI for API development

NumPy for numerical computations

Scikit-learn for machine learning models (demand prediction and anomaly detection)

OpenCV for image processing

Frontend:
React for building the user interface

React Router for navigation between pages

Testing:
Pytest for backend testing

Future Enhancements
Database Integration: Add support for persistent storage using PostgreSQL or MongoDB.

Advanced Computer Vision: Use YOLOv5 or another advanced object detection model for better accuracy.

Mobile App: Develop a mobile app version for store staff.

Cloud Deployment: Deploy the system on AWS or Azure for scalability.

This README provides all necessary instructions to set up, run, and test the ShelfSight AI system locally. For any issues or contributions, feel free to open a pull request or raise an issue in this repository!