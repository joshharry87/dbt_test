{{ config(
    materialized='incremental',
    unique_key=['device_id', 'minute'],
    incremental_strategy='merge'
) }}


WITH minute_readings AS (

    SELECT
        device_id,
        date_trunc('day', recorded_at) AS day,
        AVG(value) AS avg_value,
        MIN(value) AS min_value,
        MAX(value) AS max_value,
        COUNT(*) AS reading_count

    FROM sensor_readings

    {% if is_incremental() %}

    WHERE recorded_at >= (
        SELECT COALESCE(
            MAX(minute),
            '1900-01-01'
        )
        FROM {{ this }}
    )

    {% endif %}

    GROUP BY
        device_id,
        date_trunc('day', recorded_at)

),
 distinctPairs as(
SELECT distinct mr1.device_id device_1,
        mr1.day d1_day,
        mr1.avg_value,
        mr1.min_value,
        mr1.max_value,
        mr1.reading_count,
        mr2.device_id device_2,
        mr2.day d2_day,
        mr2.avg_value d2_avg,
        mr2.min_value d2_min,
        mr2.max_value d2_mac,
        mr2.reading_count d2count

FROM minute_readings mr1
JOIN minute_readings mr2 ON 
mr1.day = mr2.day AND 
mr1.device_id <> mr2.device_id
)

SELECT * 
FROM distinctPairs
