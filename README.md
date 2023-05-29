# Health Engine

Health Engine is a software system that combines artificial intelligence (AI) techniques, specifically leveraging the capabilities of Pandas AI, with health-related data to provide various functionalities aimed at improving individual health and well-being.

## Features

The Health Engine incorporates the following key features:

1. **Personalized Health Assessment**: The system performs personalized health assessments by analyzing user-provided data. It employs AI algorithms to evaluate health metrics, such as BMI, blood pressure, cholesterol levels, and more. Based on the analysis, the engine generates personalized insights and recommendations for the user's overall health status, potential risk factors, and suggestions for improvement.

2. **AI-Powered Symptom Checker**: The Health Engine utilizes advanced AI algorithms to enable a symptom checker functionality. Users can input their symptoms, and the engine employs machine learning techniques to identify potential diseases or conditions associated with those symptoms. This helps users get a preliminary understanding of possible health issues and facilitates informed decision-making.

3. **Health Tracker and Analytics**: The system allows users to track and monitor their health-related data over time. Users can record and analyze various health metrics, such as weight, exercise habits, sleep patterns, and more. The Health Engine provides analytics and visualizations to help users gain insights into their health trends, progress, and areas for improvement.

## Installation

To install and run the Health Engine locally, follow these steps:

1. Clone the repository:

   ```bash
   git clone https://github.com/aldiset/health-engine.git
   ```

2. Install the required dependencies:

   ```bash
   pipenv install 
   ```

3. Configure the necessary environment variables, if any.


4. Start the Health Engine application (default run on port 8000):

   ``` 
   pipenv run uvicorn main:app 
   ```