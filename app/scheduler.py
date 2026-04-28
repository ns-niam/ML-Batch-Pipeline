import schedule
import time
import os

def run_pipeline():
    os.system(
      "python app/batch_predict.py"
    )

schedule.every(1).minutes.do(
    run_pipeline
)

print("Scheduler running...")

while True:
    schedule.run_pending()
    time.sleep(1)