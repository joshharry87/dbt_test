CREATE TABLE sensor_readings(
    id BIGSERIAL PRIMARY KEY,
    device_id INT,
    recorded_at TIMESTAMP,
    value numeric
);