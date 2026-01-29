import streamlit as st
import pandas as pd
import joblib

model = joblib.load('best_model.pkl')
encoders = {col:joblib.load(f"{col}_encoder.pkl") for col in ['Sex','Housing','Saving accounts','Checking account']}
st.title("Credit Risk Prediction APP")
st.write("Enter the applicant information to predict if the credit risk is good or bad")
age = st.number_input("Age",min_value=18,max_value=80,value = 30)
sex = st.selectbox("Sex",["male","female"])
job = st.number_input("job (0-3)",max_value=3,min_value=0,value=1)
housing = st.selectbox("Housing",["own","rent","free"])
Saving_accounts = st.selectbox("Saving accounts",["little","moderate","rich","quite rich"])
Checking_account = st.selectbox("Checking account",['moderate', 'little', 'rich'])
Credit_amount = st.number_input("Credit amount",min_value=10,value=300)
Duration = st.number_input("Duration (months)",min_value=1,value = 10)
input_df = {
    "Age" : [age],
    "Sex" : [encoders["Sex"].transform([sex])[0]],
    "Job" : [job],
    "Housing" : [encoders["Housing"].transform([housing])[0]],
    "Saving accounts" : [encoders["Saving accounts"].transform([Saving_accounts])[0]],
    "Checking account" : [encoders["Checking account"].transform([Checking_account])[0]],
    "Credit amount" : [Credit_amount],
    "Duration" : [Duration]

}
final_df = pd.DataFrame(input_df)
if st.button("Predict"):
    pred = model.predict(final_df)[0]
    if pred == 1:
        st.success("The predicted Risk is : **GOOD**")
    else:
        st.error("The predicted Risk is : **BAD**")