class Assesment:
    def __ini__(self, data):
        self.data = data
    
    async def get_health_score(self):
        return self.data
    
    async def get_health_risks(self):
        return self.data
    
    async def get_health_recommendations(self):
        return self.data