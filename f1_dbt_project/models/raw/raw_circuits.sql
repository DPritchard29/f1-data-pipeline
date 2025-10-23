{{ config(materialized='table') }}

WITH source_data AS (
    SELECT * FROM circuits
)

SELECT * FROM source_data