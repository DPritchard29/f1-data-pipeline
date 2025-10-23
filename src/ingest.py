from db import get_engine
from fastf1.ergast import Ergast
import pandas as pd
from datetime import date
import time

engine = get_engine()
ergast = Ergast()

season = 2025

print('running ingest')

# Pull race schedule
race_schedule = ergast.get_race_schedule(season=season)
race_schedule = race_schedule[['season','round','raceDate','circuitId']]
race_schedule.to_sql("race_schedule", engine, if_exists="replace", index=False)
print('race schedule ingested')

# Pull driver info
drivers = ergast.get_driver_info(season=season)
drivers = drivers[['driverId','driverNumber','driverCode','driverUrl','givenName','familyName','dateOfBirth','driverNationality']]
drivers.to_sql("drivers", engine, if_exists="replace", index=False)
print('drivers ingested')

# Pull constructor info
constructors = ergast.get_constructor_info(season=season)
constructors = constructors[['constructorId','constructorUrl','constructorName','constructorNationality']]
constructors.to_sql("constructors", engine, if_exists="replace", index=False)
print('constructors ingested')

# Pull circuit info
circuits = ergast.get_circuits(season=season)
circuits = circuits[['circuitId','circuitUrl','circuitName','lat','long','locality']]
circuits.to_sql("circuits", engine, if_exists="replace", index=False)
print('circuits ingested')

# Pull driver and constructor standings
# Calculate how many rounds have been complete this season
current_date = date.today()
rounds_completed = pd.read_sql_query(f"SELECT max(round) FROM race_schedule where date(raceDate) < '{current_date}'", engine).iloc[0,0]

# Loop through standings from all rounds and create a combined dataframe
driver_standings_combined = []
constructor_standings_combined = []

# Pull driver team info
driver_teams = ergast.get_driver_standings(season=season,round=rounds_completed)
driver_teams = driver_teams.content[0]
driver_teams = driver_teams[["driverId","constructorIds"]]
# Take the last constructorId from the list (highest index) to obtain current team
driver_teams["constructorIds"] = driver_teams["constructorIds"].apply(lambda x: x[-1] if isinstance(x, list) and len(x) > 0 else None)
driver_teams.to_sql("driver_teams", engine, if_exists="replace", index=False)
print('driver teams ingested')

for round in range(1,rounds_completed+1):
    time.sleep(0.75)  # delay to avoid rate limits

    # Drivers
    driver_standings = ergast.get_driver_standings(season=season,round=round)
    driver_standings = driver_standings.content[0]
    driver_standings = driver_standings[["position","points","driverId"]]
    # Add season and round metadata
    driver_standings["season"] = season
    driver_standings["round"] = round

    driver_standings_combined.append(driver_standings)

    # Constructors
    constructor_standings = ergast.get_constructor_standings(season=season,round=round)
    constructor_standings = constructor_standings.content[0]
    constructor_standings = constructor_standings[["position","points","constructorId"]]
    # Add season and round metadata
    constructor_standings["season"] = season
    constructor_standings["round"] = round

    constructor_standings_combined.append(constructor_standings)

    # Combine all rounds into one DataFrame for each of drivers and constructors
    driver_standings_all_rounds = pd.concat(driver_standings_combined, ignore_index=True)
    constructor_standings_all_rounds = pd.concat(constructor_standings_combined, ignore_index=True)

driver_standings_all_rounds.to_sql("driver_standings", engine, if_exists="replace", index=False)
constructor_standings_all_rounds.to_sql("constructor_standings", engine, if_exists="replace", index=False)

print('driver standings ingested')
print('constructor standings ingested')
print('ingestion complete')