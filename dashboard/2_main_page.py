import streamlit as st
from utils import create_race_info, create_current_standings, create_by_race_standings

# Main title
st.markdown("<h1 style='text-align: center; color: red;'>F1 Dashboard</h1>", unsafe_allow_html=True)

# Produce last and next race info
create_race_info()

# Championship Standings
st.markdown("<h3 style='text-align: center; color: red;'>Current Championship Standings</h1>", unsafe_allow_html=True)

# Switch between drivers and constructors results
options = ['Driver Standings','Constructor Standings']
results_view = st.segmented_control(''
                                    , options=options
                                    , selection_mode='single'
                                    , default=options[0]
                                    , width='stretch'
                                    , label_visibility='collapsed'
                                    )

# Results tables
if results_view:
    create_current_standings(results_view)

    st.markdown("<h3 style='text-align: center; color: red;'>Race By Race</h1>", unsafe_allow_html=True)
    create_by_race_standings(results_view)
else:
    st.write('Select a results option above')