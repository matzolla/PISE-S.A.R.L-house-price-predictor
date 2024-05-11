# import necessary librairies
# 
import streamlit as st

import numpy as np
import string
import pickle
st.set_option('deprecation.showfileUploaderEncoding',False)
model = pickle.load(open('model.pkl','rb'))


def main():
  st.markdown("<h1 style='text-align: center; color: White;background-color:#e84343'>House Price Predictor</h1>", unsafe_allow_html=True)
  st.markdown("<h3 style='text-align: center; color: Black;'>Drop in The required Inputs and we will do  the rest.</h3>", unsafe_allow_html=True)
  st.markdown("<h4 style='text-align: center; color: Black;'>PISE S.A.R.L prototype version by STARK</h4>", unsafe_allow_html=True)
  st.sidebar.header("What is this Project about?")
  st.sidebar.text("It a Web app that would help the user in determining the price of a house .")
  st.sidebar.header("What tools where used to make this?")
  st.sidebar.text("The Model was made using a dataset from Kaggle along with using Kaggle notebooks to train the model. We made use of Sci-Kit learn in order to make our Linear Regression Model.")



  year_pay = st.slider("Input Your Year of house Payment",2012.5,2013.0)
  house_age = st.slider("Input the Age of the House",0.0,43.0)
  nearest_station = st.slider("Enter the distance to the nearest station",23.38,6488.00)
  near_store = st.slider("Enter the number of convinient nearby stores",0,10)
  latitude = st.slider("Longitude location",24.9,25.1)
  longitude= st.slider("Latitude location",121.47,121.56)

  inputs = [[year_pay,house_age,nearest_station,near_store,latitude,longitude]]

  if st.button('Predict'):
    result = model.predict(inputs)
    st.success('The Estimated price of the house is {} per unit area'.format(result))


if __name__ =='__main__':
  main()
