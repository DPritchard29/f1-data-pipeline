{{ config(materialized='table') }}

-- Rank positions of all drivers with a position value
WITH base AS (
  SELECT
    season
    , round
    , driverId
    , position
    , points
    , ROW_NUMBER() OVER (
      PARTITION BY season, round
      ORDER BY COALESCE(position, 9999)
    ) AS rank
  FROM {{ ref('raw_driver_standings') }}
)

-- Find the highest valid position after each race
, max_pos AS (
  SELECT
    season
    , round
    , MAX(position) AS max_pos
  FROM {{ ref('raw_driver_standings') }}
  WHERE position IS NOT NULL
  GROUP BY season, round
)

-- Create and append non-positioned driver rankings
, driver_all_rankings as (
SELECT
  b.season
  , b.round
  , b.driverId
  , CASE
    WHEN b.position IS NOT NULL THEN b.position
    ELSE m.max_pos + ROW_NUMBER() OVER (
           PARTITION BY b.season, b.round
           ORDER BY b.rank
         )
         - (SELECT COUNT(*) FROM {{ ref('raw_driver_standings') }} r2 WHERE r2.season = b.season AND r2.round = b.round AND r2.position IS NOT NULL)
  END AS rank
  , b.points
FROM base b
JOIN max_pos m
  ON b.season = m.season AND b.round = m.round
)

SELECT
    r.season
    , r.round
    , r.rank
    , r.points
    , d.givenName || ' ' || d.familyName name
    , dtc.colour
FROM driver_all_rankings r
LEFT JOIN {{ ref('raw_drivers') }} d
    ON r.driverId = d.driverId
LEFT JOIN {{ ref('driver_team_colours') }} dtc
    ON r.driverId = dtc.driverId