from db import get_engine
from fastf1.ergast import Ergast
import pandas as pd


engine = get_engine()
ergast = Ergast()

# Pull driver info
drivers = ergast.get_driver_info()
drivers.to_sql("drivers", engine, if_exists="replace", index=False)
print('drivers done')

# Pull constructor info
constructors = ergast.get_constructor_info()
constructors.to_sql("constructors", engine, if_exists="replace", index=False)
print('constructors done')

# Pull circuit info
circuits = ergast.get_circuits()
circuits.to_sql("circuits", engine, if_exists="replace", index=False)
print('circuits done')

# Pull race schedule
race_schedule = ergast.get_race_schedule(2025)
race_schedule.to_sql("race_schedule", engine, if_exists="replace", index=False)
print('race_schedule done')

# Pull race results
race_results = ergast.get_race_results(season=2025,round=1)
race_results = race_results.content[0]
race_results.to_sql("race_results", engine, if_exists="replace", index=False)
print('race_results done')

# Pull sprint 
sprint_results = ergast.get_sprint_results(season=2025,round=2).content[0]
sprint_results.to_sql("sprint_results", engine, if_exists="replace", index=False)
print('sprint_results done')