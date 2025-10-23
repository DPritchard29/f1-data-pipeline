{{ config(materialized='table') }}

WITH source_data AS (
    SELECT * FROM constructor_standings
)

SELECT * FROM source_data