import streamlit as st
import random
import string
# import pyperclip

def generate_password(length, use_digits,use_special_chars):
    characters = string.ascii_letters

    if use_digits:
        characters += string.digits

    if use_special_chars:
        characters += string.punctuation

    return ''.join(random.choice(characters) for _ in range(length))

st.title("Password Generator")

length = st.slider("Password Length", min_value=6, max_value=30, value=12)

use_digits = st.checkbox('Include Digits')
use_special_chars = st.checkbox('Include Special Characters')

if st.button('Generate Password'):
    password = generate_password(length, use_digits, use_special_chars)
    st.success(f"Generated Password: {password}")



st.write('Build with ❤️ by Usama Jameel!')

# st.markdown(
#         """
#     <style>
#         [data-testid="stAppViewContainer"] {
#             background-color: #e3f2fd;
#             height: 100vh;
#             text-align: center;
            
#        }
#     </style>
#     """,
#     unsafe_allow_html=True
# )