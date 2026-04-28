from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
import joblib
import os

# make sure models folder exists
os.makedirs("models", exist_ok=True)

# load sample data
iris = load_iris()

X = iris.data
y = iris.target

# train model
model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model.fit(X,y)

# save model
joblib.dump(
    model,
    "models/model.pkl"
)

print("Model trained and saved successfully")