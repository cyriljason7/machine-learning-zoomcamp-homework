import pickle

from fastapi import FastAPI
from typing import Dict, Any
import uvicorn

#api app
app = FastAPI(title = 'leadscore-prediction')

with open('pipeline_v2.bin','rb') as f_in:
   pipeline = pickle.load(f_in)

def predict_leadscore(client):
    result = pipeline.predict_proba(client)[0,1]
    return float(result)


@app.post("/prediction")
def predict(client : Dict[str, Any]):
    score = predict_leadscore(client)

    return {'leadscore': score
           }


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=9696)