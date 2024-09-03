SELECT
    COUNT(*) AS number_of_sales,
    SUM(product_quantity) AS product_quantity_count,
    CASE
        WHEN store_type = 'Web Portal' THEN 'Web'
        ELSE 'Offline'
    END AS location
FROM
    order_table o
JOIN
    dim_store_details dsd ON o.store_code = dsd.store_code
GROUP BY
    location
ORDER BY
    location DESC;