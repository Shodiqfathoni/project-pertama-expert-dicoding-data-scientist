import joblib
import numpy as np
import pandas as pd

encoder_Business_Travel = joblib.load("model/encoder_Business Travel.joblib")
encoder_Department = joblib.load("model/encoder_Department.joblib")
encoder_Education = joblib.load("model/encoder_Education.joblib")
encoder_Education_Field = joblib.load("model/encoder_Education Field.joblib")
encoder_Environment_Satisfaction = joblib.load("model/encoder_Environment Satisfaction.joblib")
encoder_Gender = joblib.load("model/encoder_Gender.joblib")
encoder_Job_Involvement = joblib.load("model/encoder_Job Involvement.joblib")
encoder_Job_Role = joblib.load("model/encoder_Job Role.joblib")
encoder_Job_Satisfaction = joblib.load("model/encoder_Job Satisfaction.joblib")
encoder_Marital_Status = joblib.load("model/encoder_Marital Status.joblib")
encoder_Over_Time = joblib.load("model/encoder_Over Time.joblib")
encoder_Performance_Rating = joblib.load("model/encoder_Performance Rating.joblib")
encoder_Relationship_Satisfaction = joblib.load("model/encoder_Relationship Satisfaction.joblib")
encoder_Work_Life_Balance = joblib.load("model/encoder_Work Life Balance.joblib")
pca_1 = joblib.load("model/pca_1.joblib")
pca_2 = joblib.load("model/pca_2.joblib")
scaler_Age = joblib.load("model/scaler_Age.joblib")
scaler_Job_Level = joblib.load("model/scaler_Job Level.joblib")
scaler_Monthly_Income = joblib.load("model/scaler_Monthly Income.joblib")
scaler_Total_Working_Years = joblib.load("model/scaler_Total Working Years.joblib")
scaler_Years_At_Company = joblib.load("model/scaler_Years At Company.joblib")
scaler_Years_In_Current_Role = joblib.load("model/scaler_Years In Current Role.joblib")
scaler_Years_Since_Last_Promotion = joblib.load("model/scaler_Years Since Last Promotion.joblib")
scaler_Years_With_Curr_Manager = joblib.load("model/scaler_Years With Curr Manager.joblib")

pca_numerical_columns_1 = [
    'Age',
    'Job Level',
    'Monthly Income',
    'Total Working Years'
]

pca_numerical_columns_2 = [
    'Years At Company',
    'Years In Current Role',
    'Years Since Last Promotion',
    'Years With Curr Manager'
]

def data_preprocessing(data):
    """Preprocessing data

    Args:
        data (Pandas DataFrame): Dataframe that contain all the data to make prediction

    return:
        Pandas DataFrame: Dataframe that contain all the preprocessed data
    """
    data = data.copy()
    df = pd.DataFrame()


    df["Business Travel"] = encoder_Business_Travel.transform(data["Business Travel"])
    df["Department"] = encoder_Department.transform(data["Department"])
    df["Education"] = encoder_Education.transform(data["Education"])
    df["Education Field"] = encoder_Education_Field.transform(data["Education Field"])
    df["Environment Satisfaction"] = encoder_Environment_Satisfaction.transform(data["Environment Satisfaction"])
    df["Gender"] = encoder_Gender.transform(data["Gender"])
    df["Job Involvement"] = encoder_Job_Involvement.transform(data["Job Involvement"])
    df["Job Role"] = encoder_Job_Role.transform(data["Job Role"])
    df["Job Satisfaction"] = encoder_Job_Satisfaction.transform(data["Job Satisfaction"])
    df["Marital Status"] = encoder_Marital_Status.transform(data["Marital Status"])
    df["Over Time"] = encoder_Over_Time.transform(data["Over Time"])
    df["Performance Rating"] = encoder_Performance_Rating.transform(data["Performance Rating"])
    df["Relationship Satisfaction"] = encoder_Relationship_Satisfaction.transform(data["Relationship Satisfaction"])
    df["Work Life Balance"] = encoder_Work_Life_Balance.transform(data["Work Life Balance"])

    # PCA 1
    data["Age"] = scaler_Age.transform(np.asarray(data["Age"]).reshape(-1, 1)).flatten()
    data["Job Level"] = scaler_Job_Level.transform(np.asarray(data["Job Level"]).reshape(-1, 1)).flatten()
    data["Monthly Income"] = scaler_Monthly_Income.transform(np.asarray(data["Monthly Income"]).reshape(-1, 1)).flatten()
    data["Total Working Years"] = scaler_Total_Working_Years.transform(np.asarray(data["Total Working Years"]).reshape(-1, 1)).flatten()


    df[["pc1_1"]] = pca_1.transform(data[pca_numerical_columns_1])

    # PCA 2
    data["Years At Company"] = scaler_Years_At_Company.transform(np.asarray(data["Years At Company"]).reshape(-1, 1)).flatten()
    data["Years In Current Role"] = scaler_Years_In_Current_Role.transform(np.asarray(data["Years In Current Role"]).reshape(-1, 1)).flatten()
    data["Years Since Last Promotion"] = scaler_Years_Since_Last_Promotion.transform(np.asarray(data["Years Since Last Promotion"]).reshape(-1, 1)).flatten()
    data["Years With Curr Manager"] = scaler_Years_With_Curr_Manager.transform(np.asarray(data["Years With Curr Manager"]).reshape(-1, 1)).flatten()


    df[["pc2_1"]] = pca_2.transform(data[pca_numerical_columns_2])

    return df