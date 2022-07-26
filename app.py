#!/usr/bin/env python
# coding: utf-8

# In[ ]:

import streamlit as st
import keras
from PIL import Image, ImageOps
import numpy as np
st.title("Brain Tumor detection app")
st.header("Brain Tumor detection through MRI of Brain")
st.text("Upload a brain MRI Image for image classification as tumor or no-tumor")
from img_classification import teachable_machine_classification
uploaded_file = st.file_uploader("Choose a brain MRI ...", type="jpg")
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded MRI.', use_column_width=True)
    st.write("")
    st.write("Classifying...")
    label = teachable_machine_classification(image, 'brain_tumor_classification.h5')
    if label == 0:
        st.write("The MRI scan has a brain tumor")
    else:
        st.write("The MRI scan is healthy")
st.text("Made by Harshit Harsh")
