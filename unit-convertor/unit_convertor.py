import streamlit as st

def convert_unit(value, from_unit, to_unit):
    conversions = {
        'meter_to_kilometer': 0.001, # 1 meter = 0.001 kilometer
        'kilometer_to_meter': 1000, # 1 kilometer = 1000 meter
        'gram_to_kilogram': 0.001, # 1 gram = 0.001 kilogram
        'kilogram_to_gram': 1000, # 1 kilogram = 1000 gram   
    }
    key = f'{from_unit}_to_{to_unit}' # create a key for the conversation

    if key in conversions:
        conversion = conversions[key]
        return value * conversion
    else:
        return 'Conversion not supported'

st.title('Unit Convertor')
value = st.number_input('Enter the value : ')
unit_from = st.selectbox('Convert from : ',['meter','kilometer','gram','kilogram'])
unit_to = st.selectbox('Convert to : ',['meter','kilometer','gram','kilogram'])

if st.button('Convert'):
    result = convert_unit(value, unit_from, unit_to)
    st.markdown(f"<p class='converted-text'>Converted Value: {result}</p>", unsafe_allow_html=True)
    
st.markdown(
        """
    <style>
        [data-testid="stAppViewContainer"] {
            background: linear-gradient(135deg, #123061, #0d1b2a);
            height: 100vh;
         h1 {
            color: white ;
            text-align: center;
        }    
        label {
            color: white ;
            font-size: 18px 
        }
        div[data-baseweb="select"] {
            background-color: lightgray ;
            border-radius: 5px ;
        }
        .converted-text {
            color: white ;
            font-size: 22px ;
            font-weight: bold ;
            text-align: center;
            background-color: rgba(255, 255, 255, 0.2);
            padding: 10px;
            border-radius: 10px;
        }
    </style>
    """,
    unsafe_allow_html=True
)