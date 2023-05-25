from pydantic import BaseModel


class SymptomList(BaseModel):
    fever: int
    headache: int
    cough: int 
    fatigue: int 
    sore_throat: int  
    muscle_pain: int 
    shortness_of_breath: int


class DurationOfSymptoms(SymptomList):
    pass 


class SeverityOfSymptoms(SymptomList):
    pass 