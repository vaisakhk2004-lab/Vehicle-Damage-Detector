import streamlit as st
import requests
st.title('🚗 Vehicle Damage Detector',text_alignment='center')
uploaded_image=st.file_uploader('Upload File',type=['jpg','png','jpeg'])
if uploaded_image:
    st.image(uploaded_image,caption='Uploaded Image')
    if st.button('Predict Damage'):
       request=requests.post('http://127.0.0.1:8000/predicted-damage',files={'file':(uploaded_image.name,uploaded_image.getvalue(),uploaded_image.type)
                                                                             }
                             )
       if request.status_code== 200:
           result=request.json()
           predicted=result["prediction"]
           if predicted == 'F_Breakage':
               st.info('Front Breakage')
           elif predicted == 'F_Crushed':
                       st.info('Front crushed')
           elif predicted == 'F_Normal':
               st.info('No Damage!')
           elif predicted == 'R_Breakage':
               st.info('Rear Breakage')
           elif predicted == 'R_Crushed':
               st.info('Rear crushed')
           else:
               st.info('No Damage!')
           st.success('Successfully Predicted Damage')
       else:
           st.error('Oops! Something went wrong.Please try again')







