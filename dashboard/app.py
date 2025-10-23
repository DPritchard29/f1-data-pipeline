import streamlit as st

# Define the pages
about = st.Page("1_about.py", title="About This Dashboard")
main_page = st.Page("2_main_page.py", title="Main Page", icon="🏎️")
circuits_and_drivers = st.Page("3_circuits_and_drivers.py", title="Circuit & Driver Info", icon="🏆")

# Set up navigation
pg = st.navigation([about, main_page, circuits_and_drivers])

# Run the selected page
pg.run()