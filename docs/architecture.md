# System Architecture

## Overview
The system processes sensor data and predicts machine failures using machine learning.

---

## Flow

Sensor Data → Preprocessing → Feature Engineering → Model → Prediction → Alert → Visualization

---

## Modules

### 1. Data Collection
- Simulated IoT sensor data
- CSV dataset

### 2. Data Preprocessing
- Handling missing values
- Removing duplicates

### 3. Feature Engineering
- Rolling averages
- Trend analysis

### 4. Model Training
- Random Forest classifier
- Train-test split

### 5. Prediction System
- Predict failure (0/1)
- Generate probability

### 6. Alert System
- NORMAL
- WARNING
- CRITICAL

### 7. Visualization
- Temperature trends
- Failure distribution

---

## Summary
This architecture simulates a real-world predictive maintenance system.