import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression

class SymptomChecker:

    def __init__(self, symptoms):
        self.symptoms = symptoms

    def predict_disease(self):
        # Load the disease dataset
        diseases = pd.read_csv("diseases.csv")

        # Create a list of symptoms for each disease
        symptom_lists = diseases["symptoms"].apply(lambda x: x.split(","))

        # Create a list of disease labels
        disease_labels = diseases["disease"]

        # Create a logistic regression model
        model = LogisticRegression()

        # Fit the model to the data
        model.fit(symptom_lists, disease_labels)

        # Predict the disease for the given symptoms
        prediction = model.predict_proba([self.symptoms])[0]

        # Get the index of the disease with the highest probability
        disease_index = np.argmax(prediction)

        # Return the name of the disease
        return diseases["disease"].iloc[disease_index]

