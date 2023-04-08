import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import cv2
import activity_1 as act1
#import pages.activity_2 as act2
#import pages.activity_3 as act3

st.set_option('deprecation.showPyplotGlobalUse', False)
#st.set_option ('browser.gatherUsageStats' , False)

def main():
    st.title("Midterm Exam in CCS221")

    st.sidebar.header("Line Algorithm Parameters")
    _act1_x0, _act1_y0, _act1_x1, _act1_y1 = st.sidebar.slider('Starting X', 1, 100), \
                     st.sidebar.slider('Starting Y', 1, 100), \
                     st.sidebar.slider('Ending X', 1, 100, 10), \
                     st.sidebar.slider('Ending Y', 1, 100, 10)
    
    st.subheader("DDA Line Algorithm")
    st.pyplot(act1.DDALine(_act1_x0, _act1_y0, _act1_x1, _act1_y1, 'ro'))
    st.subheader("Bresenham's Line Algorithm")
    t.pyplot(act1.bresenham(_act1_x0, _act1_y0, _act1_x1, _act1_y1, 'ro'))
    st.subheader("Midpoint Line Algorithm")
    st.pyplot(act1.midpoint(_act1_x0, _act1_y0, _act1_x1, _act1_y1))
    

