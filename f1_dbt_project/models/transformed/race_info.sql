{{ config(materialized='table') }}

WITH source_data AS (
    select 
        rs.season
        , rs.round
        , DATE(rs.raceDate) raceDate
        , rc.circuitName
        , rc.circuitUrl
    FROM {{ ref('raw_race_schedule') }} rs
    LEFT JOIN {{ ref('raw_circuits') }} rc
        ON rs.circuitId = rc.circuitId
)

SELECT * FROM source_data