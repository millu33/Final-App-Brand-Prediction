import streamlit as st
import numpy as np
import sklearn as sk
import pandas as pd
import pickle

def load_css(file_path):
    with open(file_path) as f:
        st.html(f"<style>{f.read()}</style>")
import pathlib
css_path = pathlib.Path('styles.css')
load_css(css_path)

st.sidebar.success("Navigate between the Your Info and Brands tabs.")

with open('rfc.pkl', 'rb') as f:
    model = pickle.load(f)

tab1, tab2 = st.tabs(["Your Info", "Brands"])

with tab1:
    st.header("Let's see who fits you the best!") 
    st.image("clothes2.jpg")



    st.write("What is your ideal price?")
    price = st.number_input("Input Price")
    st.write("What type of clothing are you looking for?")
    st.write("Options: Jacket, Jeans, Dress, T-shirt, Shoes, Sweater")
    clothing_type = st.text_input("Choose Type").capitalize()
    clothing_list = {
        "Jacket": 6,
        "Jeans": 2,
        "Shoes": 2,
        "Sweater": 4,
        "T-shirt": 5,
        "Dress": 1 }   

    clothing_number = clothing_list.get(clothing_type)


    brand_predicted = np.array([[price, clothing_number]])
 
        
    prediction = model.predict(brand_predicted)
    st.write(pd.DataFrame(prediction, columns = ["Adidas", "New Balance", "Nike", "Reebok", "Under Armour", "Puma"]))

    st.write("Check out the Brands tab to learn more about each one!")

with tab2:
    st.header("We predicted the results based on six brands. Find out more about them below!")
    st.subheader("Adidas")
    st.write("Adidas is the second largest sportswear manufacturer in the world, after Nike, and the largest in Europe. Adidas's mission is to 'change lives through sports.'")
    st.image("adidas.jpg")
    st.subheader("Puma")
    st.write("The Puma brand was founded by Rudolf Dassler in 1948. The company is known for its innovative designs and products in the sports and sports lifestyle industries.")
    st.image("puma.jpg")
    st.subheader("Reebok")
    st.write("Reebok is a global sportswear company that designs, markets, and distributes footwear, apparel, and equipment. The brand is known for its high-quality performance clothing and shoes, and is a pioneer in the sporting goods industry.")
    st.image("reebok.jpg")
    st.subheader("New Balance")
    st.write("New Balance began in 1906 as a one-man operation manufacturing arch supports, and today exists as a global corporation, selling footwear and apparel in over 120 countries worldwide. It is a run specialty brand, but its products span a variety of sport and lifestyle spaces. It maintains a significant manufacturing presence in the US and UK.")
    st.image("newbalance.jpg")
    st.subheader("Under Armour")
    st.write("Under Armour, Inc. is an American sportswear company that manufactures footwear and apparel headquartered in Baltimore, Maryland, United States.Under Armor's USP is 'Performance solutions you never knew you needed and can't imagine living without.'")
    st.image("underarmour.jpg")


        
