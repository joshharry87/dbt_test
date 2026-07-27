#!/usr/bin/env python3

import os
from pathlib import Path

import psycopg2
from psycopg2 import sql

# Configuration
DB_CONFIG = {
    "host": "localhost",
    "port": 5432,
    "dbname": "appdb",
    "user": "admin",
    "password": "password123",
}

MIGRATIONS_DIR = Path("migrations")


def ensure_migration_table(cursor):
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS schema_migrations (
            filename TEXT PRIMARY KEY,
            applied_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
    """)


def applied_migrations(cursor):
    cursor.execute("SELECT filename FROM schema_migrations")
    return {row[0] for row in cursor.fetchall()}


def migration_files():
    return sorted(
        f for f in MIGRATIONS_DIR.iterdir()
        if f.is_file() and f.suffix.lower() == ".sql"
    )


def apply_migration(conn, cursor, filepath):
    print(f"Applying {filepath.name}...")

    with open(filepath, "r", encoding="utf-8") as f:
        sql_script = f.read()

    try:
        cursor.execute(sql_script)

        cursor.execute(
            """
            INSERT INTO schema_migrations (filename)
            VALUES (%s)
            """,
            (filepath.name,)
        )

        conn.commit()
        print(f"✓ Applied {filepath.name}")

    except Exception:
        conn.rollback()
        print(f"✗ Failed {filepath.name}")
        raise


def main():
    conn = psycopg2.connect(**DB_CONFIG)

    try:
        cursor = conn.cursor()

        ensure_migration_table(cursor)
        conn.commit()

        applied = applied_migrations(cursor)

        for migration in migration_files():
            if migration.name in applied:
                print(f"Skipping {migration.name}")
                continue

            apply_migration(conn, cursor, migration)

        print("\nAll migrations complete.")

    finally:
        conn.close()


if __name__ == "__main__":
    main()