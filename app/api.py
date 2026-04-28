from fastapi import FastAPI
import joblib

app = FastAPI()

model = joblib.load(
 "models/model.pkl"
)

@app.get("/")
def home():
    return {
      "message":"ML API Running"
    }

@app.get("/predict")
def predict(
 f1: float,
 f2: float,
 f3: float,
 f4: float
):

    pred = int(
       model.predict(
         [[f1,f2,f3,f4]]
       )[0]
    )

    return {
      "prediction": pred
    }