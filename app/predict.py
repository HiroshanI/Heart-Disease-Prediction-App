# Import Tools
import numpy as np
import pickle
import streamlit as lit
from result import show_result

# Import Model
model_filepath = "output/heart_model_data.pkl"
model_data = pickle.load(open("../" + model_filepath, "rb"))
rfc_model = model_data['rfc_model']
log_model = model_data['log_model']
ann_model = model_data['ann_model']
svc_model = model_data['svc_model']
or_encoder = model_data['or_encoder']
encoder = model_data['encoder']
scaler = model_data['scaler']


def get_pred_info(pred):
    if pred == 0:
        return ("💖 No heart disease")
    elif pred == 1:
        return ("💔 There is a high chance of a heart disease")
    
def get_prediction(model, data):

    message = ""
    proba = []
    if model == "RandomForestClassifier":
        preds = rfc_model.predict(data)
        proba = rfc_model.predict_proba(data)
        message = get_pred_info(preds)
    elif model == "LogisticRegression":
        preds = log_model.predict(data)
        proba = log_model.predict_proba(data)
        message = get_pred_info(preds)
    elif model == "SupportVectorClassifier":
        preds = svc_model.predict(data)
        proba = svc_model.predict_proba(data)
        message = get_pred_info(preds)
    elif model == "ANN":
        preds = ann_model.predict(data)
        message = get_pred_info(int(preds > 0.5))
    
    if model != "ANN":
        return [message, np.max(proba)]
    else :
        return (message)

def show_prediction_page(model):

    lit.markdown(
        """
        <div style="text-align:center;padding-bottom:60px;">
            <h1><span class="heart">❤️</span> Heart Disease Prediction App</h1>
        </div>
        """,
        unsafe_allow_html=True
    )

    input = {
        'age':0, 'trestbps':0, 'chol':0, 'thalch':0, 'oldpeak':0,
        'sex':'Male', 'cp':'typical angina', 'fbs':False, 'restecg':'lv hypertrophy', 
        'exang':False, 'slope':'downsloping', 'ca':'', 'thal':''
    }
    col1, col2 = lit.columns(2)
    
    with col1:
        restecg = ['lv hypertrophy', 'normal', 'st-t abnormality']
        fbs = [True, False]
        thal = ['fixed defect', 'normal', 'reversable defect']
        sex = ['Male', 'Female']
        input['sex'] = lit.radio("Sex", sex, key=5)
        input['age'] = lit.slider("Age", 10, 90, 30, 1, key=0)
        input['trestbps'] = lit.number_input("Resting Blood Pressure - mm Hg", key=1)
        input['chol'] = lit.number_input("Serum cholesterol - mg/dl", key=2)
        input['restecg'] = lit.selectbox("Resting ECG results", restecg, key=8)
        input['fbs'] = lit.selectbox("Fasting Blood Sugar > 120 mg/dl", fbs, key=7)
        input['thal'] = lit.selectbox("Any heart defects", thal, key=12)
    
    with col2:
        ca = [0, 1, 2, 3]
        cp = ['typical angina', 'asymptomatic', 'non-anginal', 'atypical angina']
        exang = [True, False]
        slope = ['downsloping', 'flat', 'upsloping']
        input['ca'] = lit.radio("Major vessels with blockage ", ca, key=11)
        input['cp'] = lit.selectbox("Chest pain type", cp, key=6)
        input['exang'] = lit.selectbox("Exercise induced angina", exang, key=9)
        input['thalch'] = lit.number_input("Maximum heart rate achieved", key=3)
        input['oldpeak'] = lit.number_input("ST depression induced by exercise relative to rest", key=4)
        input['slope'] = lit.selectbox("The slope of the peak exercise ST segment", slope, key=10)


    submit = lit.button("Submit Details")
    if submit: 

        X = np.array(list(input.values()))
        X_num = scaler.transform((X[:5]).reshape(1,-1)) 
        X_cat = encoder.transform(X[5:].reshape(1,-1))
        X_processed = np.hstack([X_num, X_cat])

        message = get_prediction(model, X_processed)

        show_result(message)