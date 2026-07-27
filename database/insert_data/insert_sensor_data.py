import random
from datetime import datetime, timedelta

import psycopg2
from psycopg2.extras import execute_values

LOOKBACKDAYS= 1
LOOKFORWARDDAYS=2
DATAAMOUNT = 10
# Database connection settings
DB_CONFIG = {
    "host": "localhost",
    "database": "appdb",
    "user": "admin",
    "password": "password123",
    "port": 5432
}


def generate_sensor_data(rows=DATAAMOUNT):
    data = []

    start_time = datetime.now() - timedelta(days=LOOKBACKDAYS-LOOKFORWARDDAYS)

    for _ in range(rows):
        device_id = random.randint(1, 50)

        # Random timestamp within last 30 days
        recorded_at = start_time + timedelta(
            seconds=random.randint(0, LOOKBACKDAYS * 24 * 60 * 60)
        )

        # Random sensor value
        value = round(random.uniform(0, 100), 2)

        data.append(
            (
                device_id,
                recorded_at,
                value
            )
        )

    return data


def insert_sensor_data(data):
    query = """
        INSERT INTO sensor_readings
        (device_id, recorded_at, value)
        VALUES %s
    """

    with psycopg2.connect(**DB_CONFIG) as conn:
        with conn.cursor() as cursor:
            execute_values(
                cursor,
                query,
                data
            )

        conn.commit()


if __name__ == "__main__":
    rows = generate_sensor_data(DATAAMOUNT)

    insert_sensor_data(rows)

    print(f"Inserted {len(rows)} sensor readings")