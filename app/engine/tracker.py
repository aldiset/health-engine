import pandas as pd
import pandas_ai as pai

class HealthTracker:

    def __init__(self):
        self.data = pd.DataFrame()

    async def add_data(self, data):
        self.data = self.data.append(data, ignore_index=True)

    async def get_data(self):
        return self.data

    async def analyze_data(self):
        # Analyze the data using AI
        results = pai.analyze(self.data)

        # Return the results
        return results

