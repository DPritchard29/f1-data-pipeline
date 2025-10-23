{{ config(materialized='table') }}

WITH driver_data AS (
    SELECT 
        rd.driverId
        , rd.driverNumber
        , rd.driverCode
        , rd.driverUrl
        , date(rd.dateOfBirth) dob
        , rd.driverNationality
        , rd.givenName || ' ' || rd.familyName driverName
    FROM {{ ref('raw_drivers') }} rd
)

, driver_data_combined AS (
    SELECT 
        d.driverName
        , d.driverNumber
        , d.driverCode
        , d.driverUrl
        , d.dob
        , d.driverNationality
        , rc.constructorName
        , dt.colour
    FROM driver_data d
    LEFT JOIN {{ ref('driver_team_colours') }} dt
        ON d.driverId = dt.driverId
    LEFT JOIN {{ ref('raw_constructors') }} rc
        ON dt.constructorId = rc.constructorId
)

SELECT * FROM driver_data_combined