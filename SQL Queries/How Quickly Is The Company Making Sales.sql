WITH 
purchase_time_cte AS(
		SELECT year,
				month,
				day,
				timestamp,
		CAST(CONCAT(year, '-', month, '-', day, ' ', timestamp) AS TIMESTAMP) AS purchase_time
		FROM dim_date_times
		ORDER BY year, month, day, timestamp
	),	
next_purchase_time_cte AS(
	SELECT year,
			purchase_time,
			LEAD(purchase_time) OVER (PARTITION BY year ORDER BY purchase_time) AS next_purchase_time
	FROM purchase_time_cte
	ORDER BY year, purchase_time
	),
purchase_time_difference_cte AS (
	SELECT year,
			purchase_time,
			next_purchase_time,
	EXTRACT(EPOCH FROM(next_purchase_time - purchase_time)) AS purchase_time_difference
	FROM next_purchase_time_cte
	ORDER BY year, purchase_time, next_purchase_time
)
SELECT year,
CONCAT(
	'"hours": ', FLOOR(AVG(purchase_time_difference) / 3600), ', ',
	'"minutes": ', FLOOR((AVG(purchase_time_difference) % 3600) / 60), ', ',
	'"seconds": ', ROUND(AVG(purchase_time_difference) % 60), ', ',
	'"milliseconds": ', ROUND((AVG(purchase_time_difference)*1000)%1000)
) 
AS actual_time_taken
FROM purchase_time_difference_cte
GROUP BY year
ORDER BY AVG(purchase_time_difference) DESC
LIMIT 5;