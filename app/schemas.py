from pydantic import BaseModel


class PredictionInput(BaseModel):

    year: int
    round: int
    driverId: int
    constructorId: int
    circuitId: int
    grid: float
    qualifying_position: float