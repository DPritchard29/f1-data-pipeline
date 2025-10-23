{{ config(materialized='table') }}

WITH source_data AS (
    SELECT * FROM driver_standings
)

SELECT * FROM source_data