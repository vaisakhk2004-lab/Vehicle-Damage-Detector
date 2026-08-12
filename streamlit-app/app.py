import streamlit as st
from helper import predict_damage
st.title('🚗 Vehicle Damage Detector',text_alignment='center')
uploaded_image=st.file_uploader('Upload File',type=['jpg','png','jpeg'])
if uploaded_image:
    st.image(uploaded_image,caption='Uploaded Image')
    predicted=predict_damage(uploaded_image)
    if predicted=='F_Breakage':
            st.info('Front Breakage')
    elif predicted=='F_Crushed':
            st.info('Front crushed')
    elif predicted=='F_Normal':
            st.info('No Damage!')
    elif predicted=='R_Breakage':
            st.info('Rear Breakage')
    elif predicted=='R_Crushed':
            st.info('Rear crushed')
    else:
        st.info('No Damage!')





