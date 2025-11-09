import multiprocessing as mp
if __name__ == '__main__':
    mp.set_start_method('spawn')

from fastapi import FastAPI, Form
from transformers import AutoTokenizer, AutoModelForCausalLM
from fastapi.middleware.cors import CORSMiddleware
import torch
import json
import uvicorn

# Load config from file
with open("conf/config.json", "r") as f:
    config = json.load(f)


app = FastAPI()

model = None
tokenizer = None


# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

async def startup():
    global model, tokenizer  


    # Load model and tokenizer (use float16 for efficiency; device_map='auto' to utilize available hardware)
    # model_id = "brucewayne0459/OpenBioLLm-Derm"
    model_id = config["model_id"]
    model = AutoModelForCausalLM.from_pretrained(model_id, dtype=torch.float16, device_map="cpu")
    tokenizer = AutoTokenizer.from_pretrained(model_id)

app.add_event_handler("startup", startup)


@app.post("/predict")
async def predict(prompt: str = Form(...)):
    
    # Prepare inputs as conversation (LLaVA format)
    inputs = tokenizer(prompt, return_tensors="pt").to(model.device)
    outputs = model.generate(**inputs, max_new_tokens=200)
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
        
    return {"response": response}

if __name__ == "__main__": 
    #u Use config for host/port
    uvicorn.run(app, host=config["host"], port=config["backend_port"])