import sqlite3
import pandas as pd
import streamlit as st

def pull_race_dates():
    conn = sqlite3.connect("../db/f1.db")
    race_dates = pd.read_sql_query("SELECT * FROM race_dates", conn)
    conn.close()
    return race_dates

def pull_race_info(race_date):
    conn = sqlite3.connect("../db/f1.db")
    race_date = str(race_date)
    race_dates = pd.read_sql_query(f"SELECT round, circuitName, circuitUrl FROM race_info WHERE raceDate = '{race_date}'", conn)
    round = race_dates['round'][0]
    circuit_name = race_dates['circuitName'][0]
    circuit_url = race_dates['circuitUrl'][0]
    conn.close()
    return round, circuit_name, circuit_url

def pull_driver_standings():
    conn = sqlite3.connect("../db/f1.db")
    df_driver_standings = pd.read_sql_query("SELECT * FROM driver_rankings_over_time", conn)
    conn.close()
    return df_driver_standings

def pull_constructor_standings():
    conn = sqlite3.connect("../db/f1.db")
    df_constructor_standings = pd.read_sql_query("SELECT * FROM constructor_rankings_over_time", conn)
    conn.close()
    return df_constructor_standings

def pull_circuit_data():
    conn = sqlite3.connect("../db/f1.db")
    df_circuits = pd.read_sql_query("SELECT * FROM raw_circuits", conn)
    conn.close()
    return df_circuits

def pull_driver_data():
    conn = sqlite3.connect("../db/f1.db")
    df_driver_info = pd.read_sql_query("SELECT * FROM driver_info", conn)
    conn.close()
    return df_driver_info