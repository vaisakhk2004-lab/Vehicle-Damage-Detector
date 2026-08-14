# Vehicle Damage Detector
Live app:https://vehicle-damage-detector-qnxvweeysk4mtjbopoondh.streamlit.app

This app let's you drag and drop an image of a car and it will tell you what kind of damage it has.
The model is trained on third quarter front and rare view hence the picture should capture the third quarter front or rare view of a car. 

![app](screenshots/app_interface.png)

### Model Details
1. Used ResNet50 for transfer learning
2. Model was trained on around 1700 images with 6 target classes
   1. Front Normal
   1. Front Crushed
   1. Front Breakage
   1. Rear Normal
   1. Rear Crushed
   1. Rear Breakage
3. Also,built an Api for damage detection using FastAPI
### Set Up

1. To get started, first install the dependencies using:
    ```commandline
     pip install -r requirements.txt
    ```
   
2. Run the streamlit app:
   ```commandline
   streamlit run app.py
##  Results

The  model achieved approximately **82% validation accuracy** on the validation dataset.
![app](screenshots/confusion_matrix.png)