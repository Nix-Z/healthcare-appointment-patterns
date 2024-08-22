import pandas as pd
import numpy as np
from sklearn.utils import resample
from sklearn.preprocessing import StandardScaler, LabelEncoder
from datavisualization import visualize_data

def engineer_features():
    data = visualize_data()

    # Initialize a LabelEncoder
    label_encoders = {}
    specific_features = ['Gender', 'Insurance_Type', 'Chronic_Disease', 'Mental_Health_Status',
       'Employment_Status', 'Education_Level', 'Transportation_Access',
       'Area_Type', 'Appointment_Outcome']
    
    # Convert categorical feature values to numerical values using LabelEncoder
    for feature in specific_features:
        le = LabelEncoder()
        data[feature] = le.fit_transform(data[feature])
        label_encoders[feature] = le  # Store the label encoder if needed later
        unique_values = le.classes_

    print(data.head())

    data.to_csv('healthcare_dataset_cleansed_data.csv', index=False)
    
    return data

engineer_features()
