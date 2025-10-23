{{ config(materialized='table') }}

WITH source_data AS (
    SELECT * FROM driver_teams
)

SELECT * FROM source_data