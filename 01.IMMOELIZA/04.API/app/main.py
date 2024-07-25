from fastapi import FastAPI, HTTPException
from pydantic import BaseModel


app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI app."}


class Item(BaseModel):
    name: str
    description: str = None
    price: float
    tax: float = None

@app.post("/items/")
def create_item(item: Item):
    return {"item": item}

@app.get("/multiply/{number}")
def multiply_number(number: int):
    return {"result": number * 2}

class Compensation(BaseModel):
    salary: float
    bonus: float
    taxes: float

@app.post("/compute/")
def compute_compensation(compensation: Compensation):
    if not all(isinstance(value, (int, float)) for value in [compensation.salary, compensation.bonus, compensation.taxes]):
        raise HTTPException(status_code = 400, detail = "All values must be numbers.")
    result = compensation.salary + compensation.bonus - compensation.taxes
    return {"result": result}