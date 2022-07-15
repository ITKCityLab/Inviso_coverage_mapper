from sqlalchemy.orm import Session
from src import api_schema
from src.database import models
import json

def create_transmission(db: Session, t: api_schema.Transmission) -> int:
    string_data = json.dumps(t.dict()) # Pydantic model -> dict -> string.
    db_transmission = models.Transmissions(transmission=string_data)
    db.add(db_transmission)
    db.commit() # TODO consider doing an update of the db_device object. See FastAPI sql tutorial. Might not have the most updated data in local ORM object?
    return db_transmission.id

def get_transmission(db: Session, transmission_id: int):  # -> models.Signal | List[None]
    return db.query(models.Transmissions).filter(models.Transmissions.id == transmission_id).first()
