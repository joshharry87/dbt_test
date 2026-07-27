{{ config(
    materialized='incremental',
    unique_key=['device_id', 'minute'],
    incremental_strategy='merge'
) }}

WITH minute_readings AS (

    SELECT
        device_id,
        date_trunc('minute', recorded_at) AS minute,
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
        date_trunc('minute', recorded_at)

)

SELECT *
FROM minute_readings