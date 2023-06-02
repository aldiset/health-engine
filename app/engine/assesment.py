from pandas import DataFrame
from app.engine.engine import HealthEngine

class Assesment:
    def __ini__(self, dataframe: DataFrame):
        self.dataframe = dataframe
        self.health_engine = HealthEngine(dataframe=self.dataframe)
    
    async def get_health_score(self):
        prompt = "Berapa score kesehatan yang saya miliki ?"
        return await self.health_engine.run(prompt=prompt)
    
    async def get_health_risks(self):
        prompt = "Bagaimana resiko kesahatan saya ?"
        return await self.health_engine.run(prompt=prompt)
    
    async def get_health_recommendations(self):
        prompt = "Rekomendasi terkait resiko dan pola hidup yang sehat ?"
        return await self.health_engine(prompt=prompt)