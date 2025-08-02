from fastapi import FastAPI
from pydantic import BaseModel
from typing import List


app = FastAPI()

class Tea(BaseModel):
    id:int
    name: str
    origin : str

teas: list[Tea] = []

@app.get("/")
def read_root():
    return {"message": "Welcome to the Tea API"}

@app.get("/teas")
def get_teas():
    return teas

@app.post("/teas")
def add_teas(tea: Tea):
    teas.append(tea)
    return {"message": "Tea added successfully", "tea": tea}

@app.put("/teas/{tea_id}")
def update_tea(tea_id: int, updated_tea: Tea):
    for index, tea in enumerate(teas):
        if(tea.id == tea_id):
            teas[index] = updated_tea
            return {"message": "Tea updated successfully", "tea": updated_tea}
    return {"message": "Tea not found"}, 404

@app.delete("/teas/{tea_id}")
def delete_tea(tea_id: int):
    for index, tea in enumerate(teas):
        if(tea.id == tea_id):
            deleted_tea = teas.pop(index)
            return {"message": "Tea deleted successfully", "tea": deleted_tea}
    return {"message": "Tea not found"}, 404

@app.get("/teas/{tea_id}")
def get_tea(tea_id: int):
    for tea in teas:
        if tea.id == tea_id:
            return tea
    return {"message": "Tea not found"}, 404
