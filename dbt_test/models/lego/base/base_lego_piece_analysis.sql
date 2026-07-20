{{ config(
    materialized='table'
) }}





SELECT 
set_id, 
name, 
year, 
theme, 
subtheme, 
"themeGroup", 
category, 
pieces, 
minifigs, 
agerange_min, 
"US_retailPrice"
,SUM(pieces) OVER (
    PARTITION BY year
) as year_pieces
,SUM(pieces) OVER (
    PARTITION BY theme
) as theme_pieces
,SUM(pieces) OVER (
    PARTITION BY theme, subtheme
) as subtheme_pieces
	FROM {{ ref("lego_sets") }}
