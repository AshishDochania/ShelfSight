# ShelfSight AI

**ShelfSight AI** is an AI-powered retail shelf monitoring system designed to enhance inventory management. It leverages computer vision and AI to provide real-time insights into stock levels, automate shelf monitoring, and optimize restocking processes.

---

## Table of Contents
- [Features](#features)
- [File Structure](#file-structure)
- [How to Run the Project](#how-to-run-the-project)
  - [Backend Setup (FastAPI)](#1-backend-setup-fastapi)
  - [Frontend Setup (React)](#2-frontend-setup-react)
  - [Running Tests](#3-running-tests)
- [API Endpoints](#api-endpoints)
- [Frontend Features](#frontend-features)
- [Technologies Used](#technologies-used)
- [Future Enhancements](#future-enhancements)

---

## Features
- **Real-Time Monitoring**: Detects stock levels, out-of-stock items, and misplaced products using computer vision.
- **AI Analysis**: Predicts demand trends and detects anomalies in inventory data.
- **Dashboard**: Displays store layout, key metrics, tasks, and analytics.
- **Task Management**: Automates task assignments for restocking and shelf management.

---

## How to Run the Project

### 1. Backend Setup (FastAPI)

#### Prerequisites:
- Python 3.8 or higher installed

#### Steps:
1. Navigate to the backend directory:
    ```
    cd shelfsight-ai/src/api
    ```

2. Install dependencies:
    ```
    pip install fastapi uvicorn pydantic numpy scikit-learn opencv-python
    ```

3. Run the FastAPI server:
    ```
    uvicorn main:app --reload --host 0.0.0.0 --port 8000
    ```

4. Access the API documentation:
    - Open your browser and go to [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) for interactive API documentation.

---

### 2. Frontend Setup (React)

#### Prerequisites:
- Node.js and npm installed

#### Steps:
1. Navigate to the frontend directory:
    ```
    cd shelfsight-ai/src/frontend
    ```

2. Install dependencies:
    ```
    npm install
    ```

3. Start the development server:
    ```
    npm start
    ```

4. Access the frontend dashboard:
    - Open your browser and go to [http://localhost:3000](http://localhost:3000).

---

### 3. Running Tests

#### Prerequisites:
- `pytest` installed for Python tests

#### Steps:

1. Navigate to the project root directory:
    ```
    cd shelfsight-ai/
    ```

2. Run all tests:
    ```
    pytest tests/
    ```

3. View detailed test results:
    ```
    pytest -v tests/
    ```

---

## API Endpoints

### Root Endpoint:
- `GET /`
  - Returns a welcome message.

### Shelf Status Endpoints:
- `GET /shelf_status`
  - Returns a list of all shelves with their stock levels.
- `GET /shelf_status/{shelf_id}`
  - Returns details of a specific shelf by ID.

### Task Management Endpoints:
- `GET /tasks`
  - Returns a list of all tasks.
- `GET /tasks/{task_id}`
  - Returns details of a specific task by ID.

---

## Frontend Features

The frontend dashboard provides an intuitive interface for managing inventory:

1. **Dashboard**:
   - Displays store layout with color-coded shelves (green, yellow, red) based on stock levels.
   - Shows key metrics like out-of-stock items and planogram compliance.

2. **Shelf Detail View**:
   - Provides detailed information about a specific shelf, including product placements and stock levels.

3. **Task Management**:
   - Lists tasks such as restocking or cleaning with priority indicators (high/medium/low).

4. **Analytics Dashboard**:
   - Offers insights into inventory trends, sales impact, and demand forecasting.

---

## Technologies Used

### Backend:
- FastAPI for API development
- NumPy for numerical computations
- Scikit-learn for machine learning models (demand prediction and anomaly detection)
- OpenCV for image processing

### Frontend:
- React for building the user interface
- React Router for navigation between pages

### Testing:
- Pytest for backend testing

---

## Future Enhancements

1. **Database Integration**: Add support for persistent storage using PostgreSQL or MongoDB.
2. **Advanced Computer Vision**: Use YOLOv5 or another advanced object detection model for better accuracy.
3. **Mobile App**: Develop a mobile app version for store staff.
4. **Cloud Deployment**: Deploy the system on AWS or Azure for scalability.

---

This README provides all necessary instructions to set up, run, and test the ShelfSight AI system locally. For any issues or contributions, feel free to open a pull request or raise an issue in this repository!