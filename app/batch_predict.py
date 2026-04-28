import sqlite3
import joblib
from datetime import datetime

conn = sqlite3.connect("ml_pipeline.db")
c = conn.cursor()

c.execute("DELETE FROM predictions")

model = joblib.load("models/model.pkl")

# read input data
rows = c.execute(
"""
SELECT * FROM input_data
"""
).fetchall()

for row in rows:

    record_id = row[0]

    features = [list(row[1:])]

    prediction = int(
        model.predict(features)[0]
    )

    c.execute(
    """
    INSERT INTO predictions
    VALUES (?,?,?)
    """,
    (
      record_id,
      prediction,
      str(datetime.now())
    )
    )

conn.commit()

print("Batch predictions inserted successfully")