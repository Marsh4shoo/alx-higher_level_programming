-- MARSHAL ZVINOIRA'S MYSQL server
-- Displays the max value of a column in a table
SELECT `state`, MAX(`value`) AS `max_temp`
FROM `temperatures`
GROUP BY `state`
ORDER BY `state`;

