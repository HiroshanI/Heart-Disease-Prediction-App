import streamlit as lit

def show_result(pred):
    if isinstance(pred, list) :
        lit.write(f"# {pred[0]} ")
        lit.write(f"Confidence : {pred[1]*100:.1f}%")
    else:
        lit.write(f"# {pred} ") 
