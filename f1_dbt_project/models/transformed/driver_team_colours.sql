{{ config(materialized='table') }}

WITH team_colours AS (
    SELECT 'alpine' AS team_name, '#00A1E8' AS hexColour
    UNION ALL
    SELECT 'aston_martin', '#229971'
    UNION ALL
    SELECT 'ferrari', '#ED1131'
    UNION ALL
    SELECT 'haas', '#9C9FA2'
    UNION ALL
    SELECT 'mclaren', '#F47600'
    UNION ALL
    SELECT 'mercedes', '#00D7B6'
    UNION ALL
    SELECT 'rb', '#4781D7'
    UNION ALL
    SELECT 'red_bull', '#4781D7'
    UNION ALL
    SELECT 'sauber', '#01C00E'
    UNION ALL
    SELECT 'williams', '#1868DB'
)

, driver_team_colours AS (
    SELECT
        dt.driverId
        , dt.constructorIds constructorId
        , tc.hexColour colour
    FROM {{ ref('raw_driver_teams') }} dt
    LEFT JOIN team_colours tc
        ON dt.constructorIds = tc.team_name
)

SELECT * FROM driver_team_colours