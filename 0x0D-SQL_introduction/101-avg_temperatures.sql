-- Displays Average temperature
SELECT city, AVG(temperature) as avg_temp
FROM temperature_data
GROUP BY city
ORDER BY avg_temp DESC;
