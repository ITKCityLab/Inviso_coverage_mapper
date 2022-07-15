import uvicorn
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
import json
from src import api_schema
from src.database import models, crud
from src.database.database import SessionLocal, engine
from fastapi.exception_handlers import request_validation_exception_handler
from fastapi.exceptions import RequestValidationError

models.Base.metadata.create_all(bind=engine)

app = FastAPI(version="0.0.3")

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/iot/")
def create_transmission(t: api_schema.Transmission, db: Session = Depends(get_db)) -> int:
    """
    Receive HTTP body (data json) shaped like Transmission.
    :param t: json body
    :param db: database session
    :return: new sql row ID after insert
    """
    db_transmission_id = crud.create_transmission(db, t=t)
    return db_transmission_id

@app.get("/iot/{transmission_id}", response_model=api_schema.TransmissionRecord)
def read_transmission(transmission_id: int, db: Session = Depends(get_db)):
    db_transmission = crud.get_transmission(db,transmission_id)
    if db_transmission is None:
        raise HTTPException(status_code=404, detail=f"Signal id '{transmission_id}' not found.")
    db_transmission.transmission = json.loads(db_transmission.transmission)
    return db_transmission

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exc):
    """ Print validation error to help debugging HTTP error 422 when response is not available to user."""
    print(f"Validation exceptioN: '{exc}'.")
    return await request_validation_exception_handler(request, exc)


if __name__ == "__main__":
    # for development
    uvicorn.run(app, host="127.0.0.1")