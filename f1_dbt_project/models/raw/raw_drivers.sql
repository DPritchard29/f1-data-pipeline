{{ config(materialized='table') }}

WITH source_data AS (
    SELECT * FROM main.drivers
    WHERE driverNumber IS NOT NULL --Removes any drivers that haven't raced
)

SELECT * FROM source_data