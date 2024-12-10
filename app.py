import numpy as np
import streamlit as st
import sklearn as sk
import pandas as pd
import pickle


st.set_page_config(
    page_title= "MP",
    page_icon= "Hi"
)

st.title("Welcome Page")
st.sidebar.success("Welcome! You are on the homepage. Click the 'Let's Go' button to continue.")


def load_css(file_path):
    with open(file_path) as f:
        st.html(f"<style>{f.read()}</style>")
import pathlib
css_path = pathlib.Path('styles.css')
load_css(css_path)


#with open('rfc.pkl', 'rb') as f:
 #   model = pickle.load(f)

tab1 = st.tabs(["Home"])


st.header("Predicting the ideal brand for your shopping needs.") 
st.image("clothing.jpg")
if st.button("Let's go!"):
    st.switch_page("pages/2_Prediction & Brands.py")



   # st.write("What is your ideal price?")
    #price = st.number_input("Input Price")
   # st.write("What type of clothing are you looking for?")
   # st.write("Jacket, Jeans, Dresses, T-shirts, Shoes, or a Sweater?")
   # clothing_type = st.text_input("Choose Type").capitalize()
   # clothing_list = {
    #    "Jacket": 6,
     #   "Jeans": 2,
     #   "Shoes": 2,
      #  "Sweater": 4,
       # "T-shirt": 5,
       # "Dress": 1 }   

   # clothing_number = clothing_list.get(clothing_type)


  #  brand_predicted = np.array([[price, clothing_number]])
 
        
  #  prediction = model.predict(brand_predicted)
   # st.write(pd.DataFrame(prediction, columns = ["Adidas", "New Balance", "Nike", "Reebok", "Under Armour", "Puma"]))

        
