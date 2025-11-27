import streamlit as st
from data_pull import pull_race_dates, pull_race_info, pull_driver_standings, pull_constructor_standings, pull_circuit_data, pull_driver_data
from datetime import datetime, date
import plotly.express as px
import pandas as pd

def create_race_info():

    dates = pull_race_dates()['race_date'].tolist()

    # Convert string dates to date objects
    dates = [datetime.strptime(d, "%Y-%m-%d").date() for d in dates]

    today = date.today()

    col1, col2 = st.columns(2)
    with col1:
        container = st.container(border=True, height=260)
        container.subheader('Last Race Info:')
        try:
            last_race_date = max([d for d in dates if d < today])
            pull_race_data(container, last_race_date)
        except:
            container.write('Start of Season')
    with col2:
        container = st.container(border=True, height=260)
        container.subheader('Next Race Info:')
        try:
            next_race_date = min([d for d in dates if d >= today])
            pull_race_data(container, next_race_date)
        except:
            container.write('End of Season')
    return

def pull_race_data(container, race_date):
    round, circuit_name, circuit_url = pull_race_info(race_date)
    container.write(f'Race Number: {round}')
    container.write(f'Date: {race_date}')
    container.write(f'Circuit: {circuit_name}')
    container.link_button('Circuit Link', circuit_url)
    return container

def create_current_standings(results_view):
    if results_view == 'Driver Standings':
        df_standings = pull_driver_standings()
    else:
        df_standings = pull_constructor_standings()

    df_standings = df_standings[(df_standings['season'] == df_standings['season'].max()) & (df_standings['round'] == df_standings['round'].max())]
    df_standings = df_standings[['rank', 'name', 'points']].rename(columns={'rank':'Rank', 'name':'Name', 'points':'Points'})
    df_standings = st.dataframe(df_standings, hide_index=True, column_order=['Rank', 'Name', 'Points'])

    return df_standings

def create_by_race_standings(results_view):

    # Toggle between points or rank
    view_type = st.radio('', label_visibility='collapsed', options=['Ranking','Points'], index=0, horizontal=True)

    if results_view == 'Driver Standings':
        df_standings = pull_driver_standings()
    else:
        df_standings = pull_constructor_standings()

    df_standings = df_standings[df_standings['season'] == df_standings['season'].max()]
    colour_map = dict(zip(df_standings['name'], df_standings['colour']))
    y = 'rank' if view_type == 'Ranking' else 'points'

    # Create line plot
    fig = px.line(
        df_standings
        , x='round'
        , y=y
        , color='name'
        , color_discrete_map=colour_map
    )

    # Add axis titles
    fig.update_layout(
        xaxis_title="Race Number"
        , yaxis_title=y.capitalize()
    )

    # Update range for rank view
    if view_type == 'Ranking':
        max_pos = df_standings["rank"].max()
        fig.update_yaxes(
            autorange=False
            , range=[max_pos + 0.5, 0.5]
            , tickmode="array"
            , tickvals=list(range(1, int(max_pos) + 1))
            , ticktext=[str(i) for i in range(1, int(max_pos) + 1)]
        )

    return st.plotly_chart(fig)

def create_circuit_chart():
    df_circuit = pull_circuit_data()
    
    fig = px.scatter_mapbox(
        df_circuit
        , lat="lat"
        , lon="long"
        , hover_name="circuitName"
        , hover_data={"circuitId": True}
        , size_max=20
        , zoom=1
        , height=500
        , mapbox_style="carto-positron"
    )

    # Customise hover template
    fig.update_traces(
        customdata = df_circuit[['circuitName','locality','lat','long','circuitUrl']]
        , hovertemplate=(
            "<b>Circuit Name:</b> %{customdata[0]}<br>"
            "<b>Location:</b> %{customdata[1]}<br>"
            "<b>Latitude:</b> %{customdata[2]}<br>"
            "<b>Longitude:</b> %{customdata[3]}<extra></extra>"
        )
    )

    return st.plotly_chart(fig)

def show_driver_info():

    df_driver = pull_driver_data()

    drivers = df_driver['driverName'].sort_values()
    driver = st.selectbox('Select a driver', drivers, index=0)

    df = df_driver[df_driver['driverName']==driver]

    name = df['driverName'].tolist()[0]
    team = df['constructorName'].tolist()[0]
    code = df['driverCode'].tolist()[0]
    dob = df['dob'].tolist()[0]
    number = df['driverNumber'].tolist()[0]
    nationality = df['driverNationality'].tolist()[0]
    url = df['driverUrl'].tolist()[0]

    with st.container(border=True):
        col1, col2 = st.columns(2)
        with col1:
            st.subheader(name)
            st.write(f'Team: {team}')
            st.write(f'Code: {code}')
            st.write(f'DOB: {dob}')
        with col2:
            st.write(' ')
            st.write(' ')
            st.write(' ')
            st.write(f'Number: {number}')    
            st.write(f'Nationality: {nationality}')
            st.link_button('Link', url)

    return 