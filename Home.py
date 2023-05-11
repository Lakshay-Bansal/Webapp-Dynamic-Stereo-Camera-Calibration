#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 27 12:16:27 2023

@author: lakshayb
"""

import streamlit as st
import matplotlib.pyplot as plt

st.title("Camera Calibration")
st.text("We can work with two method of camera calibration:")
st.text("1. Calibration Pattern")
st.text("2. Dynamic Scene for calibration parameter correction")

fig, ax = plt.subplots()
ax.scatter([1, 2, 3], [1, 2, 3])
plt.title("Try scatter plot")
plt.xlabel("Time")
plt.ylabel("Amount")
st.pyplot(fig)

# st.altair_chart(my_chart)

# st.image("./../Single Capture Algo.png")

st.graphviz_chart("""
                  digraph{
                      "Capture image" -> "Feature extraction"
                      "Feature extraction" -> "Feature matching" 
                      "Feature matching" -> "Epipolar estimation"
                      "Epipolar estimation" -> "Bundle Adjustment"}
                  """)


path_left = st.text_input("Add path of images captured by left camera of stereo setup")
path_right = st.text_input("Add path of images captured by right camera of stereo setup")

left, right = st.columns(2)

choice = left.button("Dynamic calibration")
choice = right.button("Calibration pattern based calibration")

if choice == "Dynamic calibration":
    st.write("It uses dynaic real scene for calibration")

if choice == "Calibration pattern based calibration":
    st.write("Use fixed checkerboard pattern for camera calibration")


method = st.radio("Select the method", ["Dynamic scene", "Checkerboard pattern"], index=0)
st.write("You had selected", method)

interval = st.slider("Interval", min_value=1, max_value=5, value=1, step=1)

st.write(interval)


navig = st.sidebar.radio("Navigation", ["Home", "Theory", "Dynamic Calibration", "Single Capture Calibration", "Inbuilt Function Calibration"])

if navig == "Theory":
    st.write("Why????")
    st.balloons() # use when calibration result are calculated



method = st.sidebar.selectbox("Select method", ["Dynamic scene", "Checkerboard pattern"])
if method == "Dynamic scene":
    st.write("Awesome")

if method == "Checkerboard pattern":
    st.write("Obselete")
