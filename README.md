# ML Batch Pipeline

Production-style automated batch prediction pipeline built with Python and SQLite.

## Features
- Batch inference pipeline
- Reads data from database
- Loads trained ML model
- Stores predictions back into database
- Scheduled automated execution
- Internship-style mini MLOps project

## Tech Stack
- Python
- Scikit-learn
- SQLite
- Joblib
- Schedule

## Project Structure

```bash
app/
 ├── train.py
 ├── database.py
 ├── batch_predict.py
 └── scheduler.py

models/
 └── model.pkl

sql/
 └── schema.sql
```

## Run Project

Train model
```bash
python app/train.py
```

Create database
```bash
python app/database.py
```

Run batch prediction
```bash
python app/batch_predict.py
```
er.py
```

## Pipeline Flow
Input Data → Model Prediction → Predictions Table → Scheduled Batch Runs

## Author
Niam
AI Engneering student