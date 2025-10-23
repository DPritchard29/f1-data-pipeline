import streamlit as st
from utils import create_circuit_chart, show_driver_info
import pandas as pd

# Main title
st.markdown("<h1 style='text-align: center; color: red;'>Circuits and Drivers</h1>", unsafe_allow_html=True)

# Circuit map
st.markdown("<h3 style='text-align: center; color: red;'>Circuits Around the World</h1>", unsafe_allow_html=True)
create_circuit_chart()

# Driver info
st.markdown("<h3 style='text-align: center; color: red;'>Driver Info</h1>", unsafe_allow_html=True)
show_driver_info()
