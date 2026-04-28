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
)
""")

sample_data=[
(1,5.1,3.5,1.4,0.2),
(2,6.2,3.4,5.4,2.3),
(3,5.9,3.0,4.2,1.5)
]

c.executemany(
"""
INSERT OR REPLACE INTO input_data
VALUES (?,?,?,?,?)
""",
sample_data
)

conn.commit()

print("Database and sample data created")