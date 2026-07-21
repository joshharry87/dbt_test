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
case when year_pieces <> 0 then (coalesce(pieces::numeric, 1) / coalesce(year_pieces::numeric,1)) else 0.0::numeric end yearprop,
case when theme_pieces <> 0 then (coalesce(pieces::numeric,1)/ coalesce(theme_pieces::numeric,1)) else 0.0::numeric end themeprop,
case when  subtheme_pieces <> 0 then (coalesce(pieces::numeric,1) / coalesce(subtheme_pieces::numeric,1)) else 0.0::numeric end subthemeprop,
 year_dollars,
"US_retailPrice"
,year_pieces
, theme_pieces
,subtheme_pieces
	FROM {{ ref("base_lego_piece_analysis") }}