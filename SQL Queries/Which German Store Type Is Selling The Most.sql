SELECT
    ROUND(CAST(SUM(o.product_quantity * p.product_price) AS NUMERIC), 2) AS total_sales,
    s.store_type,
    s.country_code
FROM
    order_table o
JOIN
    dim_products p ON o.product_code = p.product_code
JOIN
    dim_store_details s ON o.store_code = s.store_code
WHERE
    s.country_code = 'DE'
GROUP BY
    s.store_type, s.country_code
ORDER BY
    total_sales;