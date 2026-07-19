
{{ config(materialized='table') }}

select
    cast(null as integer) as id,
    cast(null as varchar(100)) as name,
    cast(null as timestamp) as created_at

where false