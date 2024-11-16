import streamlit as st

st.set_page_config(page_title='Superhero App')

st.title("Let's create your superhero name!")

favorite_color = st.text_input('', placeholder='Enter your favorite color')

st.text(f'Color of choice is: {favorite_color}')

favorite_animal = st.text_input('', placeholder='Enter your favorite animal')
st.text(f'Animal of choice is: {favorite_animal}')

lucky_number = st.number_input('What is your lucky number?', step=1)
st.text(f'Number of choice is: {lucky_number}')

if st.button('Generate my superhero name'):
    st.subheader(f'Your superhero name is The {favorite_color} {favorite_animal} {lucky_number}!')