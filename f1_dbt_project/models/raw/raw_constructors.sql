{{ config(materialized='table') }}

WITH source_data AS (
    SELECT * FROM constructors
)

SELECT * FROM source_data