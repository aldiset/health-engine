from pydantic import BaseModel

class HealthAssessmentSchema(BaseModel):
    bmi: int
    user_id: int
    heart_rate: int
    blood_pressure: int
    glucose_levels: int 
    sleep_patterns: int
    exercise_habits: int
    cholesterol_levels: int
    dietary_information: int