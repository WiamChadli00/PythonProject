import streamlit as st
# To make things easier later, we're also importing numpy and pandas for
# working with sample data.
#import numpy as np
import pandas as pd
st.title('My first app')
st.write("well hello there")

df = pd.DataFrame({
  'first column': ['pink', 'white', 'blue', 'black']
})

option = st.selectbox(
    'choose a color',
     df['first column'])
if option == 'pink':
    #'pink background'
    st.write('pink background')

elif option == 'black':
    'black background'
elif option == 'white':
    'white background'
elif option == 'blue':
    'blue background'
x=st.slider("slide me ",0.0,500.0,600.00)
'you selected',x
y=st.text_input("text")