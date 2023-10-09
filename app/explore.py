import streamlit as lit
import pandas as pd
import matplotlib.pyplot as plt
from tabulate import tabulate
from scipy.stats.mstats import winsorize

title_md = """<div style="text-align:center; padding-bottom:60px; "><h1>Explore Heart Disease Data</h1></div>"""
MY_PALETTE= ["#525FE1","#F55353", "#8F43EE","#FEB139", "#00DFA2"]

@lit.cache_resource
def load_data():
    data = pd.read_csv('../input/heart_disease_uci.csv') 
    data.rename(mapper={'num':'class'}, axis=1, inplace=True) # rename target column to "class"
    data.dropna(subset=['class'], axis=0, inplace=True) # drop rows if target is null 
    data.drop_duplicates(keep='first', inplace=True) # drop duplicate rows
    data = data[data['dataset'] == "Cleveland"]
    data.drop(['dataset'], axis=1, inplace=True)
    data['chol_'] = winsorize(data['chol'], limits=[0, 0.01])
    data['Heart Disease'] = [y != 0 for y in data['class']]
    return data

def show_explore_page():
    
    lit.markdown(
        title_md,
        unsafe_allow_html=True
    ) 

    temp = load_data()

    


