import streamlit as lit

def show_result(pred):
    if isinstance(pred, list) :
        lit.write(f"""# Results """)
        
        if ("💔") in (pred[0].split()):
            lit.error(f"""## {pred[0]} """)
        else:
            lit.success(f"""## {pred[0]} """)
            
        lit.write(f"""Confidence : {pred[1]*100:.1f}%""")
    else:
        lit.info(f"# {pred} ") 
