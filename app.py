import streamlit as st
import pandas as pd
from PIL import Image
import pickle
import numpy as np
import os
from sklearn.preprocessing import OneHotEncoder
from sklearn.pipeline import Pipeline




MODEL_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)),'data/rf_app_pickle.pkl')

model = pickle.load(open('data/rf_app_pickle.pickle', 'rb'))




image = Image.open('logo.png')

colT1,colT2, colT3 = st.columns([1,8,1])
with colT2:
    st.image(image, width=700)


image = Image.open('logo2.png')

colT1,colT2, colT3 = st.columns([1,1,1])
with colT2:
    st.image(image, width=100)



st.markdown("<h1 style='text-align: center; color: blue;'>CO2 Emissions Predictions</h1>", unsafe_allow_html=True)

# # welcome info
st.info(":high_brightness: Welcome here !  caracteristiques batiments")



def main():


	PrimaryPropertyType = st.selectbox(
    		'What is your property Use ?',
    		('Low-Rise Multifamily', 'Mixed Use Property', 'Senior Care Community', "University"))


	NumberofFloors = st.number_input('Number of floors')
	st.write('The current number is ', NumberofFloors)

	BuildingAge = st.number_input('Age of the building')
	st.write('The current number is ', BuildingAge)

	harvesine_distance = st.number_input('Distance from Seattle Center')
	st.write('The current number is ', harvesine_distance)


	# # welcome info
	st.info(":high_brightness: Welcome here !  Hop,  you can predict the energy use by the building in Seattle and the GHG emissions by year")

	NaturalGas = st.number_input('NaturalGas(kBtu)')
	st.write('The current number is ', NaturalGas)

	SteamUse = st.number_input('SteamUse(kBtu)')
	st.write('The current number is ', SteamUse)

	GHGEmissionsIntensity = st.number_input('GHGEmissionsIntensity')
	st.write('The current number is ', GHGEmissionsIntensity)


	SourceEUI = st.number_input('SourceEUI(kBtu/sf)')
	st.write('The current number is ', SourceEUI)




	d = {'NaturalGas(kBtu)': [NaturalGas], 'SteamUse(kBtu)': [SteamUse],'GHGEmissionsIntensity': [GHGEmissionsIntensity],'SourceEUI(kBtu/sf)': [SourceEUI], 'PrimaryPropertyType': [PrimaryPropertyType], 'NumberofFloors': [NumberofFloors], 'harvesine_distance': [harvesine_distance], 'BuildingAge': [BuildingAge]}   
	#d = {'NaturalGas(kBtu)': [100], 'SteamUse(kBtu)': [100],'GHGEmissionsIntensity': [100],'SourceEUI(kBtu/sf)': [100], 'PrimaryPropertyType': ["University"], 'NumberofFloors': [100], 'harvesine_distance': [100], 'BuildingAge': [100]}
	X_test = pd.DataFrame(data=d)


	st.dataframe(X_test)

	y_pred = model.predict(X_test)




	if st.button('Predict Consumption'):
   		st.write('The building consumption is ', float(y_pred))
	else:
    		st.write('Hit the button')

if __name__ == '__main__':
    main()