from pydantic import BaseModel
from typing import List
from datetime import datetime

"""
Pydantic models.

Definition of the sensor data from an IOT device.
The required values in these classes are used for visualising signal quality. 
"""
class TransmitterData(BaseModel):
    """Tramsmitter/sensor location"""
    latitudeDeg: float
    longitudeDeg: float

class GatewayLocation(BaseModel):
    """ Gateway/antenna location"""
    altitude: int
    latitude: float
    longitude: float

class TxInfo(BaseModel):
    """ signal quality """
    frequency: int
    dr: int

class RxInfo(BaseModel):
    """
    Antenna info.
    RxInfo is received as a list of dicts.
    This class represents the dict.
    """
    rssi: int
    name: str
    time: str
    loRaSNR: float
    location: GatewayLocation
    gatewayID: str



class Transmission(BaseModel):
    adr: bool
    devEUI: str
    rxInfo: List[RxInfo]
    txInfo: TxInfo
    data: TransmitterData
    deviceName: str

"""
My first pydantic-db model.
Think CRUD?
One class for each. Base class because it represents the core of the object.
"""

class TransmissionRecord(BaseModel):
    id: int
    inserted: datetime
    transmission: Transmission

    class Config:
        orm_mode = True
