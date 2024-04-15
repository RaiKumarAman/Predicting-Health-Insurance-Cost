import numpy as np
import pickle 
import streamlit as st

def insurance(input_data):
    load_model= pickle.load(open(r"C:\Users\Aman\OneDrive\Documents\Python\Medical Insurance Cost Predicition\insurance.sav", 'rb'))
    data1=np.asarray(input_data)
    data=data1.reshape(1,-1)
    prediction=load_model.predict(data)
    return prediction[0]

def main():
    st.title("Insurance_Predictive")

    

    age= st.number_input("Age")
    bmi= st.number_input("BMI")
    children= st.number_input("Number of Children")
    smoker= st.number_input("Are you a Smoker: 1-No/0-Yes")
    sex= st.number_input("Sex: 0-Male/1-Female")
    region= st.number_input("Region: 3-NW/2-NE/0-SE/1-SW")


    diagonsis=""

    if st.button("Cost"):
        diagonsis= insurance([age,sex,bmi,children,smoker,region])


    st.success(diagonsis)

if __name__=="__main__":
    main()
