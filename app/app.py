import streamlit as lit
# Pages 
from predict import show_prediction_page
from explore import show_explore_page

# Page properties
lit.set_page_config(page_title=f"Heart Disease Prediction", page_icon="💔")

# Sidebar
lit.sidebar.write("# __Welcome!__")
page = lit.sidebar.selectbox("Predict or Explore", ["Predict", "Explore"])  

if page == 'Predict':
    lit.sidebar.write("---")
    lit.sidebar.write("# Preferences")
    model = lit.sidebar.selectbox("Select Pre-trained model", 
                                  ['RandomForestClassifier', 
                                   'LogisticRegression', 
                                   'SupportVectorClassifier', 
                                   'ANN'], 
                                   key='model')  
    show_prediction_page(model)
elif page == 'Explore':
    show_explore_page()