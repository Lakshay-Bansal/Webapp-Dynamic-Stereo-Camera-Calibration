#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 27 12:16:27 2023

@author: lakshayb
"""

import streamlit as st
import matplotlib.pyplot as plt
import os
import sys

PWD = os.getcwd()
sys.path.append(rf'{PWD}\Images')


st.title("Camera Model")

st.write('''To familiarise with the process of calibration start calibrating a
monocular and stereo camera by using a conventional Tsai algorithm [13].''')

st.image('Images/PinHole_camera.jpg', 
         caption='''Figure 3.1: Pin hole camera model. 
         Source: https://in.mathworks.com/help/vision/ug/camera-calibration.html ''',
                width=300)

st.write('''
The pinhole camera is as shown in Fig. 3.1. The light reflected from an object that
needs to be captured passes through a pinhole and the image is formed on the
screen of the camera (inverted w.r.t. orientation of the object in the real world i.e.
captured by camera). In the pin-hole camera model, it is assumed that all light rays
are passed through the pinhole’s center before being imaged on the screen. Ideally,
pinhole camera model, which lacks a lens, does not consider lens distortion. The full
camera model that accounts for lens distortion includes radial and tangential lens
distortion.
''')

st.write('''
As shown in Fig. 3.2, the point P (Xw, Yw, Zw) in world coordinate is transformed
to (Xc, Yc, Zc) from the reference frame of camera coordinate system by applying
rotation and translation to the world point (see Eq. 3.1).
''')

st.image('Images/CameraModel_1.jpg', 
         caption='''Figure 3.2: Image formation of pin hole camera via a perspective transform ''',
                width=500)

st.latex(r'''
\begin{equation}
    \begin{bmatrix}
     X_c \\
     Y_c \\
     Z_c
 \end{bmatrix}
  =
 \textbf{R}
 \begin{bmatrix}
     X_{w}\\
     Y_{w}\\ 
     Z_{w}
 \end{bmatrix}
 +
 \textbf{T},
\end{equation} \n
where \textbf{R}, is a $3 \times 3$ rotation matrix and \textbf{T} is a $3 \times 1$ translation matrix.
''')

st.write("Then (Xc, Yc, Zc) is mapped to the image plane after perspective projection as shown in Eq. 3.2:")
st.latex(r'''
\begin{equation}\label{eq:3.2.2}
x = f\frac{X_{c}}{Z_{c}} \quad\mbox{,}\quad y = f\frac{Y_{c}}{Z_{c}}
\end{equation}

Which can be written as:
\begin{equation}
     \begin{bmatrix}
        x'_{im}\\ 
        y'_{im}\\
        z'_{im}
    \end{bmatrix} = K 
    \begin{bmatrix}
        X_{c}\\
        Y_{c}\\
        Z_c
    \end{bmatrix},
\end{equation}
where K is intrinsic matrix.

\begin{equation}\label{eq:3.2.7}
    \textbf{K} = 
    \begin{bmatrix}
        \alpha f & 0 & o_x \\
        0 & \beta f & o_y \\
        0 & 0 & 1
    \end{bmatrix}
\end{equation}

Hence they will be mapped to the image plane in homogeneous coordinate form.

\begin{equation}\label{eq:3.2.9}
    \begin{bmatrix}
        \alpha f & 0 & o_x \\
        0 & \beta f & o_y \\
        0 & 0 & 1
    \end{bmatrix}
    \begin{bmatrix}
        X_{c}\\
        Y_{c}\\
        Z_c
    \end{bmatrix}
    = 
    \begin{bmatrix}
        \alpha f X_c + o_x Z_c \\
        \beta f Y_c + o_y Z_c \\
        Z_c
    \end{bmatrix}
    =
    \begin{bmatrix}
        x'_{im}\\ 
        y'_{im}\\
        z'_{im}
    \end{bmatrix}_{\substack{\text{homogeneous} \\ \text{coord.}}}
\end{equation}
''')
