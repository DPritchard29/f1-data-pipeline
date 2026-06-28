import sqlite3
import pandas as pd
import streamlit as st
from pathlib import Path

# Get repo root
base_path = Path(__file__).parent.parent
db_path = base_path / "db/f1.db"


@st.cache_data(ttl=3600)
def pull_race_dates():
    with sqlite3.connect(db_path) as conn:
        race_dates = pd.read_sql_query("SELECT * FROM race_dates", conn)
    return race_dates


@st.cache_data(ttl=3600)
def pull_race_info(race_date):
    race_date = str(race_date)
    query = "SELECT round, circuitName, circuitUrl FROM race_info WHERE raceDate = ?"
    with sqlite3.connect(db_path) as conn:
        race_dates = pd.read_sql_query(query, conn, params=(race_date,))

    round = race_dates['round'].iat[0]
    circuit_name = race_dates['circuitName'].iat[0]
    circuit_url = race_dates['circuitUrl'].iat[0]
    return round, circuit_name, circuit_url


@st.cache_data(ttl=3600)
def pull_driver_standings():
    with sqlite3.connect(db_path) as conn:
        df_driver_standings = pd.read_sql_query("SELECT * FROM driver_rankings_over_time", conn)
    return df_driver_standings


@st.cache_data(ttl=3600)
def pull_constructor_standings():
    with sqlite3.connect(db_path) as conn:
        df_constructor_standings = pd.read_sql_query("SELECT * FROM constructor_rankings_over_time", conn)
    return df_constructor_standings


@st.cache_data(ttl=3600)
def pull_circuit_data():
    with sqlite3.connect(db_path) as conn:
        df_circuits = pd.read_sql_query("SELECT * FROM raw_circuits", conn)
    return df_circuits


@st.cache_data(ttl=3600)
def pull_driver_data():
    with sqlite3.connect(db_path) as conn:
        df_driver_info = pd.read_sql_query("SELECT * FROM driver_info", conn)
    return df_driver_info