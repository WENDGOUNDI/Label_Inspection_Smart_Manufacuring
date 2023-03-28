# Import Libraries

import streamlit as st
from PIL import Image
import io
import tempfile
import cv2
import numpy as np
import numpy
import imutils
import os
import pickle
from paddleocr import PaddleOCR

# Initialize our OCR engine
ocr_model = PaddleOCR(lang='en', show_log=False, use_angle_cls=True, use_gpu=True, enable_mkldnn=True)


st.set_page_config(
    page_title = "PRODUCT LABEL INSPECTION IN SMART MANUFACTURING")

# Function to receive uploaded images
def saveImage(byteImage):
    bytesImg = io.BytesIO(byteImage)
    imgFile = Image.open(bytesImg)
    return imgFile, bytesImg

# Application of header and file uploader
st.header("PRODUCT LABEL INSPECTION IN SMART MANUFACTURING")
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

# Function to extract the product number from the uploaded file
def extract_prod_num(image):

    result = ocr_model.ocr(image)
    ocr_result = [line[1][0] for line in result[0]]
    prod_num = [i for i in ocr_result if i.startswith("Prod ")]
    prod_num = prod_num[0].split(": ")[1]
    return prod_num

# Function to verify if the extracted product number is in our database
def verify_correctness(prod_num):
    DB_file= open('label_db.pickle', 'rb')
    DB_data = pickle.load(DB_file)
    # close the file
    DB_file.close()
    
    if prod_num in DB_data['prod_numb']:
        return True
    else:
        return False
        

#final_result
if uploaded_file is not None:
    # Read the uploaded image
    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    image = cv2.imdecode(file_bytes, 1)
    st.image(image, channels="BGR")
    extracted_prod_num = extract_prod_num(image)
    st.write(f" The product Number is {extracted_prod_num}")
    final_result = verify_correctness(extracted_prod_num)
    if final_result==True:
        st.success("The Product Number Exist in our Database", icon="✅")
    else:
        st.warning("The Product Number does not Exist in our Database", icon="⚠️")
