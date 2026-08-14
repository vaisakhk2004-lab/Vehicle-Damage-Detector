import streamlit as st
import requests

st.title('🚗 Vehicle Damage Detector', text_alignment='center')

uploaded_image = st.file_uploader(
    'Upload File',
    type=['jpg', 'png', 'jpeg']
)

if uploaded_image:
    st.image(uploaded_image, caption='Uploaded Image')

    if st.button('Predict Damage'):

        response = requests.post(
            'http://127.0.0.1:8000/predicted-damage',
            files={
                'file': (
                    uploaded_image.name,
                    uploaded_image.getvalue(),
                    uploaded_image.type
                )
            }
        )

        if response.status_code == 200:

            result = response.json()
            predicted = result["prediction"]

            if predicted == 'F_Breakage':
                st.info('Front Breakage')

            elif predicted == 'F_Crushed':
                st.info('Front Crushed')

            elif predicted == 'F_Normal':
                st.info('No Damage!')

            elif predicted == 'R_Breakage':
                st.info('Rear Breakage')

            elif predicted == 'R_Crushed':
                st.info('Rear Crushed')

            elif predicted == 'R_Normal':
                st.info('No Damage!')

            st.success('Successfully Predicted Damage')

        else:
            st.error(
                f'API request failed: {response.status_code}'
            )





