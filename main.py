from fastapi import FastAPI, HTTPException
import os 
import logging
from datetime import datetime
from utils.helper import Prompt, process_prompt
import pickle
import base64
app = FastAPI()

@app.post("/prompt/")
async def process_prompt(prompt: Prompt):
    try:
        assert prompt is not None

        out = process_prompt(prompt)
        # with open('sample_output.pkl', 'rb') as f:
        #     out = pickle.load(f)
            out = base64.b64encode(out)
        return {'Ouput':out}

    except Exception as e:
        
        logging.error(f"Error Process Prompt, {datetime.now()}, Error- {e}")
        return HTTPException(status_code=500, detail="Internal Server Error, Request Failed")


