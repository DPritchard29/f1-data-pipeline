{{ config(materialized='table') }}

WITH source_data AS (
    SELECT * FROM main.drivers
)

SELECT * FROM source_data