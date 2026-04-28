import sqlite3

conn = sqlite3.connect("ml_pipeline.db")
cursor = conn.cursor()

with open("sql/schema.sql","r") as file:
    cursor.executescript(
        file.read()
    )

sample_data = [
(1,5.1,3.5,1.4,0.2),
(2,6.2,3.4,5.4,2.3),
(3,5.9,3.0,4.2,1.5)
]

cursor.executemany(
"""
INSERT INTO input_data
VALUES (?,?,?,?,?)
""",
sample_data
)

conn.commit()

print("Database and sample data created")