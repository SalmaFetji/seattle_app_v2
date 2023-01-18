import streamlit as st
import pandas as pd
from PIL import Image
import pickle
import numpy as np
import os
from sklearn.preprocessing import OneHotEncoder
from sklearn.pipeline import Pipeline






def check_password():
    """Returns `True` if the user had a correct password."""

    def password_entered():
        """Checks whether a password entered by the user is correct."""
        if (
            st.session_state["username"] in st.secrets["passwords"]
            and st.session_state["password"]
            == st.secrets["passwords"][st.session_state["username"]]
        ):
            st.session_state["password_correct"] = True
            del st.session_state["password"]  # don't store username + password
            del st.session_state["username"]
        else:
            st.session_state["password_correct"] = False

    if "password_correct" not in st.session_state:
        # First run, show inputs for username + password.
        st.text_input("Username", on_change=password_entered, key="username")
        st.text_input(
            "Password", type="password", on_change=password_entered, key="password"
        )
        return False
    elif not st.session_state["password_correct"]:
        # Password not correct, show input + error.
        st.text_input("Username", on_change=password_entered, key="username")
        st.text_input(
            "Password", type="password", on_change=password_entered, key="password"
        )
        st.error("😕 User not known or password incorrect")
        return False
    else:
        # Password correct.
        return True

if check_password():

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
	st.info(":high_brightness: Welcome here !  Enter your building characteristics")



	def main():


		PrimaryPropertyType = st.selectbox(
    			'What is your property Use ?',
    			('Low-Rise Multifamily', 'Mid-Rise Multifamily', 'Small- and Mid-Sized Office', 'Large Office', 'Warehouse', 'Mixed Use Property', 'Retail Store', 'Hotel', 'Worship Facility', 'Distribution' , 'Center', 'Hospital' ,  'University', 'Distribution Center'))


		NumberofFloors = st.number_input('Number of floors', step=1)
		st.write('The current number is ', NumberofFloors)

		BuildingAge = st.number_input('Age of the building', step=1)
		st.write('The current number is ', BuildingAge)

		harvesine_distance = st.number_input('Distance from Seattle Center')
		st.write('The current number is ', harvesine_distance)


		# # welcome info
		st.info(":high_brightness: Welcome here !  Hop,  you can predict the GHG emissions of your building in Seattle for a year")

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
		pred = float(y_pred)
		predround = round(pred)





		if st.button('Predict Consumption'):

			st.metric(label="The building consumption (tons per year) is :", value = predround)
   			#st.write('The building consumption (tons per year) is :  ', float(y_pred))
		else:
    			st.write('Hit the button')

	if __name__ == '__main__':
    		main()
    		

