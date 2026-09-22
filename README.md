# EduGuard AI

## Student Academic Risk Prediction System

EduGuard AI is a machine-learning based early-warning system for identifying students who may be at academic risk before the final examination.

## Risk Levels
- High Risk: D or F
- Medium Risk: C
- Low Risk: A or B

## Input Features
- Gender
- Study time
- Attendance
- Sleep hours
- Parental education
- Internet access
- Extracurricular activities
- Part-time job
- Previous grade

## Machine Learning
Final model: Weighted Logistic Regression

Dataset size: 1,000 students

## Results
Held-out test accuracy: 69.5%
High Risk recall: 55%
Weighted F1: 0.70

5-fold cross-validation accuracy: 72.5% ± 2.3%
5-fold macro F1: 60.4% ± 4.2%
5-fold weighted F1: 71.7% ± 2.1%

## Technology
- Python
- Pandas
- Scikit-learn
- Streamlit
- Google Colab

## Running the App
pip install -r requirements.txt
streamlit run app.py

## Limitation
EduGuard is an AI-assisted screening tool and should support, not replace, human academic judgment.

## Future Scope
- Explainable AI
- Teacher dashboard
- Historical risk tracking
- Larger and more diverse datasets
- Early intervention recommendations