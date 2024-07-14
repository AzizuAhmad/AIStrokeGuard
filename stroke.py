import pandas as pd
import numpy as np
import streamlit as st
import time
import pickle

model = pickle.load(open("modelStroke1.pkl", 'rb'))

st.set_page_config(
    page_title="Stroke Prediction",
    page_icon="🏥",
)

st.image("image/strokeLogo5.png")
st.title("AIStrokeGuard")


tab1, tab2 = st.tabs(["**About AIStrokeGuard**", "**Stroke Predict**"])

with tab1: 
    st.header("AIStrokeGuard")

    # Columns for layout
    col1, col2 = st.columns([1, 2])

    with col1:
        st.image("image/strokeLogo5.png", caption="AIStrokeGuard Logo")  # Add your image here

    with col2:
        st.write("""
            AIStrokeGuard is an AI-powered stroke detection system designed to provide early and accurate diagnosis. 
            AIStrokeGuard aims to save lives and reduce long-term disability. 
            Everyone can use AIStrokeGuard whether it's a child, an elderly person, or a medical employee.
        """)

    st.markdown("### How to Use AIStrokeGuard:")
    st.write("""
        To detect strokes quickly and accurately, simply enter the required data into the application. 
        AIStrokeGuard will predict the results based on the data entered, allowing for efficient stroke detection 
        using simulated or real data.
        """)

    st.markdown("### Advantages:")

    # Use expander for details
    with st.expander("Learn more about the advantages"):
        st.markdown("""
        - **Early Detection**: Enables timely medical intervention by predicting stroke risk early.
        - **User-Friendly Interface**: Designed for ease of use by both laymen and professionals.
        - **Cost-Effective**: Free access ensures affordability for all users.
        """)

    st.markdown("### Technology Used:")

    with st.expander("Learn more about the technology"):
        st.markdown("""
        - **Artificial Intelligence**: Utilizing state-of-the-art AI and machine learning techniques for high accuracy in stroke predictions.
        - **Web-Based Deployment**: Accessible through a user-friendly web application, developed using Streamlit for ease of use.
        """)

    st.write("### Accuracy:")
    st.write("AIStrokeGuard achieves an accuracy rate above :green[**90%**] in predicting stroke risks.")

with tab2:
    st.sidebar.header("**User Input** Sidebar")

    gender_sb = st.sidebar.selectbox(label=":violet[**Gender**]",options=["Female","Male"])
    st.sidebar.write("")
    st.sidebar.write("")
    if gender_sb == "Female":
        gender = 0
    elif gender_sb == "Male":
        gender = 1 
    # -- Value 0: Female
    # -- Value 1: Male

    age = st.sidebar.number_input(label=":violet[**Age**]",min_value= 10,max_value= 90)
    st.sidebar.write(f":orange[Min] value: :orange[**{10}**], :red[Max] value: :red[**{90}**]")

    hypertension_sb =  st.sidebar.selectbox(label=":violet[**Hypertension**]",options=["Yes","No"])
    st.sidebar.write("")
    if hypertension_sb == "Yes":
        hypertension = 1
    elif hypertension_sb == "No":
        hypertension = 0

    heart_disease_sb = st.sidebar.selectbox(label=":violet[**Heart Disease**]",options=["Yes","No"])
    st.sidebar.write("")
    if heart_disease_sb == "Yes":
        heart_disease = 1
    elif heart_disease_sb == "No":
        heart_disease = 0

    ever_married_sb = st.sidebar.selectbox(label=":violet[**Ever Married**]",options=["Yes","No"])
    st.sidebar.write("")
    if ever_married_sb == "Yes":
        ever_married = 1
    elif ever_married_sb == "No":
        ever_married = 0

    work_type_sb = st.sidebar.selectbox(label=":violet[**Work Type**]",options=["Private","Self-Employed","Childern","Goverment Job","Never Worked"])
    st.sidebar.write("")
    if work_type_sb == "Private":
        work_type = 2
    elif work_type_sb == "Self-Employed":
        work_type = 3
    elif work_type_sb == "Childern":
        work_type = 4
    elif work_type_sb == "Goverment Job":
        work_type = 0
    elif work_type_sb == "Never Worked":
        work_type = 1

    Residence_type_sb = st.sidebar.selectbox(label=":violet[**Residence Type**]",options=["Urban","Rural"])
    st.sidebar.write("")
    if Residence_type_sb == "Rural":
        Residence_type = 0
    elif Residence_type_sb == "Urban":
        Residence_type = 1

    avg_glucose_level = st.sidebar.number_input(label=":violet[**Average Glucose Level**]",min_value= 55.0,max_value= 280.0)
    st.sidebar.write(f":orange[Min] value: :orange[**{10.0}**], :red[Max] value: :red[**{280.0}**]")

    bmi = st.sidebar.number_input(label=":violet[**BMI**]",min_value= 10.0,max_value= 100.0)
    st.sidebar.write(f":orange[Min] value: :orange[**{10.0}**], :red[Max] value: :red[**{100.0}**]")

    smoking_status_sb = st.sidebar.selectbox(label=":violet[**Smoking Status**]",options=["Never Smoked","Unknown","Formerly Smoked","Smokes"])
    st.sidebar.write("")
    if smoking_status_sb == "Never Smoked":
        smoking_status = 2
    elif smoking_status_sb == "Unknown":
        smoking_status = 0
    elif smoking_status_sb == "Formerly Smoked":
        smoking_status = 1
    elif smoking_status_sb == "Smokes":
        smoking_status = 3

    data = {
        'Gender': gender_sb,
        'Age': age,
        'Hypertension': hypertension_sb,
        'Heart Disease': heart_disease_sb,
        'Ever Married': ever_married_sb,
        'Work Type': work_type_sb,
        'Residence Type': Residence_type_sb,
        'Average Glucose Level': avg_glucose_level,
        'BMI': bmi,
        'Smoking Status': smoking_status_sb,
    }

    preview_df = pd.DataFrame(data, index=['input'])
    st.header("User Input as DataFrame")
    st.write("")
    st.dataframe(preview_df.iloc[:, :7])
    st.write("")
    st.dataframe(preview_df.iloc[:, 7:])
    st.write("")

    result = ":violet[-]"

    predict_btn = st.button("**Predict**", type="primary")

    st.write("")
    if predict_btn:
        inputs = [[age, gender, hypertension, heart_disease, ever_married, work_type, Residence_type, avg_glucose_level, bmi, smoking_status]]
        prediction = model.predict(inputs)[0]

        bar = st.progress(0)
        status_text = st.empty()

        for i in range(1, 101):
            status_text.text(f"{i}% complete")
            bar.progress(i)
            time.sleep(0.01)
            if i == 100:
                time.sleep(1)
                status_text.empty()
                bar.empty()

        if prediction == 0:
            result = ":green[**Healthy**]"
        elif prediction == 1:
            result = ":red[**Stroke Potential**]"


    st.write("")
    st.write("")
    st.subheader("Prediction Result:")
    st.subheader(result)


