CREATE TABLE input_data(
id INTEGER PRIMARY KEY,
feature1 REAL,
feature2 REAL,
feature3 REAL,
feature4 REAL
);

CREATE TABLE predictions(
id INTEGER,
prediction INTEGER,
prediction_timestamp TEXT
);