SELECT 
    ROUND(SUM(CAST(dim_products.product_price * order_table.product_quantity AS numeric)), 2) AS total_sales,
    dim_date_times.month
FROM 
    dim_date_times
INNER JOIN 
    order_table ON dim_date_times.date_uuid = order_table.date_uuid
INNER JOIN 
    dim_products ON dim_products.product_code = order_table.product_code
GROUP BY 
    dim_date_times.month
ORDER BY 
    total_sales DESC
LIMIT 7;
