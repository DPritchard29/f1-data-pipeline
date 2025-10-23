{{ config(materialized='table') }}

WITH source_data AS (
    SELECT * FROM race_schedule
)

SELECT * FROM source_data