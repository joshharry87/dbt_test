making a quick thing


setup docker server for local dev:
    docker build -t my-postgres .

    docker run -d \
        --name postgres-db \
        -p 5432:5432 \
        -v postgres_data:/var/lib/postgresql/data \
        my-postgres

docker run -d --name postgres-db -e POSTGRES_USER=admin -e POSTGRES_PASSWORD=password123 -e POSTGRES_DB=appdb -p 5432:5432 -v postgres_data:/var/lib/postgresql/data postgres:16

Python:
py install 3.12
py -3.12 -m venv .venv

Set-ExecutionPolicy -Scope CurrentUser RemoteSigned

.venv\Scripts\Activate.ps1

python -m pip install --upgrade pip

python -m pip install dbt-core==1.12.0 dbt-postgres==1.11.0

check:

dbt --version

python -m dbt.cli.main init dbt_test


$env:DBT_PROFILES_DIR=".\profiles"

dbt:  

dbt debug --profiles-dir profiles

dbt run --profiles-dir profiles



API
uvicorn main:app --reload