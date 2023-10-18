-- MARSHAL ZVINOIRA'S MySQL server.
SELECT `score`, `name`
FROM `second_table`
WHERE `name` != ""
ORDER BY `score` DESC
