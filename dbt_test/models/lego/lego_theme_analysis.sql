SELECT
    ls."themeGroup",
    ls.subtheme,
    SUM(ls.pieces) AS pieces,
    ROUND(SUM(ls."US_retailPrice"::numeric), 2) AS total_price
FROM {{ ref("lego_sets") }} AS ls
GROUP BY ls."themeGroup", ls.subtheme



-- select * from  {{ ref("lego_sets") }}