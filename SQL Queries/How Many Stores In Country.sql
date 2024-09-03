SELECT country_code AS country,
COUNT(country_code) AS total_num_stores
FROM dim_store_details
GROUP BY country 
ORDER BY total_num_stores DESC;