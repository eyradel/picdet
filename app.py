import streamlit as st
import cv2 
from PIL import Image
from cvzone.FaceDetectionModule import FaceDetector
import numpy as np
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}

            </style>
            <html><body><p></p><body/></html>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)
detector = FaceDetector()
upload =st.file_uploader("upload image")
if st.checkbox("show/hide"):
	image = np.array(Image.open(upload))
	placeholders = st.columns(1)
	img,bboxs = detector.findFaces(image)
	capture = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
	placeholders[0].image(img)






