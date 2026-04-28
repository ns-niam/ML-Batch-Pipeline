import sqlite3

conn=sqlite3.connect("ml_pipeline.db")
c=conn.cursor()

c.execute("""
CREATE TABLE IF NOT EXISTS input_data(
id INTEGER PRIMARY KEY,
feature1 REAL,
feature2 REAL,
feature3 REAL,
feature4 REAL
)
""")

c.execute("""
CREATE TABLE IF NOT EXISTS predictions(
id INTEGER,
prediction INTEGER,
prediction_timestamp TEXT

