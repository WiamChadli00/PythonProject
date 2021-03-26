#streamlit run Streamlittools.py (in terminal)
import streamlit as st
import pandas as pd
import os
import numpy as np
#title
st.title("my first try")
#text
st.write("hello there")
#make a table
df=pd.DataFrame({
                       'first row':[0,8,6],
                       'scnd row':[9,8,6]
})
df
# add checkbox to show dataFrame
if st.checkbox('Show dataframe'):
    chart_data = pd.DataFrame(
       np.random.randn(20, 3),
       columns=['a', 'b', 'c'])

    chart_data
#checkbox
if st.sidebar.checkbox('I agree to the terms'):
    "the box has been checked"
#create a mini database
db= pd.DataFrame({'colonne':["pink","white","green","yellow","blue"]})
db
#make a selectbox(sidebar brings everything to the side)
option = st.sidebar.selectbox("please choose a background color",db)
'great! you selected ',option
#button
left_column, right_column = st.beta_columns(2)
pressed = left_column.button('Press me?')
if pressed:
    right_column.write("Woohoo!")
#create a tab that expands
expander = st.beta_expander("FAQ")
expander.write("Here you could put in some really, really long explanations...")
#text input for one line
textBox=st.text_input("enter text")
textBox
#text input for multiple lines
txt=st.text_area("enter a longer text")
txt
#file input
filename = st.text_input('Enter a file path:')
try:
    with open(filename) as input:
        st.text(input.read())
except FileNotFoundError:
    st.error('File not found.')
