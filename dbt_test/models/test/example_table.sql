
{{ config(materialized='table') }}

select
    1 as id,
    'Alice' as name

union all

select
    2,
    'Bob'
union all
select    3,
     'Josh'