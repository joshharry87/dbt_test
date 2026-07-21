SELECT
    set_id,
    name,
    year,
    theme,
    subtheme,
    "themeGroup",
    category,
    pieces,
    ROUND(yearprop * 100, 5)::text || '%' AS year_proportion,
    ROUND(themeprop * 100, 5)::text || '%' AS theme_proportion,
    ROUND(subthemeprop * 100, 5)::text || '%' AS subtheme_proportion,
    year_pieces,
    theme_pieces,
    subtheme_pieces
FROM {{ ref("int_lego_piece_analysis") }}