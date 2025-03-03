from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "¡Hola, FastAPI con Docker y Git en MacOS!"}

@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id, "value": f"Valor del ítem {item_id}"}

