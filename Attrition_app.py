import streamlit as st
import pandas as pd
import joblib
from data_preprocessing import data_preprocessing
from data_preprocessing import (
    encoder_Business_Travel, 
    encoder_Department, 
    encoder_Education,
    encoder_Education_Field, 
    encoder_Environment_Satisfaction, 
    encoder_Gender,
    encoder_Job_Involvement, 
    encoder_Job_Role, 
    encoder_Job_Satisfaction, 
    encoder_Marital_Status,
    encoder_Over_Time, 
    encoder_Performance_Rating, 
    encoder_Relationship_Satisfaction,
    encoder_Work_Life_Balance
)
from prediction import prediction

col1, col2 = st.columns([1, 5])
with col1:
    st.image("https://github.com/dicodingacademy/assets/raw/main/logo.png", width=130)
with col2:
    st.header('Attrition analysis App (Prototype)')
data = pd.DataFrame()

col1, col2, col3, col4 = st.columns(4)

with col1:
    Business_Travel = st.selectbox(label='Business Travel', options=encoder_Business_Travel.classes_, index=1)
    data["Business Travel"] = [Business_Travel]

with col2:
    Department = st.selectbox(label='Department', options=encoder_Department.classes_, index=1)
    data["Department"] = [Department]

with col3:
    Education = st.selectbox(label='Education', options=encoder_Education.classes_, index=1)
    data["Education"] = [Education]

with col4:
    Education_Field = st.selectbox(label='Education Field', options=encoder_Education_Field.classes_, index=1)
    data["Education Field"] = [Education_Field]

col1, col2, col3, col4 = st.columns(4)

with col1:
    Environment_Satisfaction = st.selectbox(label='Environment Satisfaction', options=encoder_Environment_Satisfaction.classes_, index=1)
    data["Environment Satisfaction"] = [Environment_Satisfaction]

with col2:
    Gender = st.selectbox(label='Gender', options=encoder_Gender.classes_, index=1)
    data["Gender"] = [Gender]

with col3:
    Job_Involvement = st.selectbox(label='Job Involvement', options=encoder_Job_Involvement.classes_, index=1)
    data["Job Involvement"] = [Job_Involvement]

with col4:
    Job_Role = st.selectbox(label='Job Role', options=encoder_Job_Role.classes_, index=1)
    data["Job Role"] = [Job_Role]

col1, col2, col3, col4 = st.columns(4)

with col1:
    Job_Satisfaction = st.selectbox(label='Job Satisfaction', options=encoder_Job_Satisfaction.classes_, index=1)
    data["Job Satisfaction"] = [Job_Satisfaction]

with col2:
    Marital_Status = st.selectbox(label='Marital Status', options=encoder_Marital_Status.classes_, index=1)
    data["Marital Status"] = [Marital_Status]

with col3:
    Over_Time = st.selectbox(label='Over Time', options=encoder_Over_Time.classes_, index=1)
    data["Over Time"] = [Over_Time]

with col4:
    Performance_Rating = st.selectbox(label='Performance Rating', options=encoder_Performance_Rating.classes_, index=1)
    data["Performance Rating"] = [Performance_Rating]

col1, col2 = st.columns(2)

with col1:
    Relationship_Satisfaction = st.selectbox(label='Relationship Satisfaction', options=encoder_Relationship_Satisfaction.classes_, index=1)
    data["Relationship Satisfaction"] = [Relationship_Satisfaction]

with col2:
    Work_Life_Balance = st.selectbox(label='Work Life Balance', options=encoder_Work_Life_Balance.classes_, index=1)
    data["Work Life Balance"] = [Work_Life_Balance]

col1, col2, col3, col4 = st.columns(4)

with col1:
    Age = float(st.number_input(label='Age', value=0))
    data["Age"] = [Age]

with col2:
    Job_Level = float(st.number_input(label='Job Level', value=0))
    data["Job Level"] = [Job_Level]

with col3:
    Monthly_Income = float(st.number_input(label='Monthly Income', value=0))
    data["Monthly Income"] = [Monthly_Income]

with col4:
    Total_Working_Years = float(st.number_input(label='Total Working Years', value=0))
    data["Total Working Years"] = [Total_Working_Years]

col1, col2, col3, col4 = st.columns(4)

with col1:
    Years_At_Company = float(st.number_input(label='Years At Company', value=0))
    data["Years At Company"] = [Years_At_Company]

with col2:
    Years_In_Current_Role = float(st.number_input(label='Years In Current Role', value=0))
    data["Years In Current Role"] = [Years_In_Current_Role]

with col3:
    Years_Since_Last_Promotion = float(st.number_input(label='Years Since Last Promotion', value=0))
    data["Years Since Last Promotion"] = [Years_Since_Last_Promotion]

with col4:
    Years_With_Curr_Manager = float(st.number_input(label='Years With Curr Manager', value=0))
    data["Years With Curr Manager"] = [Years_With_Curr_Manager]

with st.expander("View the Raw Data"):
    st.dataframe(data=data, width=800, height=10)

if st.button('Predict'):
    new_data = data_preprocessing(data=data)
    with st.expander("View the Preprocessed Data"):
        st.dataframe(data=new_data, width=800, height=10)
    
    prediction_result = prediction(new_data)
    
    # Tampilkan prediksi dengan elemen yang sesuai
    if prediction_result == 'stay':
        st.success(f"In my prediction, Employee will be: {prediction_result.capitalize()}")
    else:
        st.error(f"In my prediction, Employee will be: {prediction_result.capitalize()}")
