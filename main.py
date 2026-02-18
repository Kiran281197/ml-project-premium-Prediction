import streamlit as st
from prediction_helper import predict
import numpy as np

st.title("Health Insurance Prediciton App")

categorical_options = {
            "gender" : ['Male', 'Female'],
            "region" : ['Northwest', 'Southeast', 'Northeast', 'Southwest'],
            "marital_status" : ['Unmarried' ,'Married'],
            "bmi_category" : ['Normal' ,'Obesity' ,'Overweight', 'Underweight'],
            "smoking_status" : ['No Smoking', 'Regular' ,'Occasional'],
            "employment_status" : ['Salaried', 'Self-Employed', 'Freelancer'],
            "income_level" : ['<10L' ,'10L - 25L' ,'> 40L' ,'25L - 40L'],
            "medical_history" : ['Diabetes' ,'High blood pressure' ,'No Disease',
             'Diabetes & High blood pressure', 'Thyroid' ,'Heart disease',
             'High blood pressure & Heart disease', 'Diabetes & Thyroid',
             'Diabetes & Heart disease'],
            "insurance_plan" : ['Bronze' ,'Silver' ,'Gold']
}

row1 = st.columns(3)
row2 = st.columns(3)
row3 = st.columns(3)
row4 = st.columns(3)

# row 1
with row1[0]:
    age = st.number_input("Age",min_value=18, max_value=100, step=1)
with row1[1]:
    number_of_dependants = st.number_input("Number of Dependants", min_value=0, max_value=20, step=1)
with row1[2]:
    income_lakhs = st.number_input("Income Lakhs",min_value=1, max_value=200, step=1)

# row 2
with row2[0]:
    genetical_risk = st.number_input("Genetical Risk",min_value=0, max_value=5, step=1)
with row2[1]:
    gender = st.selectbox("Gender",categorical_options["gender"])
with row2[2]:
    region = st.selectbox("Region",categorical_options["region"])

#row 3
with row3[0]:
    marital_status = st.selectbox("Marital Status",categorical_options["marital_status"])
with row3[1]:
    bmi_category = st.selectbox("Bmi Category",categorical_options["bmi_category"])
with row3[2]:
    smoking_status = st.selectbox("Smoking Status",categorical_options["smoking_status"])

#row 4
with row4[0]:
    employment_status = st.selectbox("Employment Status",categorical_options["employment_status"])
with row4[1]:
    medical_history = st.selectbox("Medical History",categorical_options["medical_history"])
with row4[2]:
    insurance_plan = st.selectbox("Insurance Plan", categorical_options["insurance_plan"])

#input directory
input_directory = {
    "Age" : age,
    "Number of Dependants" : number_of_dependants,
    "Income Lakhs" : income_lakhs,
    "Genetical Risk" : genetical_risk,
    "Gender" : gender,
    "Region" : region,
    "Marital Status" : marital_status,
    "BMI Category" : bmi_category,
    "Smoking Status" : smoking_status,
    "Employment Status" : employment_status,
    "Medical History" : medical_history,
    "Insurance Plan" : insurance_plan
}


# Button to make prediction
if st.button("Predict"):
    prediction = predict(input_directory, input_directory["Age"])
    st.success(f"Insurance Price will be {np.round(prediction,0)}")














