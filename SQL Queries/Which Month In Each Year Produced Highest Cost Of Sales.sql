SELECT
    ROUND(CAST(SUM(o.product_quantity * p.product_price) AS NUMERIC), 2) AS total_sales,
    dt.year,
    dt.month
FROM
    order_table o
JOIN
    dim_products p ON o.product_code = p.product_code
JOIN
    dim_date_times dt ON o.date_uuid = dt.date_uuid
GROUP BY 
    dt.year, dt.month
ORDER BY 
    total_sales DESC
LIMIT 10;