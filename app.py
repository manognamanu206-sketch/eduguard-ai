
import streamlit as st
import pandas as pd
import joblib

# ============================================================
# EDUGUARD AI
# Mobile-Friendly Academic Risk Early Warning System
# ============================================================

st.set_page_config(
    page_title="EduGuard AI",
    page_icon="🎓",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Load model
model = joblib.load("/content/eduguard_ai_model.pkl")

# ============================================================
# CUSTOM CSS - MOBILE FRIENDLY
# ============================================================

st.markdown("""
<style>

.main-title {
    text-align: center;
    font-size: 42px;
    font-weight: 800;
    margin-bottom: 5px;
}

.subtitle {
    text-align: center;
    font-size: 18px;
    margin-bottom: 25px;
}

.section-title {
    font-size: 24px;
    font-weight: 700;
    margin-top: 20px;
    margin-bottom: 10px;
}

div.stButton > button {
    width: 100%;
    min-height: 55px;
    font-size: 18px;
    font-weight: 700;
    border-radius: 12px;
}

@media (max-width: 600px) {

    .main-title {
        font-size: 32px;
    }

    .subtitle {
        font-size: 16px;
    }

    .section-title {
        font-size: 21px;
    }

    .block-container {
        padding-top: 1rem;
        padding-left: 1rem;
        padding-right: 1rem;
    }

}

</style>
""", unsafe_allow_html=True)

# ============================================================
# HEADER
# ============================================================

st.markdown(
    '<div class="main-title">🎓 EduGuard AI</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">AI-Powered Academic Risk Early-Warning System</div>',
    unsafe_allow_html=True
)

st.write(
    "EduGuard AI analyzes academic, behavioral, and student-support "
    "information to estimate academic risk and provide a personalized "
    "support plan."
)

st.divider()

# ============================================================
# STUDENT PROFILE
# ============================================================

st.markdown(
    '<div class="section-title">👤 Student Profile</div>',
    unsafe_allow_html=True
)

school = st.selectbox("School", ["GP", "MS"])
sex = st.selectbox("Sex", ["F", "M"])
age = st.number_input("Age", 15, 22, 17)
address = st.selectbox("Address", ["U", "R"])
famsize = st.selectbox("Family Size", ["GT3", "LE3"])
Pstatus = st.selectbox("Parent Status", ["A", "T"])

Medu = st.selectbox("Mother's Education", [0, 1, 2, 3, 4])
Fedu = st.selectbox("Father's Education", [0, 1, 2, 3, 4])

Mjob = st.selectbox(
    "Mother's Job",
    ["teacher", "health", "services", "at_home", "other"]
)

Fjob = st.selectbox(
    "Father's Job",
    ["teacher", "health", "services", "at_home", "other"]
)

reason = st.selectbox(
    "School Choice Reason",
    ["home", "reputation", "course", "other"]
)

guardian = st.selectbox(
    "Guardian",
    ["mother", "father", "other"]
)

# ============================================================
# ACADEMIC INFORMATION
# ============================================================

st.markdown(
    '<div class="section-title">📚 Academic Information</div>',
    unsafe_allow_html=True
)

traveltime = st.selectbox("Travel Time", [1, 2, 3, 4])

studytime = st.selectbox(
    "Weekly Study Time",
    [1, 2, 3, 4]
)

failures = st.selectbox(
    "Previous Failures",
    [0, 1, 2, 3]
)

absences = st.number_input(
    "School Absences",
    min_value=0,
    max_value=100,
    value=2
)

G1 = st.number_input(
    "First Period Grade (G1)",
    min_value=0,
    max_value=20,
    value=10
)

G2 = st.number_input(
    "Second Period Grade (G2)",
    min_value=0,
    max_value=20,
    value=10
)

famrel = st.slider(
    "Family Relationship",
    1, 5, 4
)

freetime = st.slider(
    "Free Time",
    1, 5, 3
)

goout = st.slider(
    "Social Activity",
    1, 5, 3
)

health = st.slider(
    "Current Health",
    1, 5, 3
)

# ============================================================
# SUPPORT INFORMATION
# ============================================================

st.markdown(
    '<div class="section-title">🏠 Support & Lifestyle</div>',
    unsafe_allow_html=True
)

schoolsup = st.selectbox(
    "School Support",
    ["yes", "no"]
)

famsup = st.selectbox(
    "Family Support",
    ["yes", "no"]
)

paid = st.selectbox(
    "Extra Paid Classes",
    ["yes", "no"]
)

activities = st.selectbox(
    "Extra Activities",
    ["yes", "no"]
)

nursery = st.selectbox(
    "Attended Nursery",
    ["yes", "no"]
)

higher = st.selectbox(
    "Plans Higher Education",
    ["yes", "no"]
)

internet = st.selectbox(
    "Internet Access",
    ["yes", "no"]
)

romantic = st.selectbox(
    "Romantic Relationship",
    ["yes", "no"]
)

# ============================================================
# PREDICTION
# ============================================================

st.divider()

st.markdown(
    '<div class="section-title">🔮 Academic Risk Prediction</div>',
    unsafe_allow_html=True
)

st.write(
    "Enter the information above and generate an academic risk assessment."
)

predict_button = st.button(
    "🔮 Predict Academic Risk"
)

# ============================================================
# PREDICTION LOGIC
# ============================================================

if predict_button:

    student = pd.DataFrame([{
        "school": school,
        "sex": sex,
        "age": age,
        "address": address,
        "famsize": famsize,
        "Pstatus": Pstatus,
        "Medu": Medu,
        "Fedu": Fedu,
        "Mjob": Mjob,
        "Fjob": Fjob,
        "reason": reason,
        "guardian": guardian,
        "traveltime": traveltime,
        "studytime": studytime,
        "failures": failures,
        "schoolsup": schoolsup,
        "famsup": famsup,
        "paid": paid,
        "activities": activities,
        "nursery": nursery,
        "higher": higher,
        "internet": internet,
        "romantic": romantic,
        "famrel": famrel,
        "freetime": freetime,
        "goout": goout,
        "health": health,
        "absences": absences,
        "G1": G1,
        "G2": G2
    }])

    prediction = model.predict(student)[0]

    # ========================================================
    # RESULT
    # ========================================================

    st.divider()

    st.subheader("📊 Prediction Result")

    if prediction == "High Risk":

        st.error("🔴 HIGH ACADEMIC RISK")

        st.write(
            "The model identifies this student as having a higher "
            "academic risk based on the information provided."
        )

        support_level = "High Priority Support"

    elif prediction == "Medium Risk":

        st.warning("🟡 MEDIUM ACADEMIC RISK")

        st.write(
            "The model identifies this student as having a moderate "
            "academic risk."
        )

        support_level = "Regular Monitoring"

    else:

        st.success("🟢 LOW ACADEMIC RISK")

        st.write(
            "The model identifies this student as currently having "
            "a lower academic risk."
        )

        support_level = "Maintain Current Progress"

    # ========================================================
    # UNIQUE FEATURE
    # SMART SUPPORT PLAN
    # ========================================================

    st.divider()

    st.subheader("💡 EduGuard Smart Support Plan")

    st.write(
        "Instead of only showing a risk level, EduGuard AI creates "
        "simple actions that can help support the student's progress."
    )

    # --------------------------------------------------------
    # HIGH RISK PLAN
    # --------------------------------------------------------

    if prediction == "High Risk":

        st.error("🚨 Priority: Immediate Academic Support")

        st.markdown("""
        **📅 7-Day Support Plan**

        **Day 1:** Review recent grades and identify difficult subjects.

        **Day 2:** Create a simple daily study schedule.

        **Day 3:** Review missed topics with a teacher or mentor.

        **Day 4:** Complete focused practice for weak subjects.

        **Day 5:** Review attendance and missed classroom work.

        **Day 6:** Take a short practice test or revision session.

        **Day 7:** Review progress and adjust the study plan.
        """)

        st.info(
            "👨‍🏫 Suggested action: Teacher/counselor follow-up "
            "and additional academic support."
        )

    # --------------------------------------------------------
    # MEDIUM RISK PLAN
    # --------------------------------------------------------

    elif prediction == "Medium Risk":

        st.warning("📌 Priority: Regular Monitoring")

        st.markdown("""
        **📅 7-Day Improvement Plan**

        **Day 1:** Set two academic goals for the week.

        **Day 2:** Spend focused time reviewing difficult topics.

        **Day 3:** Complete pending assignments.

        **Day 4:** Practice questions from weaker subjects.

        **Day 5:** Review previous mistakes.

        **Day 6:** Complete a short revision session.

        **Day 7:** Check progress against the weekly goals.
        """)

        st.info(
            "👨‍🏫 Suggested action: Monitor progress and provide "
            "support when needed."
        )

    # --------------------------------------------------------
    # LOW RISK PLAN
    # --------------------------------------------------------

    else:

        st.success("🌟 Priority: Maintain Progress")

        st.markdown("""
        **📅 7-Day Growth Plan**

        **Day 1:** Set a learning goal.

        **Day 2:** Review current subjects.

        **Day 3:** Practice one challenging topic.

        **Day 4:** Complete revision.

        **Day 5:** Explore an additional learning resource.

        **Day 6:** Test your understanding.

        **Day 7:** Review achievements and set the next goal.
        """)

        st.info(
            "👨‍🏫 Suggested action: Continue positive study habits "
            "and monitor academic progress."
        )

    # ========================================================
    # QUICK INSIGHTS
    # ========================================================

    st.divider()

    st.subheader("📈 Quick Student Insights")

    if studytime <= 1:
        st.warning(
            "📚 Study time is relatively low. Increasing consistent "
            "study time may be beneficial."
        )
    else:
        st.success(
            "📚 Study time appears reasonably consistent."
        )

    if absences > 15:
        st.warning(
            "🏫 Attendance may require attention because absences are high."
        )
    else:
        st.success(
            "🏫 Attendance is within a relatively manageable range."
        )

    if failures > 0:
        st.warning(
            "🎯 Previous academic failures indicate that additional "
            "monitoring may be useful."
        )
    else:
        st.success(
            "🎯 No previous failures were reported."
        )

    if G2 < G1:
        st.warning(
            "📉 The second-period grade is lower than the first-period grade."
        )
    elif G2 > G1:
        st.success(
            "📈 The second-period grade is higher than the first-period grade."
        )
    else:
        st.info(
            "📊 The first and second period grades are currently the same."
        )

# ============================================================
# ABOUT
# ============================================================

st.divider()

with st.expander("🤖 About EduGuard AI"):

    st.write(
        "**Machine Learning Model:** Gradient Boosting"
    )

    st.write(
        "**Test Accuracy:** 84.62%"
    )

    st.write(
        "**Training Dataset:** 649 student records"
    )

    st.write(
        "**Alcohol-related features:** Removed"
    )

with st.expander("⚠️ Responsible Use"):

    st.write(
        "EduGuard AI is an educational early-warning tool. "
        "Predictions should support—not replace—teachers, counselors, "
        "parents, and other qualified decision-makers."
    )

# ============================================================
# FOOTER
# ============================================================

st.divider()

st.caption(
    "🎓 EduGuard AI • Academic Risk Awareness & Smart Student Support"
)
