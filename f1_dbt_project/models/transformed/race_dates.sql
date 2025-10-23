{{ config(materialized='table') }}

WITH source_data AS (
    SELECT
         DISTINCT date(raceDate) race_date
    FROM {{ ref('raw_race_schedule') }} rs
)

SELECT * FROM source_data