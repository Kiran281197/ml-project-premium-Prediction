import pandas as pd
from joblib import load

model_young = load("artifacts/model_young.joblib")
model_rest = load("artifacts/model_rest.joblib")

scaler_young = load("artifacts/scaler_young.joblib")
scaler_rest = load("artifacts/scaler_rest.joblib")

column_lst = [
    'age',
     'number_of_dependants',
     'income_lakhs',
     'insurance_plan',
     'genetical_risk',
     'normalized_risk_score',
     'gender_Male',
     'region_Northwest',
     'region_Southeast',
     'region_Southwest',
     'marital_status_Unmarried',
     'bmi_category_Obesity',
     'bmi_category_Overweight',
     'bmi_category_Underweight',
     'smoking_status_Occasional',
     'smoking_status_Regular',
     'employment_status_Salaried',
     'employment_status_Self-Employed'
]

def preprocessing(input_dict):
    df = pd.DataFrame(0, columns=column_lst, index=[0])
    for key, value in input_dict.items():
        if key=="Age":
            df["age"] = value
        elif key=="Number of Dependants":
            df["number_of_dependants"] = value
        elif key=="Income Lakhs":
            df["income_lakhs"] = value
        elif key=="Genetical Risk":
            df["genetical_risk"] = value
        elif key=="Gender":
            if value=="Male":
                df["gender_Male"] = 1
        elif key=="Region":
            if value=="Northwest":
                df["region_Northwest"] = 1
            elif value=="Southeast":
                df["region_Southeast"] = 1
            elif value=="Southwest":
                df["region_Southwest"] = 1
        elif key=="Marital Status":
            if value=="Unmarried":
                df["marital_status_Unmarried"] = 1
        elif key=="BMI Category":
            if value=="Obesity":
                df["bmi_category_Obesity"] = 1
            elif value=="Overweight":
                df["bmi_category_Overweight"] = 1
            elif value=="Underweight":
                df["bmi_category_Underweight"] = 1
        elif key=="Smoking Status":
            if value=="Occasional":
                df["smoking_status_Occasional"] = 1
            elif value=="Regular":
                df["smoking_status_Regular"] = 1
        elif key=="Employment Status":
            if value=="Salaried":
                df["employment_status_Salaried"] = 1
            elif value=="Self-Employed":
                df["employment_status_Self-Employed"] = 1
        elif key == "Medical History":
            risk_scores = {
                "diabetes": 6,
                "heart disease": 8,
                "high blood pressure": 6,
                "thyroid": 5,
                "no disease": 0
            }

            diseases = [d.strip().lower() for d in value.split("&")]

            total_risk_score = 0
            for disease in diseases:
                total_risk_score += risk_scores.get(disease, 0)

            max_score = 14
            min_score = 0

            df["normalized_risk_score"] = (total_risk_score - min_score) / (max_score - min_score)

        elif key=="Insurance Plan":
            if value=="Bronze":
                df["insurance_plan"] = 1
            elif value=="Silver":
                df["insurance_plan"] = 2
            else:
                df["insurance_plan"] = 3

    df = handle_scaling(df["age"].iloc[0], df)
    return df

def handle_scaling(age, df):
    if age<=25:
        scaler_object = scaler_young
    else:
        scaler_object = scaler_rest

    col_to_scale = scaler_object["col_to_scale"]
    scaler = scaler_object["scaler"]

    df["income_level"] = 0
    df[col_to_scale] = scaler.transform(df[col_to_scale])
    df.drop("income_level", axis=1, inplace=True)
    return df


def predict(input_dict, age):
    input_df = preprocessing(input_dict)
    print(age)
    if age <= 25:
        model = model_young
    else:
        model = model_rest

    output = model.predict(input_df)
    return output