import pandas as pd
from data_analysis import analyze_data

def preprocess_data():
    data, categorical_features, numerical_features = analyze_data()

    # Remove rows with any empty values
    data = data.dropna().reset_index(drop=True)

    # Changing from float to int
    data['Age'] = data['Age'].astype(int)
    data['Distance_from_Facility'] = data['Distance_from_Facility'].astype(int)

    # Convert 'Booking_Date' and 'Appointment_Date' to datetime objects
    data['Booking_Date'] = pd.to_datetime(data['Booking_Date'], format="%Y-%m-%d")
    data['Appointment_Date'] = pd.to_datetime(data['Appointment_Date'], format="%Y-%m-%d")

    # Calculate the difference in days between 'Booking_Date' and 'Appointment_Date'
    data['Days_Between'] = (data['Appointment_Date'] - data['Booking_Date']).dt.days

    # Drop unnecessary rows 
    data.drop(['Patient_ID', 'Booking_Date', 'Appointment_Date'], axis=1, inplace=True)

    print(data.head())

    categorical_features = data.select_dtypes("object").columns
    numerical_features = data.select_dtypes("number").columns

    return data, categorical_features, numerical_features

preprocess_data()
