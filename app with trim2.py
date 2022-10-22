# -*- coding: utf-8 -*-
"""
Created on Sat Oct 22 18:35:37 2022

@author: navne
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Oct 21 18:23:43 2022

@author: navne
"""

import streamlit as st
from keras.models import load_model
import numpy as np 
import pandas as pd

model = load_model("C:/Users/navne/.spyder-py3/BSRAtrim2.h5")
def predict(x1,x2,x3,x4,x5,x6,x7):
    prediction=model.predict(pd.DataFrame([[Trim_LBP, Length_Disp, L_B, Block_Coefft, B_T, LCB_Posn, V_L]],columns=['Trim/LBP','Length/Disp','L/B','Block Coefft','B/T','LCB Posn','V/Sqrt(L)']))
    return prediction

st.title("Prediction of circular C")
Trim_LBP=st.number_input("Trim/LBP",step=1e-4)
Trim_LBP_scaled=(Trim_LBP-0.0252/0.0146)
Length_Disp=st.number_input("Length/Disp",step=1e-4)
Length_Disp_scaled=(Length_Disp-4.877)/0.216
L_B=st.number_input("L/B",step=1e-3)
L_B_scaled=(L_B-5.399)/0.356
Block_Coefft=st.number_input("Block Coefft",step=1e-4)
Block_Coefft_scaled=(Block_Coefft-0.562)/0.022
B_T=st.number_input("B/T",step=1e-4)
B_T_scaled=(B_T-2.256)/0.259
LCB_Posn=st.number_input("LCB Posn",step=1e-4)
LCB_Posn_scaled=(LCB_Posn+1.692)/1.836
V_L=st.number_input("V/Sqrt(L)",step=1e-4)
V_L_scaled=(V_L-0.902)/0.171

btn=st.button("circ C")

if btn:
	pred = model.predict(np.array([Trim_LBP_scaled,Length_Disp_scaled,L_B_scaled,Block_Coefft_scaled,B_T_scaled,LCB_Posn_scaled,V_L_scaled]).reshape(1,-1))
	st.subheader(pred)