from pydantic import BaseModel


class TrackerAndAnalyticSchema(BaseModel):
    body_weight: int
    blood_pressure: int
    heart_rate: int
    sleep_patterns: int 
    exercise_activities: int
    dietary_intake: int
    other: dict = None