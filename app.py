
import streamlit as st
import pandas as pd
import pickle

with open("/content/eduguard_model.pkl", "rb") as f:
    model = pickle.load(f)

with open("/content/eduguard_data.pkl", "rb") as f:
    data = pickle.load(f)

st.set_page_config(
    page_title="EduGuard AI",
    page_icon="🎓",
    layout="centered"
)

st.title("🎓 EduGuard AI")
st.subheader("Student Academic Risk Prediction System")

st.write(
    "EduGuard AI uses academic, attendance, study, sleep, and "
    "student-background information to estimate academic risk "
    "before the final examination."
)

st.divider()

st.header("📝 Student Information")

gender = st.selectbox("Gender", ["Male", "Female"])

study_time_hours = st.number_input(
    "Study Time (hours per day)",
    min_value=0.0,
    max_value=12.0,
    value=3.0,
    step=0.5
)

attendance_percent = st.number_input(
    "Attendance (%)",
    min_value=0.0,
    max_value=100.0,
    value=80.0,
    step=1.0
)

sleep_hours = st.number_input(
    "Sleep Hours per Day",
    min_value=0.0,
    max_value=12.0,
    value=7.0,
    step=0.5
)

parental_education = st.selectbox(
    "Parental Education",
    ["High School", "Bachelor's", "Master's", "PhD"]
)

internet_access = st.selectbox(
    "Internet Access",
    ["Yes", "No"]
)

extracurricular_activities = st.selectbox(
    "Extracurricular Activities",
    ["Yes", "No"]
)

part_time_job = st.selectbox(
    "Part-Time Job",
    ["Yes", "No"]
)

previous_grade = st.number_input(
    "Previous Grade",
    min_value=0.0,
    max_value=100.0,
    value=70.0,
    step=0.1
)

if st.button("🔍 Predict Risk", use_container_width=True):

    student_data = pd.DataFrame([{
        "gender": gender,
        "study_time_hours": study_time_hours,
        "attendance_percent": attendance_percent,
        "sleep_hours": sleep_hours,
        "parental_education": parental_education,
        "internet_access": internet_access,
        "extracurricular_activities": extracurricular_activities,
        "part_time_job": part_time_job,
        "previous_grade": previous_grade
    }])

    prediction = model.predict(student_data)[0]

    probabilities = model.predict_proba(student_data)[0]
    classes = model.classes_

    probability_dict = dict(zip(classes, probabilities))

    st.divider()
    st.header("📊 Prediction Result")

    if prediction == "High Risk":
        st.error("🔴 High Risk")
    elif prediction == "Medium Risk":
        st.warning("🟡 Medium Risk")
    else:
        st.success("🟢 Low Risk")

    st.write("### Risk Probabilities")

    for risk in ["High Risk", "Medium Risk", "Low Risk"]:
        probability = probability_dict.get(risk, 0)
        st.write(f"**{risk}: {probability:.1%}**")
        st.progress(float(probability))

    st.info(
        "This is an AI-assisted risk estimate intended to help identify "
        "students who may benefit from additional academic support."
    )

st.divider()

st.caption("EduGuard AI • Student Support System")
